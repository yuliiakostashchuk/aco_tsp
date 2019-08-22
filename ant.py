import math


class Ant:
    def __init__(self, instance):

        self.instance = instance
        n = self.instance.n
        self.tour = [None for i in range(n + 1)]
        self.visited = [False for i in range(n)]
        self.tour_length = 0

    def empty_memory(self):
        for visited in self.visited:
            visited = False

    def place(self, step, city):
        self.tour[step] = city
        self.visited[city] = True

    def choose_closest_next(self, phase):

        n = self.instance.n
        distances = self.instance.distances
        next_city = n
        current_city = self.tour[phase - 1]
        min_distance = math.inf

        for city in range(n):
            if self.visited[city]:
                pass
            else:
                if distances[current_city][city] < min_distance:
                    next_city = city
                    min_distance = distances[current_city][city]

        assert 0 <= next_city < n
        self.place(phase, next_city)
