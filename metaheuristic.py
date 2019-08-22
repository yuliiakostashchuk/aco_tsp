MAXIMUM_NO_TRIES = 100
LONG_MAX = 2147483647
MAX_ANTS = 1024
INFTY = LONG_MAX
MAX_NEIGHBOURS = 512


class Metaheuristic:
    def __init__(self, args):

        self.set_default_parameters()

        if args.tries is not None:
            self.max_tries = args.tries
            assert 1 <= self.max_tries <= MAXIMUM_NO_TRIES
        if args.tours is not None:
            self.max_tours = args.tours
            assert 1 <= self.max_tours <= LONG_MAX
        if args.time is not None:
            self.max_time = args.time
            assert 0.0 <= self.max_time <= 86400.0
        if args.optimum is not None:
            self.optimal = args.optimum

        # Choose ACO algorithm. mmas_flag is set to True by default
        if args.asys + args.eas + args.ras + args.mmas + args.bwas + args.acs > 1:
            print("Error: more than one ACO algorithm enabled in the command line")
        if args.asys + args.eas + args.ras + args.mmas + args.bwas + args.acs == 1:
            # Disable default ACO algorithm
            self.as_flag = False
            self.eas_flag = False
            self.ras_flag = False
            self.mmas_flag = False
            self.bwas_flag = False
            self.acs_flag = False
            # Enable ACO algorithm
            if args.asys:
                self.as_flag = True
            elif args.eas:
                self.eas_flag = True
            elif args.ras:
                self.ras_flag = True
            elif args.mmas:
                self.mmas_flag = True
            elif args.bwas:
                self.bwas_flag = True
            elif args.acs:
                self.acs_flag = True
        # Set parameters for ACO algorithm without local search
        if self.as_flag:
            self.set_default_as_parameters()
        elif self.eas_flag:
            self.set_default_eas_parameters()
        elif self.ras_flag:
            self.set_default_ras_parameters()
        elif self.mmas_flag:
            self.set_default_mmas_parameters()
        elif self.bwas_flag:
            self.set_default_bwas_parameters()
        elif self.acs_flag:
            self.set_default_acs_parameters()

        # Add local search. ls_flag is set to 3 by default
        if args.localsearch is not None:
            self.ls_flag = args.localsearch
            assert 0 <= self.ls_flag <= 3
        if self.ls_flag:
            self.set_default_ls_parameters()

        if args.ants is not None:
            self.n_ants = args.ants
            assert 1 <= self.n_ants <= MAX_ANTS - 1
        if args.nnants is not None:
            self.nn_ants = args.nnants
            assert 1 <= self.nn_ants <= 100
        if args.alpha is not None:
            self.alpha = args.alpha
            assert 0.0 <= self.alpha <= 100.0
        if args.beta is not None:
            self.beta = args.beta
            assert 0.0 <= self.beta <= 100.0
        if args.rho is not None:
            self.rho = args.rho
            assert 0.000001 <= self.rho <= 1.0
        if args.q0 is not None:
            self.q_0 = args.q0
            assert 0.0 <= self.q_0 <= 1.0
        if args.elitistants is not None:
            self.elitist_ants = args.elitistants
            assert 0 <= self.elitist_ants <= LONG_MAX
        if args.rasranks is not None:
            self.ras_ranks = args.rasranks
            assert 0 <= self.ras_ranks <= LONG_MAX
        if args.nnls is not None:
            self.nn_ls = args.nnls
            assert 0 <= self.nn_ls <= LONG_MAX
        if args.dlb is not None:
            self.dlb_flag = args.dlb
            assert 0 <= self.dlb_flag <= 1

        quiet_flag = args.quiet

    def set_default_parameters(self):

        self.max_tries = 10
        self.max_tours = 0
        self.max_time = 10.0
        self.optimal = 1

        self.n_ants = 25
        self.nn_ants = 20
        self.alpha = 1.0
        self.beta = 2.0
        self.rho = 0.5
        self.q_0 = 0.0
        self.elitist_ants = 0
        self.ras_ranks = 0

        self.nn_ls = 20

        self.ls_flag = 3

        self.dlb_flag = True

        self.as_flag = False
        self.eas_flag = False
        self.ras_flag = False
        self.mmas_flag = True
        self.bwas_flag = False
        self.acs_flag = False

        self.quiet_flag = False
        self.branch_fac = 1.00001
        self.u_gb = INFTY

    def set_default_as_parameters(self):

        assert self.as_flag

        self.n_ants = -1  # -1 means instance size
        self.nn_ants = 20
        self.alpha = 1.0
        self.beta = 2.0
        self.rho = 0.5
        self.q_0 = 0.0
        self.ras_ranks = 0
        self.elitist_ants = 0

    def set_default_eas_parameters(self):

        assert self.eas_flag

        self.n_ants = -1  # -1 means instance size
        self.nn_ants = 20
        self.alpha = 1.0
        self.beta = 2.0
        self.rho = 0.5
        self.q_0 = 0.0
        self.ras_ranks = 0
        self.elitist_ants = self.n_ants

    def set_default_ras_parameters(self):

        assert self.ras_flag

        self.n_ants = -1  # -1 means instance size
        self.nn_ants = 20
        self.alpha = 1.0
        self.beta = 2.0
        self.rho = 0.1
        self.q_0 = 0.0
        self.ras_ranks = 6
        self.elitist_ants = 0

    def set_default_bwas_parameters(self):

        assert self.bwas_flag

        self.n_ants = -1  # -1 means instance size
        self.nn_ants = 20
        self.alpha = 1.0
        self.beta = 2.0
        self.rho = 0.1
        self.q_0 = 0.0
        self.ras_ranks = 0
        self.elitist_ants = 0

    def set_default_mmas_parameters(self):

        assert self.mmas_flag

        self.n_ants = -1  # -1 means instance size
        self.nn_ants = 20
        self.alpha = 1.0
        self.beta = 2.0
        self.rho = 0.02
        self.q_0 = 0.0
        self.ras_ranks = 0
        self.elitist_ants = 0

    def set_default_acs_parameters(self):

        assert self.acs_flag

        self.n_ants = 10
        self.nn_ants = 20
        self.alpha = 1.0
        self.beta = 2.0
        self.rho = 0.1
        self.q_0 = 0.9
        self.ras_ranks = 0
        self.elitist_ants = 0

    def set_default_ls_parameters(self):

        assert self.ls_flag

        self.dlb_flag = True
        self.nn_ls = 20

        self.n_ants = 25
        self.nn_ants = 20
        self.alpha = 1.0
        self.beta = 2.0
        self.rho = 0.5
        self.q_0 = 0.0

        if self.mmas_flag:
            self.n_ants = 25
            self.rho = 0.2
            self.q_0 = 0.00
        elif self.acs_flag:
            self.n_ants = 10
            self.rho = 0.1
            self.q_0 = 0.98
        elif self.eas_flag:
            self.elitist_ants = self.n_ants

    def update_parameters(self, n):
        """Set parameters that are equal to the instance size"""

        if self.n_ants < 0:
            self.n_ants = n

        # Default setting for elitist_ants if EAS is applied is -1
        # elitist_ants value may change if local search is applied
        # or option elitist_ants is used
        if self.eas_flag and self.elitist_ants <= 0:
            self.elitist_ants = n

        self.nn_ls = min(n - 1, self.nn_ls)

        assert self.n_ants < MAX_ANTS - 1
        assert self.nn_ants < MAX_NEIGHBOURS
        assert self.nn_ants > 0
        assert self.nn_ls > 0
