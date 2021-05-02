import itertools


from data.data_20 import data
from action import Action
from solutions import Solutions
from utils import timeit

MAX_COST = 500


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
