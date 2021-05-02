import itertools
from collections import OrderedDict
import functools
import time

data = [
    ["Action-1", 20, 5],
    ["Action-2", 30, 10],
    ["Action-3", 50, 15],
    ["Action-4", 70, 20],
    ["Action-5", 60, 17],
    ["Action-6", 80, 25],
    ["Action-7", 22, 7],
    ["Action-8", 26, 11],
    ["Action-9", 48, 13],
    ["Action-10", 34, 27],
    ["Action-11", 42, 17],
    ["Action-12", 110, 9],
    ["Action-13", 38, 23],
    ["Action-14", 14, 1],
    ["Action-15", 18, 3],
    ["Action-16", 8, 8],
    ["Action-17", 4, 12],
    ["Action-18", 10, 14],
    ["Action-19", 24, 21],
    ["Action-20", 114, 18],
]
MAX_COST = 500


class Action:
    instances = []

    def __init__(self, action):
        self.name = action[0]
        self.price = float(action[1])
        self.profit_per_cent = float(action[2])
        self.profit = (self.price * self.profit_per_cent) / 100
        self.instances.append(self)

    def __repr__(self):
        return f'Nom de l\'action: {self.name} - ' \
               f'Prix d\'achat: {self.price} - ' \
               f'Benefice en %: {self.profit_per_cent} - ' \
               f'Benefice apres deux ans: {self.profit}\n'


class Solutions:

    def __init__(self):
        self.index = 0
        self.actions = None
        self.all_results = OrderedDict()
        self.nbr_results = 1

    def __repr__(self):
        return f'-------------MEILLEUR SOLUTION---------------\n' \
               f'{"".join([str(action) for action in self.all_results[1][:-2]])}' \
               f'PRIX TOTAL: {self.all_results[1][-2]}, PROFIL: {self.all_results[1][-1]}'

    def add_combinations(self, index, action, total_price):
        self.all_results[index] = action
        self.all_results[index].append(round(total_price, 2))

    def add_profit(self):
        for k, value in self.all_results.items():
            self.all_results[k].append((round(sum([v.profit for v in value if isinstance(v, Action)]), 2)))

    def sort_by_best_profit(self):
        self.all_results = sorted(self.all_results.values(), key=lambda x: x[-1], reverse=True)


def timeit(method):
    @functools.wraps(method)
    def timed(*args, **kw):
        ts = time.time()
        result = method(*args, **kw)
        te = time.time()
        print(f'Temps écoulé: {te - ts} pour l\'execution de: {method.__name__}')
        return result

    return timed


@timeit
def knapsack_bruteforce(action_list):
    combinations = []
    for i in range(len(action_list)):
        [combinations.append([action_list[x] for x in action]) for action in
         [combis for combis in itertools.combinations(range(0, len(action_list)), i) if combis]]
    # print(len(combinations))
    for i, actions in enumerate(combinations):
        total_price = sum([action.price for action in actions])
        if total_price < MAX_COST:
            A_solutions.add_combinations(i, actions, total_price)  # ajouter total_price
    return True


if __name__ == "__main__":
    A_solutions = Solutions()
    knapsack_bruteforce([Action(action) for action in data])
    A_solutions.add_profit()
    A_solutions.sort_by_best_profit()
    print(A_solutions)

