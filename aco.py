import math
import random

from ant import Ant


class AntColony:
    def __init__(self, parameters, instance):

        self.instance = instance
        self.ants = [Ant(instance) for i in range(parameters.n_ants)]
        self.best_so_far_ant = Ant(instance)
        self.restart_best_ant = Ant(instance)
        self.prob_of_selection = [0 for i in range(parameters.nn_ants + 1)]
        # Ensure that we do not run over the last element in the random wheel.
        self.prob_of_selection[parameters.nn_ants] = math.inf
        self.pheromone = [[None for i in range(instance.n)] for i in range(instance.n)]
        self.total = [[None for i in range(instance.n)] for i in range(instance.n)]
        self.nn_tour = None
        self.compute_nn_tour()

    def compute_nn_tour(self):

        ant = self.ants[0]
        phase = 0
        n = self.instance.n
        random.seed()
        city = int(random.random() * n)
        ant.place(phase, city)
        while phase < n - 1:
            phase = phase + 1
            ant.choose_closest_next(phase)
        phase = n
        ant.tour[n] = ant.tour[0]
        ant.tour_length = self.instance.compute_tour_length(ant.tour)
        help = ant.tour_length
        ant.empty_memory()
        self.nn_tour = help

    def report(self, file_name):

        with open(file_name, "w") as file:

            file.write("Attributes:\n")
            for attr in self.__dict__.keys():
                file.write("{}\n".format(attr))

            file.write("\nnn_tour: {}\n".format(self.nn_tour))
