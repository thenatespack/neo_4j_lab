"""
CLI entry point for the extra Neo4j transit tooling (on top of the assignment).

Modes:
  seed       - populate the database with the fictional transit network
  visualize  - render the network diagram to screenshots/graph.png
  analyze    - run the route-finding / analysis tools and print results
  clear      - delete all nodes and relationships from the database
  all        - seed, then visualize and analyze (default)

Run with: uv run runner.py [mode]
"""

import argparse

from src.app import print_analysis
from src.db.neo4j import Neo4JDriver
from src.db.seed import seed_database
from src.graph_data import fetch_graph
from src.visualize import render_graph


def run(mode: str) -> None:
    driver = Neo4JDriver()
    try:
        if mode == "clear":
            driver.session.run("MATCH (n) DETACH DELETE n")
            print("Cleared database")
            return

        if mode in ("seed", "all"):
            seed_database(driver)
            print("Seeded database")

        if mode in ("visualize", "analyze", "all"):
            graph = fetch_graph(driver)

        if mode in ("visualize", "all"):
            render_graph(graph, output_path="screenshots/graph.png")
            print("Wrote screenshots/graph.png")

        if mode in ("analyze", "all"):
            print_analysis(driver, graph)
    finally:
        driver.close()


def main() -> None:
    parser = argparse.ArgumentParser(description="Neo4j transit network tooling")
    parser.add_argument(
        "mode",
        choices=["seed", "visualize", "analyze", "clear", "all"],
        default="all",
        nargs="?",
        help="which tooling to run (default: all)",
    )
    args = parser.parse_args()
    run(args.mode)


if __name__ == "__main__":
    main()
