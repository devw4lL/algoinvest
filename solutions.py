import time
from collections import OrderedDict

from action import Action


class Solutions:

    def __init__(self):
        self.index = 0
        self.actions = None
        self.all_results = OrderedDict()
        self.nbr_results = 1

    def __repr__(self):
        return f'-------------MEILLEUR SOLUTION---------------\n' \
               f'{"".join([str(action.convert_to_usd()) for action in self.all_results[0][:-2]])}' \
               f'PRIX TOTAL: {self.all_results[0][-2] / 100}, PROFIL: {self.all_results[0][-1] / 100}'

    def add_combinations(self, index, action, total_price):
        self.all_results[index] = action
        self.all_results[index].append(total_price)

    def add_profit(self):
        for k, value in self.all_results.items():
            self.all_results[k].append((round(sum([v.profit for v in value if isinstance(v, Action)]), 2)))

    def add_price(self):
        for k, value in self.all_results.items():
            self.all_results[k].insert(-1, (round(sum([v.price for v in value if isinstance(v, Action)]), 2)))

    def sort_by_best_profit(self):
        self.all_results = sorted(self.all_results.values(), key=lambda x: x[-1], reverse=True)