from population import Population
from tqdm.notebook import tqdm
from itertools import product
class GeneticAlgorithm:
    def __init__(self, populations_size, tournament_size, crossover_rate, mutation_rate):
        self.populations_size = populations_size
        self.tournament_size = tournament_size
        self.crossover_rate = crossover_rate
        self.mutation_rate = mutation_rate

    def fit(self, iterations, task, show_tqdm=False):
        population = Population(genotyp_size=task.n, population_size=self.populations_size)
        best_history = []
        best_genotyp_history = []
        mean_evaluation_history = []
        the_best_individual, the_best_evaluation = population.best(task)
        if show_tqdm:
            iterator = tqdm(range(iterations))
        else:
            iterator = range(iterations)
        for _ in iterator:
            new_population = Population()
            for _ in range(population.size):
                parent_1 = population.tournament(self.tournament_size, task)
                parent_2 = population.tournament(self.tournament_size, task)
                child = population.crossover(self.crossover_rate, parent_1, parent_2, task)
                child.mutate(self.mutation_rate)
                new_population.add_child(child)

            best_individual, best_evaluation = population.best(task)
            best_genotyp_history.append(best_individual.genotyp)
            if best_evaluation > the_best_evaluation:
                the_best_individual = best_individual
                the_best_evaluation = best_evaluation
            best_history.append(best_evaluation)

            mean_evaluation_history.append(population.evaluate(task).mean())

            population = new_population

        return (
            the_best_individual,
            best_history,
            best_genotyp_history,
            mean_evaluation_history,
        )

    def test_param(self, params, cases, iterations, task):
        param_name = list(params.keys())[0]
        test_set = list(params.values())[0]
        measured_param_history = []
        total = cases * len(test_set)
        t = tqdm(
            enumerate(list(product(test_set, range(cases)))),
            total=total,
            leave=False
        )
        for i, (param, test_case) in t:
            test_histories = []
            if param_name == "Crossover rate":
                self.crossover_rate = param
            elif param_name == "Mutation rate":
                self.mutation_rate = param
            elif param_name == "Population size":
                self.populations_size = param
            elif param_name == "Tournament size":
                self.tournament_size = param
            else:
                raise Exception("param_name", "wrong")

            best, best_history, best_evaluation, mean_evaluation_history = self.fit(iterations, task)
            test_histories.append(best_history)
            measured_param_history.append(test_histories)
        return measured_param_history
