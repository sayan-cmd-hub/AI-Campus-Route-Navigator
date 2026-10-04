import csv
import os

from agents import Pathfinder, Orbit


BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DEFAULT_EXPERIMENTS = [
    (
        "Reception of Calcutta University",
        "Library"
    ),
    (
        "Canteen, CU Technology Campus",
        "New Building 2 (Workshop Building)"
    ),
    (
        "Entry Gate 1 (G1)",
        "CSE Laboratory"
    ),
    (
        "Auditorium Hall",
        "CSE_AKC Seminar Hall"
    ),
    (
        "Library",
        "Canteen, CU Technology Campus"
    ),
    (
        "Tower 2 Front Entry",
        "CSE Laboratory"
    ),
    (
        "Tower 2 Rear Entry",
        "CSE Laboratory"
    ),
    (
        "CSE Laboratory",
        "Reception of Calcutta University"
    ),
    (
        "CSE_AKC Seminar Hall",
        "Entry Gate 1 (G1)"
    ),
    (
        "CSE Laboratory",
        "CSE_AKC Seminar Hall"
    ),
    (
        "CSE_Reflxon Room",
        "Library"
    ),
    (
        "Playground of Technology Campus",
        "Entry Gate 2 (G2)"
    ),
    (
        "CSE_AKC Seminar Hall",
        "CSE_Reflxon Room"
    )
]


def run_experiments(campus, filename="results.csv", pairs=None):

    if pairs is None:
        pairs = DEFAULT_EXPERIMENTS

    # Verify every location before running the experiments
    locations = set(campus.get_locations())

    for start, destination in pairs:
        if start not in locations:
            raise ValueError(
                f"Unknown starting location: {start}"
            )

        if destination not in locations:
            raise ValueError(
                f"Unknown destination location: {destination}"
            )

    agents = [
        Pathfinder(campus),
        Orbit(campus)
    ]

    results = []

    for start, destination in pairs:
        for agent in agents:

            result = agent.find_route(start, destination)

            if result["found"]:
                route = " -> ".join(result["path"])
            else:
                route = "No route found"

            row = {
                "agent": agent.name,
                "start": start,
                "destination": destination,
                "route": route,
                "path_cost_m": (
                    round(result["cost"], 2)
                    if result["cost"] is not None
                    else ""
                ),
                "nodes_explored": result["nodes_explored"],
                "time_seconds": round(
                    result["time_seconds"], 8
                ),
                "found": result["found"]
            }

            results.append(row)

            print(f"\nAgent: {agent.name}")
            print(f"Start: {start}")
            print(f"Destination: {destination}")
            print(f"Route: {route}")

            if result["cost"] is not None:
                print(f"Total cost: {result['cost']:.2f} m")

            print(
                f"Nodes explored: {result['nodes_explored']}"
            )
            print(
                f"Execution time: "
                f"{result['time_seconds']:.8f} seconds"
            )
            print(f"Route found: {result['found']}")

    fieldnames = [
        "agent",
        "start",
        "destination",
        "route",
        "path_cost_m",
        "nodes_explored",
        "time_seconds",
        "found"
    ]

    filepath = os.path.join(BASE_DIR, filename)

    with open(
        filepath,
        "w",
        newline="",
        encoding="utf-8"
    ) as file:
        writer = csv.DictWriter(
            file,
            fieldnames=fieldnames
        )

        writer.writeheader()
        writer.writerows(results)

    print("\n" + "=" * 45)
    print("ALL EXPERIMENTS COMPLETED")
    print("=" * 45)
    print(f"Experiments: {len(pairs)}")
    print(f"Agents: {len(agents)}")
    print(f"Total result rows: {len(results)}")
    print(f"Results saved to: {filepath}")

    return results
