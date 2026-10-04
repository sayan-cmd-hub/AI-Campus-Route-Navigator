
from campus_map import CampusMap
from agents import Pathfinder, Orbit
from experiment import run_experiments


def display_result(agent, start, destination):
    result = agent.find_route(start, destination)

    print(f"\n{'=' * 45}")
    print(agent.name)
    print("=" * 45)

    if result["found"]:
        print("Route:", " -> ".join(result["path"]))
        print(f"Total cost: {result['cost']:.2f} m")
    else:
        print("No valid route found.")

    print(f"Nodes explored: {result['nodes_explored']}")
    print(f"Execution time: {result['time_seconds']:.8f} seconds")

    return result


def main():
    try:
        campus = CampusMap("campus.json")
    except (OSError, ValueError, KeyError) as error:
        print("Error loading campus graph:", error)
        return

    print("\nAI CAMPUS ROUTE NAVIGATOR")
    print("-" * 35)

    print("\nAvailable locations:")
    for location in campus.get_locations():
        print("-", location)

    start = input("\nEnter starting location: ").strip()
    destination = input("Enter destination: ").strip()

    if start not in campus.graph:
        print("Invalid starting location.")
        return

    if destination not in campus.graph:
        print("Invalid destination.")
        return

    display_result(Pathfinder(campus), start, destination)
    display_result(Orbit(campus), start, destination)

    choice = input(
        "\nRun all experiments and update results.csv? (y/n): "
    ).strip().lower()

    if choice == "y":
        try:
            run_experiments(campus)
        except (ValueError, KeyError) as error:
            print("Experiment error:", error)
            print(
                "Check that every experiment location exists "
                "in campus.json."
            )


if __name__ == "__main__":
    main()