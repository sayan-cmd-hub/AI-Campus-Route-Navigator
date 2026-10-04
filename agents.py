
from search import greedy_best_first, a_star


class RoutingAgent:
    def __init__(self, name, campus):
        self.name = name
        self.campus = campus

    def find_route(self, start, destination):
        raise NotImplementedError


class Pathfinder(RoutingAgent):
    def __init__(self, campus):
        super().__init__("PATHFINDER", campus)

    def find_route(self, start, destination):
        return greedy_best_first(
            self.campus, start, destination
        )


class Orbit(RoutingAgent):
    def __init__(self, campus):
        super().__init__("ORBIT", campus)

    def find_route(self, start, destination):
        return a_star(
            self.campus, start, destination
        )