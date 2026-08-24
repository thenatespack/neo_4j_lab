# 🚇 Neo4j Transit Network — Group Assignment

## Overview

In this Assignment, you will use Neo4J to model a small transit network.

Your goal is to learn how a real-world system can be represented as a **graph** and then use **Cypher queries** to explore the relationships within that graph.

You are **not** expected to build a complete transit application. Focus on creating a clean graph, writing useful queries, and discovering something interesting about your network.

This repo comes with starter code — see `README.md` for how to install and run
Neo4j and the project dependencies. Once that's set up, you'll do the work
below inside `main.py`, which has a function stub (with `TODO`s) for each
part of this assignment.

**Stuck on the Cypher syntax for a TODO?** Open `hints.html` in your browser.
It has one panel per function with hints that start vague and get more
specific — but even the last hint stops short of a paste-in answer, so try
for real first.

---

## 👥 Groups

* Groups of **Any Size Up to 4**
* Everyone should contribute to the database, queries, and final presentation.

---

# 🎯 Project Goal

Build a Neo4j database that represents a small transit system and answer questions such as:

* What stations are connected?
* What stations are on each line?
* How can a passenger get from one station to another?
* Which station has the most connections?
* Which stations are transfer points?
* What happens if an important station is removed?

---

# 🚉 Part 1 — Choose Your Transit System

Choose **one small transit network**.

You can use:

* UTA TRAX
* A university shuttle system
* A simplified subway system
* A fictional city transit system
* Another public transportation system approved by your instructor

### Keep it small!

Your graph should contain approximately:

* **10–20 stations**
* **1–3 transit lines**
* **At least 2 transfer stations**

You do **not** need to model an entire city's transit system.

---

# 🧩 Part 2 — Design Your Graph

Before building your database, decide what your nodes and relationships represent.

At minimum, include:

### Nodes

```text
Station
Line
```

### Relationships

```text
CONNECTS_TO
ON_LINE
```

For example:

```text
(University)-[:CONNECTS_TO]->(Main Street)
(University)-[:ON_LINE]->(Red Line)
```

You should also add useful properties.

Example:

```text
Station
- name

CONNECTS_TO
- minutes
```

A connection could look like:

```text
(University)-[:CONNECTS_TO {minutes: 6}]->(Main Street)
```

---

# 💾 Part 3 — Build Your Neo4j Database

Create your transit network in Neo4j by filling in `build_graph()` in
`main.py`. It runs on every execution, so use `MERGE` (not `CREATE`) for
your nodes and relationships — that way re-running the script doesn't create
duplicates.

Under the hood, each `session.run(...)` call sends a Cypher statement that
creates your `Station` and `Line` nodes and your `CONNECTS_TO` /
`ON_LINE` relationships — written with `MERGE` and query parameters so it's
safe to re-run.

Your final graph should satisfy the minimum requirements:

* 10–20 stations
* 1–3 lines
* At least 2 transfer stations
* Stations connected to other stations
* Stations associated with transit lines

Not sure what the `MERGE` pattern looks like? Open `hints.html` and expand
the `build_graph()` panel for step-by-step hints.

---

# 🔎 Part 4 — Cypher Queries

Write **at least 5 Cypher queries** that answer useful questions about your network.

Each one has a matching function stub in `main.py` — `show_all_stations`,
`stations_on_line`, `stations_connected_to`, `route_between`, and
`most_connected_station`. Fill in the query and have the function print its
results.

### Required Queries

#### 1. Show all stations

Write a query that returns every station in the graph.

#### 2. Show stations on a particular line

Write a query that returns all the stations that belong to a given line.

#### 3. Find stations directly connected to a station

Write a query that returns the stations directly reachable from a given
station.

#### 4. Find a route between two stations

Write a query — using a variable-length path — that finds a route from one
station to another.

#### 5. Find the most connected station

Write a query that counts how many connections each station has, and
returns the stations ordered by that count.

You may design these queries however you like, or come up with your own
additional ones. If you're not sure how to translate one of these into
Cypher, open `hints.html` — it has a hint panel for each of these five
functions that starts vague and gets progressively more specific, without
ever handing you the finished query.

---

# 🧠 Part 5 — Analyze Your Network

Choose **2 additional questions** to investigate. `main.py` has stubs for
two common ones — `transfer_points` and `line_with_most_stations` — but feel
free to rename/replace them (or add more functions) if your group picks
different questions.

Some ideas:

* Which station has the most connections?
* Which stations are transfer points?
* What is the shortest path between two stations?
* What is the longest route?
* Which line has the most stations?
* Which station would be the best place for a new connection?
* What happens if an important station is removed?
* Which stations are most important for keeping the network connected?

Your answers must be supported by **Cypher queries and results**.

`hints.html` has hint panels for `transfer_points` and
`line_with_most_stations` too, if your group picks those two.

---

# ⭐ Optional Challenge

If your group finishes early, try adding one of these:

* Calculate the fastest route using travel time.
* Find a route with the fewest transfers.
* Add fares and find the cheapest route.

These are **optional** and are not required for full credit.

---

# 📦 Final Deliverables

Submit these files:

```text
main.py
analysis.txt
```

### `main.py`

Your completed starter file, with every `TODO` filled in:

* `build_graph()` — your database creation commands (Part 3)
* Your 5 required query functions (Part 4)
* Your 2 analysis query functions (Part 5)

### `analysis.txt`

Include a short explanation of:

1. What transit system you modeled
2. Why you chose your nodes and relationships
3. Your two analysis questions
4. What you discovered
5. Why Neo4j was useful for this problem

### `screenshots/graph.png`

Include a screenshot of your completed Neo4j graph.

---

# Objectives

* Form groups
* Choose a transit system
* Design your graph
* Fill in `build_graph()` in `main.py`
* Add stations and lines
* Create relationships
* Complete the 5 required query functions in `main.py`
* Check your database
* Take a graph screenshot
* Begin analysis
* Complete the 2 analysis questions
* Finish `analysis.md`


---

# ✅ Minimum Requirements

Your project must include:

* [ ] 10–20 stations
* [ ] 1–3 transit lines
* [ ] At least 2 transfer stations
* [ ] `Station` nodes
* [ ] `Line` nodes
* [ ] `CONNECTS_TO` relationships
* [ ] `ON_LINE` relationships
* [ ] 5 working Cypher queries (as filled-in functions in `main.py`)
* [ ] 2 analysis questions (as filled-in functions in `main.py`)
* [ ] Neo4j graph screenshot
* [ ] Short written analysis

---

# 💡 Guiding Question

> **How can a graph database help us understand how people move through a transit network?**

Focus less on building a huge database and more on demonstrating **why relationships make Neo4j useful for this problem**.