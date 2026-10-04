
import heapq
import itertools
import time


CSE_LOCATIONS = {
    "CSE Laboratory",
    "CSE_AKC Seminar Hall",
    "CSE_Reflxon Room"
}

TOWER_ENTRIES = {
    "Tower 2 Front Entry",
    "Tower 2 Rear Entry"
}

ACCESS_CORRIDOR = TOWER_ENTRIES | {"Parking Area"}


def get_next_zone(location, phase, neighbor, destination_is_cse):

    if neighbor in CSE_LOCATIONS:
        if location in CSE_LOCATIONS or (
            location == "Lift Area" and phase == "inside"
        ):
            return "inside"
        return None

    if phase == "inside":
        if location in CSE_LOCATIONS:
            if neighbor == "Lift Area":
                return "exit"
            if neighbor in CSE_LOCATIONS:
                return "inside"
            return None

        if location == "Lift Area":
            if neighbor in CSE_LOCATIONS:
                return "inside"
            if neighbor == "Tower 2 Rear Entry":
                return "exit"
            return None
    if phase == "approach":
        if neighbor == "Lift Area":
            if location == "Tower 2 Rear Entry":
                return "inside"
            return None

        if neighbor in ACCESS_CORRIDOR:
            return "approach"
        return "outside"

    if phase == "exit":
        if location == "Lift Area":
            if neighbor == "Tower 2 Rear Entry":
                return "exit"
            return None

        if location in ACCESS_CORRIDOR:
            if neighbor in ACCESS_CORRIDOR:
                return "exit"

            if location in TOWER_ENTRIES:
                return "outside"

            return None
    if phase == "outside":
        if neighbor == "Lift Area" and destination_is_cse:
            return None

        if neighbor in TOWER_ENTRIES and destination_is_cse:
            return "approach"

        if neighbor in CSE_LOCATIONS:
            return None

        return "outside"

    return None


def reconstruct_path(parent, state):
    path = []

    while state is not None:
        path.append(state[0])
        state = parent.get(state)

    path.reverse()
    return path


def search(campus, start, destination, algorithm):
    if start not in campus.graph:
        raise ValueError(f"Unknown starting location: {start}")

    if destination not in campus.graph:
        raise ValueError(f"Unknown destination: {destination}")

    if algorithm not in {"greedy", "astar"}:
        raise ValueError("Unknown search algorithm.")

    start_time = time.perf_counter()

    destination_is_cse = destination in CSE_LOCATIONS

    if start in CSE_LOCATIONS or (
        start == "Lift Area" and destination_is_cse
    ):
        initial_phase = "inside"
    elif start in TOWER_ENTRIES and destination_is_cse:
        initial_phase = "approach"
    else:
        initial_phase = "outside"

    start_state = (start, initial_phase)

    frontier = []
    counter = itertools.count()

    initial_h = campus.get_heuristic(start, destination)

    heapq.heappush(
        frontier,
        (initial_h, next(counter), start_state)
    )

    parent = {start_state: None}
    costs = {start_state: 0.0}
    explored_states = set()
    nodes_explored = 0

    while frontier:
        _, _, state = heapq.heappop(frontier)

        if state in explored_states:
            continue

        explored_states.add(state)
        nodes_explored += 1

        location, phase = state

        if location == destination:
            elapsed = time.perf_counter() - start_time

            return {
                "found": True,
                "path": reconstruct_path(parent, state),
                "cost": costs[state],
                "nodes_explored": nodes_explored,
                "time_seconds": elapsed
            }

        for neighbor, distance in campus.get_neighbors(location).items():
            next_phase = get_next_zone(
                location,
                phase,
                neighbor,
                destination_is_cse
            )

            if next_phase is None:
                continue

            next_state = (neighbor, next_phase)
            new_cost = costs[state] + distance

            if new_cost >= costs.get(next_state, float("inf")):
                continue

            costs[next_state] = new_cost
            parent[next_state] = state

            h = campus.get_heuristic(neighbor, destination)

            if algorithm == "greedy":
                priority = h
            else:
                priority = new_cost + h

            heapq.heappush(
                frontier,
                (priority, next(counter), next_state)
            )

    elapsed = time.perf_counter() - start_time

    return {
        "found": False,
        "path": [],
        "cost": None,
        "nodes_explored": nodes_explored,
        "time_seconds": elapsed
    }


def greedy_best_first(campus, start, destination):
    return search(campus, start, destination, "greedy")


def a_star(campus, start, destination):
    return search(campus, start, destination, "astar")