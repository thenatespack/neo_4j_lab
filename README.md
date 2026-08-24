## Neo4j Lab

A Neo4j transit network project (see `Assingment-Instructions.md` for the assignment) plus some
extra Python tooling for visualizing and analyzing the graph.

### Step 1 — Install & run Neo4j

```bash
docker run \
    --restart always \
    --publish=7474:7474 --publish=7687:7687 \
    --env NEO4J_AUTH=neo4j/RcbeVionoDiXdCKzfpLZdmFk \
    neo4j:2026.07.1
```

This runs Neo4j **Community Edition**, which only supports the default
`neo4j` database (no custom database names — `CREATE DATABASE` requires
Enterprise).

### Step 2 — Configure environment variables

Create a `.env` file in the project root:

```
URI=neo4j://localhost
USR=neo4j
PAS=RcbeVionoDiXdCKzfpLZdmFk
DB=neo4j
```

### Step 3 — Install dependencies

```bash
uv sync
```

### Step 4 — Complete the assignment

- `main.py` — the assignment starter. Fill in each `TODO` to build the
  transit graph and write the 5 required + 2 analysis Cypher queries.

```bash
uv run main.py
```

Then write up `analysis.txt` (see Assignment-Instructions.md's Final Deliverables section) and
take a screenshot of your finished graph in Neo4j Browser, saved to
`screenshots/graph.png`.

### Step 5 — Run the extra tooling

`runner.py` seeds a sample transit network, renders a graph screenshot, and
runs route-finding/analysis tools (shortest route, transfer stations,
articulation points, centrality, station-removal impact) on top of the
graph — independent of the assignment work in `main.py`.

```bash
uv run runner.py seed        # populate the database with sample data
uv run runner.py visualize   # render screenshots/graph.png
uv run runner.py analyze     # print route-finding / analysis results
uv run runner.py all         # do all three (also the default with no mode)
```

### Project structure

```
main.py            # assignment starter (TODOs)
hints.html         # progressive hints for each TODO in main.py — open in a browser
runner.py          # CLI for the extra tooling (seed / visualize / analyze / all)
src/                # compiled .pyc only — no readable source, do not hand-edit
  db/
    neo4j.pyc       # Neo4JDriver connection wrapper
    seed.pyc        # sample transit network data + loader
  app.pyc           # shared analysis-printing helper
  analysis.pyc      # route-finding / graph analysis functions
  graph_data.pyc    # Neo4j -> networkx graph fetch
  visualize.pyc     # renders screenshots/graph.png
```

`src/` (everything the extra tooling depends on) ships as compiled `.pyc`
bytecode only — no `.py` source. `main.py` and `main_template.py` stay plain
Python. Python can import a bare `.pyc` placed at a module's path directly
(no matching `.py` needed), which is what makes this work.

`.pyc` bytecode is tied to the **Python version** that compiled it (not the
OS/CPU), so unlike a native-compiled approach this same `src/` works on any
teammate's machine as long as they're on the same Python version this project
requires (3.14). 
