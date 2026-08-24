"""
Neo4j Transit Network Assignment — Student Starter

Fill in each TODO below to complete the assignment (see Docs.md):
  Part 3 — build the transit graph (Station/Line nodes, CONNECTS_TO/ON_LINE relationships)
  Part 4 — the 5 required Cypher queries
  Part 5 — 2 analysis questions of your choosing

Run with: uv run main.py

--- How to run a query and use the results ---
`driver.session.run(cypher, **params)` sends a Cypher query and returns a
Result you can iterate over; each item is a Record you index like a dict,
e.g. record["name"]. A typical query function looks like:

    result = driver.session.run(
        "MATCH (s:Station) RETURN s.name AS name ORDER BY name"
    )
    for record in result:
        print(f"  {record['name']}")

Always pass values as query parameters (`$name` in the Cypher + `name=...` as
a keyword argument to `.run()`) instead of f-string-ing them into the query
text — it's how the driver avoids Cypher injection, and it's what lets Neo4j
cache/reuse the query plan.

Each function below is called directly from main() and is expected to print
its own results (it doesn't need to `return` anything).

Stuck on a TODO? Open hints.html in a browser — it has progressive hints for
each function below, from vague to fairly specific.
"""

from src.db.neo4j import Neo4JDriver  # pyright: ignore[reportMissingImports]


def build_graph(driver: Neo4JDriver) -> None:
    """Part 3: create your Station and Line nodes and CONNECTS_TO / ON_LINE relationships."""
    session = driver.session

    # TODO: create a Line node for each transit line in your network.
    # Use MERGE (not CREATE) so re-running this function doesn't create duplicates.

    # TODO: create a Station node for each station in your network.

    # TODO: create ON_LINE relationships connecting each Station to its Line(s).
    # A station that appears on more than one Line is a transfer station —
    # you need at least 2 of those (Docs.md Part 1).

    # TODO: create CONNECTS_TO relationships between adjacent stations, with a
    #       `minutes` property. CONNECTS_TO is directed — if you want a route
    #       to work in both directions, create it a second time reversed.
    raise NotImplementedError("TODO: build the transit graph")


def show_all_stations(driver: Neo4JDriver) -> None:
    """Required query 1: show all stations."""
    # TODO: query for every station and print each one.
    raise NotImplementedError


def stations_on_line(driver: Neo4JDriver, line_name: str) -> None:
    """Required query 2: show stations on a particular line."""
    # TODO: query for stations on the given line and print each one.
    raise NotImplementedError


def stations_connected_to(driver: Neo4JDriver, station_name: str) -> None:
    """Required query 3: find stations directly connected to a station."""
    # TODO: query for stations directly connected to the given station and print each one.
    raise NotImplementedError


def route_between(driver: Neo4JDriver, start: str, end: str) -> None:
    """Required query 4: find a route between two stations (variable-length path)."""
    # TODO: find a path from start to end and print the stations along the way.
    raise NotImplementedError


def most_connected_station(driver: Neo4JDriver) -> None:
    """Required query 5: find the most connected station."""
    # TODO: find the station(s) with the most connections and print the results.
    raise NotImplementedError


def transfer_points(driver: Neo4JDriver) -> None:
    """Analysis question 1: which stations are transfer points?"""
    # TODO: find stations that are on more than one line and print each one.
    raise NotImplementedError


def line_with_most_stations(driver: Neo4JDriver) -> None:
    """Analysis question 2: which line has the most stations?"""
    # TODO: count stations per line and print the results.
    raise NotImplementedError


def main() -> None:
    driver = Neo4JDriver()
    try:
        build_graph(driver)

        print("All stations:")
        show_all_stations(driver)

        print("\nStations on Red Line:")
        stations_on_line(driver, "Red Line")

        print("\nStations connected to Central Station:")
        stations_connected_to(driver, "Central Station")

        print("\nRoute from Riverside to Airport:")
        route_between(driver, "Riverside", "Airport")

        print("\nMost connected station:")
        most_connected_station(driver)

        print("\nTransfer points:")
        transfer_points(driver)

        print("\nLine with the most stations:")
        line_with_most_stations(driver)
    finally:
        # Always close the driver, even if a query above raised — otherwise
        # the connection to Neo4j is left open.
        driver.close()


if __name__ == "__main__":
    main()
