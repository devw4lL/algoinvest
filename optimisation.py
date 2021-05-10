from utils import timeit


class KpDynamic:
    def __init__(self, solutions):
        self.solutions = solutions
        self.results = []

    @timeit
    def knapsack(self, actions, max_cost):
        matrice = [[0 for x in range(max_cost + 1)] for x in range(len(actions) + 1)]
        n = len(actions)
        w = max_cost

        for i in range(1, len(actions) + 1):
            for j in range(1, max_cost + 1):
                if actions[i - 1].price <= j:
                    matrice[i][j] = max(actions[i - 1].profit + matrice[i - 1][j - actions[i - 1].price], matrice[i - 1][j])
                else:
                    matrice[i][j] = matrice[i - 1][j]

        while w >= 0 and n >= 0:
            e = actions[n - 1]
            if matrice[n][w] == matrice[n - 1][w - e.price] + e.profit:
                self.results.append(e)
                w -= e.price
            n -= 1
        self.solutions.add_combinations(0, self.results, matrice[len(actions)][max_cost])
        return True

