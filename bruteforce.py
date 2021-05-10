import itertools

from utils import timeit


class Bruteforce:

    def __init__(self, solutions):
        self.combinations = []
        self.solutions = solutions

    @timeit
    def knapsack_bruteforce(self, action_list, max_cost):
        """
        O(2^n)
        Args:
            action_list:

        Returns:

        """

        for i in range(len(action_list)):
            [self.combinations.append([action_list[x] for x in action]) for action in
             [combis for combis in itertools.combinations(range(0, len(action_list)), i) if combis]]
        for i, actions in enumerate(self.combinations):
            total_price = sum([action.price for action in actions])
            if total_price < max_cost:
                self.solutions.add_combinations(i, actions, total_price)
        return True
