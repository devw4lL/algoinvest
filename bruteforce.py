import pprint
import time
import itertools

# NAME, COST, RETURN in %
actions = [
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


def timeit(method):

    def timed(*args, **kw):
        ts = time.time()
        result = method(*args, **kw)
        te = time.time()
        print(f'Temps écoulé: {te-ts}')
        return result
    return timed


def add_gain(all_actions):
    [action.append((action[1] * action[2]) / 100) for action in all_actions]


def sort_by_return(all_actions):
    for i in range(len(all_actions)):
        for j in range(0, len(all_actions) - i - 1):
            if all_actions[j][3] < all_actions[j+1][3]:
                all_actions[j], all_actions[j+1] = all_actions[j+1], all_actions[j]

@timeit
def bruteforce(all_actions):
    for permuts in itertools.permutations(range(len(all_actions)-1), r=None): #Permutation des indices
        summ = 0
        results = []
        for index in permuts:
            if summ < MAX_COST:
                if (summ + all_actions[index+1][1]) < MAX_COST:
                    summ += all_actions[index][1]
                    results.append(all_actions[index])
                else:
                    cost = 0
                    gain = 0
                    for action in results:
                        cost += action[1]
                        gain += action[3]
                    results.append(f'PRIX ACHAT DES ACTIONS: {cost}, GAIN TOTAL: {gain}')
                    break
        print(results)







def show_results(results):
    rows = [['--', f'{result[0]})', f'{result[1]}', f'{result[2]}',
             f'{result[3]}'] for result in results]
    rows.insert(0, ["--", "NOM ACTION", "PRIX", "GAIN %", "GAIN EN EUROS"])
    max_width = [max(map(len, col)) for col in zip(*rows)]
    [print("  ".join((val.ljust(width) for val, width in zip(row, max_width)))) for row in rows]
    print("\n\r\n\r")
    return True


if __name__ == '__main__':
    # csv = open_csv('dataset1.csv')
    # actions = add_gain(csv)
    add_gain(actions)
    sort_by_return(actions)
    bruteforce(actions)

"""
def bruteforce(all_actions):
    summ = 0
    gain = 0
    results = []
    while summ < MAX_COST:
        for action in all_actions:
            if action[1] < (MAX_COST - summ):
                print('sum', summ, action, gain)
                summ += action[1]
                gain += action[3]
                results.append(action)
    return results
"""