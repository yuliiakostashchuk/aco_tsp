import math

from metaheuristic import LONG_MAX


class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y


class TSP:
    def __init__(self, tsplibfile):

        self.name = None
        self.n = None
        self.coordinates = None
        self.distances = None
        self.nn_lists = None

        with open(tsplibfile, "r") as file:
            for line in file:
                buf = line.split()  # Split line into the list
                if buf[0] == "NODE_COORD_SECTION":  # Check for node coordinates
                    break
                if buf[0] == "NAME":  # Read instance name
                    self.name = buf[2]
                elif buf[0] == "DIMENSION":  # Read instance dimension
                    self.n = int(buf[2])
                    assert 2 < self.n < 6000
            if buf[0] == "NODE_COORD_SECTION":  # Check for node coordinates
                self.coordinates = []
                for line in file:
                    if line == "EOF\n":
                        break
                    buf = line.split()  # Split line into the list
                    x = int(buf[1])
                    y = int(buf[2])
                    self.coordinates.append(Point(x, y))

        self.compute_distances()

    def compute_distances(self):
        """Compute distances between nodes"""

        self.distances = [[None for i in range(self.n)] for i in range(self.n)]

        for i, first in enumerate(self.coordinates):
            for j, second in enumerate(self.coordinates):
                self.distances[i][j] = calc_distance(first, second)

    def compute_nn_lists(self, nn):

        if nn >= self.n:
            nn = self.n - 1

        assert self.n > nn

        self.nn_lists = [[None for i in range(nn)] for i in range(self.n)]
        distance_vector = [None for i in range(self.n)]
        help_vector = [None for i in range(self.n)]

        for node in range(self.n):
            for i in range(self.n):
                distance_vector[i] = self.distances[node][i]
                help_vector[i] = i
            distance_vector[node] = LONG_MAX
            sort2(distance_vector, help_vector, 0, self.n - 1)
            for i in range(nn):
                self.nn_lists[node][i] = help_vector[i]

    def compute_tour_length(self, t):

        tour_length = 0

        for i in range(self.n):
            distance = self.distances[t[i]][t[i + 1]]
            tour_length = tour_length + distance

        return tour_length

    def report(self, file_name):

        with open(file_name, "w") as file:

            file.write("Attributes:\n")
            for attr in self.__dict__.keys():
                file.write("{}\n".format(attr))

            file.write("\nDistances:\n")

            for row in self.distances:
                for item in row:
                    file.write("{:<3d}".format(item))
                file.write("\n")

            file.write("\nnn_lists:\n")

            for row in self.nn_lists:
                for item in row:
                    file.write("{:<4d}".format(item))
                file.write("\n")


def calc_distance(point_1, point_2):
    """
    Calculate Euclidean distance between two points.
    For the definition of how to compute this distance see TSPLIB.

    :param Point point_1: First point
    :param Point point_2: Second point
    :rtype: float
    :return: Euclidean distance
    """

    xd = point_1.x - point_2.x
    yd = point_1.y - point_2.y
    distance = int(math.sqrt(xd * xd + yd * yd) + 0.5)
    return distance


def swap2(v, v2, i, j):
    tmp = v[i]
    v[i] = v[j]
    v[j] = tmp
    tmp = v2[i]
    v2[i] = v2[j]
    v2[j] = tmp


def sort2(v, v2, left, right):
    if left >= right:
        return
    swap2(v, v2, left, (left + right) // 2)
    last = left
    for k in range(left + 1, right + 1):
        if v[k] < v[left]:
            last = last + 1
            swap2(v, v2, last, k)
    swap2(v, v2, left, last)
    sort2(v, v2, left, last)
    sort2(v, v2, last + 1, right)
