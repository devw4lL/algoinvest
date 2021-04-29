import pprint
from collections import OrderedDict
from operator import getitem
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
        print(f'Temps écoulé: {te - ts}')
        return result

    return timed


def add_gain(all_actions):
    [action.append((action[1] * action[2]) / 100) for action in all_actions]


def sort_by_return(all_actions):
    for i in range(len(all_actions)):
        for j in range(0, len(all_actions) - i - 1):
            if all_actions[j][3] < all_actions[j + 1][3]:
                all_actions[j], all_actions[j + 1] = all_actions[j + 1], all_actions[j]


def sort_by_total_return(all_actions):
    return OrderedDict(sorted(all_actions.items(), key=lambda x: getitem(x[1], 'gain'), reverse=True))


@timeit
def bruteforce(all_actions):
    all_results = {}
    all_combinaison = []
    count = 0
    for i in range(len(all_actions)):
        [all_combinaison.append(combis) for combis in
         itertools.combinations(range(0, len(all_actions)), i)]  # Permutation des indices #Permutation des indices
    all_combinaison.pop(0)
    for combi in all_combinaison:
        count += 1
        all_results[count] = {'action': [], 'cout': 0, 'gain': 0}
        for index in combi:
            if all_results[count]['cout'] < MAX_COST and (all_results[count]['cout'] + all_actions[index][1]) < MAX_COST:
                all_results[count]['action'].append(all_actions[index][0])
                all_results[count]['cout'] += all_actions[index][1]
                all_results[count]['gain'] += round(all_actions[index][3], 2)
    return all_results


def show_results(results):
    rows = [['--', f'{result["action"]})', f'{result["cout"]}', f'{result["gain"]}'] for result in results.values()]
    rows.insert(0, ["--", "NOM DES ACTION", "PRIX TOTAL", "GAIN APRES 2 ANS"])
    max_width = [max(map(len, col)) for col in zip(*rows[:20])]
    [print("  ".join((val.ljust(width) for val, width in zip(row, max_width)))) for row in rows[:20]]
    print("\n\r\n\r")
    return True


if __name__ == '__main__':
    add_gain(actions)
    sort_by_return(actions)
    results = bruteforce(actions)
    pprint.pprint(show_results(sort_by_total_return(results)))

