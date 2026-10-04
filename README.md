# AI Campus Route Navigator

## 1. Project Overview

The **AI Campus Route Navigator** is a Python-based Artificial Intelligence project developed for the AI/ML Lab assignment. The project finds routes between different locations within the University of Calcutta Technology Campus using informed search algorithms.

The campus is represented as a graph in which locations are nodes and the connections between locations are edges. Each edge has an estimated travel distance.

Two search agents are implemented:

* **PATHFINDER:** Greedy Best-First Search
* **ORBIT:** A* Search Algorithm

The project compares these algorithms using route cost, number of nodes explored, and execution time. Experimental results are saved in a CSV file.

## 2. Objectives

The objectives of this project are:

1. Represent the campus map as a graph.
2. Implement Greedy Best-First Search.
3. Implement the A* Search Algorithm.
4. Find routes between specified campus locations.
5. incorporate the special routing restrictions for the CSE zone.
6. Compare the performance of both search agents.
7. Record the routes, path costs, nodes explored, execution times, and search success.
8. Export experimental results to a CSV file.

## 3. Search Algorithms

### 3.1 PATHFINDER — Greedy Best-First Search

PATHFINDER uses the heuristic estimate to prioritize which location to explore next.

The evaluation function is:

`f(n) = h(n)`

Where:

* `n` represents the current node.
* `h(n)` is the estimated distance from node `n` to the destination.
* `f(n)` is the evaluation value used to prioritize nodes.

Greedy Best-First Search attempts to reach the destination by prioritizing locations that appear closer to the goal. It does not generally guarantee the minimum-cost route.

### 3.2 ORBIT — A* Search Algorithm

ORBIT considers both the cost already incurred and the estimated remaining distance.

The evaluation function is:

`f(n) = g(n) + h(n)`

Where:

* `g(n)` is the accumulated cost from the starting location to node `n`.
* `h(n)` is the estimated distance from node `n` to the destination.
* `f(n)` is the combined evaluation value.

A* can find an optimal route when its heuristic and graph-search implementation satisfy the necessary conditions, including appropriate handling of improved paths to previously discovered nodes.

## 4. Campus Map Representation

The campus layout and graph data are stored in `campus.json`.

The graph contains the following locations:

1. Playground of Technology Campus
2. Parking Area
3. Tower 2 Front Entry
4. CSE Laboratory
5. Tower 2 Rear Entry
6. Library
7. CSE_Reflxon Room
8. Lift Area
9. CSE_AKC Seminar Hall
10. Power Area
11. Reception of Calcutta University
12. Canteen, CU Technology Campus
13. CRNN Centre (Nano Technology)
14. Auditorium Hall
15. Garden Area
16. New Building 1 (Electrical & Seminar)
17. New Building 2 (Workshop Building)
18. Entry Gate 1 (G1)
19. Entry Gate 2 (G2)

The graph consists of:

* **Nodes:** Campus locations.
* **Edges:** Connections between locations.
* **Edge costs:** Estimated travel distances.
* **Heuristics:** Estimated distances from locations to the destination.

The distances and heuristic values are estimates based on the modeled campus map; they should not be interpreted as officially measured campus distances.

## 5. Special CSE-Zone Routing Rules

The CSE zone consists of the following locations:

* CSE Laboratory
* CSE_AKC Seminar Hall
* CSE_Reflxon Room

The assignment specifies special restrictions for entering and leaving this zone.

### Entering the CSE zone

The intended entry route passes through Tower 2 Front Entry or Tower 2 Rear Entry and then through Lift Area before reaching a CSE location.

### Moving within the CSE zone

After crossing Lift Area to enter the CSE zone, the route must remain within permitted CSE locations until it returns to Lift Area.

### Exiting the CSE zone

A route leaving the CSE zone must return through Lift Area before continuing to other campus locations.

These restrictions must be enforced by the search logic rather than by hard-coding individual routes. The generated routes should be checked against these rules during testing.

## 6. Project Structure

The project contains the following files:

```text
campus-navigator/
│
├── main.py
├── campus.json
├── campus_map.py
├── agents.py
├── search.py
├── experiment.py
├── results.csv
└── README.md
```

| File            | Description                                                            |
| --------------- | ---------------------------------------------------------------------- |
| `main.py`       | Entry point for running the application and interacting with the user. |
| `campus.json`   | Stores campus locations, connections, distances, and heuristic data.   |
| `campus_map.py` | Loads the campus graph and provides access to campus locations.        |
| `agents.py`     | Defines the PATHFINDER and ORBIT agents.                               |
| `search.py`     | Contains the search algorithms and route-search logic.                 |
| `experiment.py` | Runs predefined test cases and saves experimental results.             |
| `results.csv`   | Stores the results generated by the experiment script.                 |
| `README.md`     | Documents the project, algorithms, execution procedure, and results.   |

## 7. Requirements

* Python 3.14.0
* PyCharm or another Python-compatible IDE
* Standard Python libraries used by the project

The experiment script uses Python's built-in `csv` and `os` modules. These do not require separate installation.

## 8. How to Run the Project

### Step 1: Open the project

Open the `campus-navigator` folder in PyCharm.

### Step 2: Verify the files

Ensure that the required Python files and `campus.json` are present in the project directory.

### Step 3: Run the application

Open `main.py` and run it using PyCharm.

### Step 4: Enter the route details

Enter or select a valid starting location and destination when prompted by the application.

The application runs the search agents and displays their route-search results.

### Step 5: Run the experiments

When prompted to run the predefined experiments, enter:

```text
y
```

The experiment script executes the configured test cases using both PATHFINDER and ORBIT.

### Step 6: View the results

Open `results.csv` in PyCharm or a spreadsheet application.

The CSV file contains the agent name, starting location, destination, route, path cost, nodes explored, execution time, and whether a route was found.

The experiment script overwrites the previous contents of `results.csv` when it generates a new set of results.

## 9. Experimental Setup

The updated experiment configuration contains **13 test cases**. Each test case is executed using both search agents, resulting in **26 experimental records**.

The test cases cover:

1. Reception of Calcutta University to Library.
2. Canteen to New Building 2.
3. Entry Gate 1 to CSE Laboratory.
4. Auditorium Hall to CSE_AKC Seminar Hall.
5. Library to Canteen.
6. Tower 2 Front Entry to CSE Laboratory.
7. Tower 2 Rear Entry to CSE Laboratory.
8. CSE Laboratory to Reception of Calcutta University.
9. CSE_AKC Seminar Hall to Entry Gate 1.
10. CSE Laboratory to CSE_AKC Seminar Hall.
11. CSE_Reflxon Room to Library.
12. Playground of Technology Campus to Entry Gate 2.
13. CSE_AKC Seminar Hall to CSE_Reflxon Room.

Each agent's results are recorded separately so that their routes and performance can be compared.

## 10. Experimental Results

The following table contains the results from the updated `results.csv`.

| Test                                    | Agent      | Cost (m) | Nodes explored | Time (seconds) | Found |
| --------------------------------------- | ---------- | -------: | -------------: | -------------: | ----- |
| Reception → Library                     | PATHFINDER |      230 |              6 |       0.000094 | Yes   |
| Reception → Library                     | ORBIT      |      230 |              6 |       0.000057 | Yes   |
| Canteen → New Building 2                | PATHFINDER |      160 |              3 |       0.000038 | Yes   |
| Canteen → New Building 2                | ORBIT      |      160 |              3 |       0.000034 | Yes   |
| Entry Gate 1 → CSE Laboratory           | PATHFINDER |      318 |              8 |       0.000125 | Yes   |
| Entry Gate 1 → CSE Laboratory           | ORBIT      |      318 |              9 |       0.000455 | Yes   |
| Auditorium → CSE_AKC Seminar Hall       | PATHFINDER |      352 |              8 |       0.000131 | Yes   |
| Auditorium → CSE_AKC Seminar Hall       | ORBIT      |      237 |             10 |       0.000080 | Yes   |
| Library → Canteen                       | PATHFINDER |      265 |              4 |       0.000038 | Yes   |
| Library → Canteen                       | ORBIT      |      245 |              9 |       0.000098 | Yes   |
| Tower 2 Front Entry → CSE Laboratory    | PATHFINDER |      123 |              5 |       0.000046 | Yes   |
| Tower 2 Front Entry → CSE Laboratory    | ORBIT      |      123 |              5 |       0.000042 | Yes   |
| Tower 2 Rear Entry → CSE Laboratory     | PATHFINDER |       43 |              3 |       0.000026 | Yes   |
| Tower 2 Rear Entry → CSE Laboratory     | ORBIT      |       43 |              3 |       0.000024 | Yes   |
| CSE Laboratory → Reception              | PATHFINDER |      248 |              7 |       0.000062 | Yes   |
| CSE Laboratory → Reception              | ORBIT      |      248 |             10 |       0.000170 | Yes   |
| CSE_AKC Seminar Hall → Entry Gate 1     | PATHFINDER |      322 |              9 |       0.000104 | Yes   |
| CSE_AKC Seminar Hall → Entry Gate 1     | ORBIT      |      322 |             12 |       0.000126 | Yes   |
| CSE Laboratory → CSE_AKC Seminar Hall   | PATHFINDER |       15 |              2 |       0.000018 | Yes   |
| CSE Laboratory → CSE_AKC Seminar Hall   | ORBIT      |       15 |              2 |       0.000018 | Yes   |
| CSE_Reflxon Room → Library              | PATHFINDER |       63 |              3 |       0.000040 | Yes   |
| CSE_Reflxon Room → Library              | ORBIT      |       63 |              4 |       0.000043 | Yes   |
| Playground → Entry Gate 2               | PATHFINDER |      540 |              8 |       0.000095 | Yes   |
| Playground → Entry Gate 2               | ORBIT      |      390 |              8 |       0.000086 | Yes   |
| CSE_AKC Seminar Hall → CSE_Reflxon Room | PATHFINDER |       18 |              2 |       0.000026 | Yes   |
| CSE_AKC Seminar Hall → CSE_Reflxon Room | ORBIT      |       18 |              2 |       0.000050 | Yes   |

### 10.1 Route Details

The following are examples of the routes produced by the agents.

**Example 1: Reception to Library**

Both agents produced the same route:

```text
Reception of Calcutta University
→ Power Area
→ Tower 2 Front Entry
→ Parking Area
→ Tower 2 Rear Entry
→ Library
```

The reported path cost was 230 metres for both agents.

**Example 2: Auditorium to CSE_AKC Seminar Hall**

PATHFINDER produced:

```text
Auditorium Hall
→ Canteen, CU Technology Campus
→ Power Area
→ Tower 2 Front Entry
→ Parking Area
→ Tower 2 Rear Entry
→ Lift Area
→ CSE_AKC Seminar Hall
```

Reported cost: 352 metres.

ORBIT produced:

```text
Auditorium Hall
→ Garden Area
→ Library
→ Lift Area
→ CSE_AKC Seminar Hall
```

Reported cost: 237 metres.

**Example 3: Tower 2 Rear Entry to CSE Laboratory**

Both agents produced:

```text
Tower 2 Rear Entry
→ Lift Area
→ CSE Laboratory
```

Reported cost: 43 metres.

**Example 4: Playground to Entry Gate 2**

PATHFINDER reported a cost of 540 metres, while ORBIT reported a cost of 390 metres. The agents selected different routes through the modeled campus graph.

## 11. Analysis and Observations

### 11.1 Route Cost

The results show that the two agents can return routes with different costs.

For Auditorium to CSE_AKC Seminar Hall, ORBIT reported 237 metres compared with PATHFINDER's 352 metres.

For Library to Canteen, ORBIT reported 245 metres compared with PATHFINDER's 265 metres.

For Playground to Entry Gate 2, ORBIT reported 390 metres compared with PATHFINDER's 540 metres.

These results are consistent with the difference between a greedy strategy that prioritizes the heuristic estimate and A*'s use of both accumulated cost and estimated remaining cost. However, the results alone do not prove that every ORBIT route is optimal.

### 11.2 Nodes Explored

The number of nodes explored varies across test cases.

For example:

* Reception to Library: both agents explored 6 nodes.
* Tower 2 Rear Entry to CSE Laboratory: both agents explored 3 nodes.
* CSE Laboratory to CSE_AKC Seminar Hall: both agents explored 2 nodes.
* CSE_AKC Seminar Hall to Entry Gate 1: PATHFINDER explored 9 nodes, while ORBIT explored 12 nodes.

The number of nodes explored depends on the graph, destination, heuristic values, and search implementation.

### 11.3 Execution Time

Execution time is recorded in seconds for every experiment.

The measured times are very small because the modeled campus graph contains a limited number of nodes and edges. Small timing differences may result from interpreter overhead, system activity, and measurement variability.

Therefore, these results should be interpreted as measurements for this particular implementation and graph rather than as a universal comparison of the two algorithms.

### 11.4 Successful Route Finding

All 26 experimental records report `found = True`.

This means that the search implementation returned a route for each of the 13 configured start-destination pairs. It does not, by itself, prove that every returned route satisfies all special CSE-zone restrictions.

## 12. CSV Output Format

The generated CSV file contains the following columns:

```text
agent,start,destination,route,path_cost_m,nodes_explored,time_seconds,found
```

The columns represent:

* `agent`: The algorithm used, PATHFINDER or ORBIT.
* `start`: The starting campus location.
* `destination`: The target campus location.
* `route`: The sequence of locations returned by the algorithm.
* `path_cost_m`: Total reported path cost in metres.
* `nodes_explored`: Number of nodes explored by the search.
* `time_seconds`: Measured execution time in seconds.
* `found`: Whether a route was found.

The updated experiment output contains **26 data rows and one header row**, giving 27 lines in total.

## 13. Limitations

1. The path distances are estimates and may differ from actual walking distances on campus.
2. Heuristic estimates influence the behavior of both search algorithms.
3. A* optimality depends on the heuristic properties and the correctness of the search implementation.
4. Execution-time measurements can vary between runs.
5. Finding a route does not automatically guarantee compliance with the special CSE-zone rules.
6. The experiment covers 13 selected start-destination pairs rather than every possible combination of campus locations.
7. Results depend on the connections and costs represented in `campus.json`.

## 14. Conclusion

The AI Campus Route Navigator demonstrates the application of informed search algorithms to campus route planning.

PATHFINDER uses Greedy Best-First Search with the evaluation function `f(n) = h(n)`, while ORBIT uses A* Search with `f(n) = g(n) + h(n)`.

The campus graph enables the agents to search for routes between different locations. The experimental module records the resulting routes, path costs, nodes explored, execution times, and search success in a CSV file.

The updated experiments demonstrate that different search strategies can produce different routes and path costs. They also show that the number of explored nodes and execution time vary by test case.

Overall, the project provides a practical demonstration of graph-based route planning, heuristic search, experimental comparison, and structured output generation in Python.
