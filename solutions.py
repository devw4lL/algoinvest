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