
import json


class CampusMap:
    def __init__(self, filename="campus.json"):
        with open(filename, "r", encoding="utf-8") as file:
            data = json.load(file)

        self.locations = data["locations"]
        self.graph = {location: {} for location in self.locations}
        self.heuristics = data.get("heuristics", {})

        for edge in data["edges"]:
            start = edge["from"]
            end = edge["to"]
            distance = float(edge["distance"])

            if start not in self.graph or end not in self.graph:
                raise ValueError("An edge contains an unknown location.")

            if distance < 0:
                raise ValueError("Distance cannot be negative.")

            self.graph[start][end] = distance
            self.graph[end][start] = distance

    def get_neighbors(self, location):
        return self.graph.get(location, {})

    def get_heuristic(self, location, destination):
        return float(
            self.heuristics.get(destination, {}).get(location, 0)
        )

    def get_locations(self):
        return list(self.graph.keys())