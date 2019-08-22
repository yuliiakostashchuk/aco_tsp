"""
        http://www.aco-metaheuristic.org/aco-code/public-software.html
        Software package: ACOTSP.V1.03.tgz
        Author: Thomas Stützle
"""

import argparse

from aco import AntColony
from metaheuristic import Metaheuristic
from tsp import TSP


def parse_arguments():

    parser = argparse.ArgumentParser()

    parser.add_argument("tsplibfile", type=str, help="input file in TSPLIB format")
    parser.add_argument("--tries", type=int)
    parser.add_argument("--tours", type=int)
    parser.add_argument("--time", type=float)
    parser.add_argument("--optimum", type=int)
    parser.add_argument("--ants", type=int)
    parser.add_argument("--nnants", type=int)
    parser.add_argument("--alpha", type=float)
    parser.add_argument("--beta", type=float)
    parser.add_argument("--rho", type=float)
    parser.add_argument("--q0", type=float)
    parser.add_argument("--elitistants", type=int)
    parser.add_argument("--rasranks", type=int)
    parser.add_argument("--nnls", type=int)
    parser.add_argument("--localsearch", type=int)
    parser.add_argument("--dlb", type=bool)
    parser.add_argument("--asys", action="store_true")
    parser.add_argument("--eas", action="store_true")
    parser.add_argument("--ras", action="store_true")
    parser.add_argument("--mmas", action="store_true")
    parser.add_argument("--bwas", action="store_true")
    parser.add_argument("--acs", action="store_true")
    parser.add_argument("--quiet", action="store_true")

    args = parser.parse_args()

    return args


if __name__ == "__main__":

    args = parse_arguments()
    heuristic = Metaheuristic(args)

    tsplibfile = args.tsplibfile
    instance = TSP(tsplibfile)

    n = instance.n
    heuristic.update_parameters(n)

    nn = max(heuristic.nn_ls, heuristic.nn_ants)
    instance.compute_nn_lists(nn)
    instance.report("instance_report.txt")

    ant_colony = AntColony(heuristic, instance)
    ant_colony.report("ant_colony_report.txt")
