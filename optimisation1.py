import os
import csv
import pprint
import time
import functools

"""
- Enlever les valeurs négatives.
- Enlever les 0 gain.
- Calculer les gain en euros
"""
PATH = os.path.join(os.path.dirname(__file__), "data")
MAX_COST = 500

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
def load_csv(file):
    data = []
    try:
        with open(os.path.join(PATH, file), 'r') as f:
            r = csv.reader(f, delimiter=',')
            next(r)
            for row in r:
                data.append([row[0], float(row[1]), float(row[2])])

    except ValueError as e:
        print(f'impossible d\'ouvrir le fichier: {file} ERREUR: {e}')
    return data


def sort_by(all_actions):  # tri fusion (merge sort) O(n log n) linéaire
    """
    Diviser tableaux en deux.
    Tant que les deux tableaux non vides.
    Comparer la permire valeur de chacun des tableaux.
    Prendre la plus petit valeur et ajouter au tableaux de résultats.
    Ajouter au résultat le tableau non vide restant.
    :param all_actions:
    :return:
    """
    n = len(all_actions)
    # break condition
    if n > 1:
        # split
        mid = n // 2
        left, right = all_actions[:mid], all_actions[mid:]
        sort_by(left)
        sort_by(right)
        # combine
        idx_all = idx_left = idx_right = 0
        while idx_left < len(left) and idx_right < len(right):
            if left[idx_left] < right[idx_right]:
                all_actions[idx_all] = left[idx_left]
                idx_left += 1
            else:
                all_actions[idx_all] = right[idx_right]
                idx_right += 1
            idx_all += 1
        while idx_left < len(left):
            all_actions[idx_all] = left[idx_left]
            idx_left += 1
            idx_all += 1

        while idx_right < len(right):
            all_actions[idx_all] = right[idx_right]
            idx_right += 1
            idx_all += 1


#capacité = MAX_COAST
#element = all_actions
#element[i][1] = all_actions[i][1]
#element[i][2] = all_actions[i][3]
#matrice = res
t = [['Share-AAZC', 36, 18, 6],
 ['Share-ABJM', 21, 38, 8],
 ['Share-ACQS', 32, 1, 0],
 ['Share-ADLV', 18, 4, 0],
 ['Share-AFAJ', 29, 34, 10],
 ['Share-AGPL', 15, 15, 2],
 ['Share-AHQO', 28, 15, 4],
 ['Share-AHYU', 20, 5, 1],
 ['Share-AIQL', 25, 33, 8],
 ['Share-AIRL', 7, 31, 2]]

def knapsack(all_actions):
    n = len(all_actions)
    res = [[0 for x in range(MAX_COST + 1)] for x in range(n + 1)]
    if n > 1:
        for i in range(1, n + 1):
            for w in range(1, MAX_COST + 1):
                if all_actions[i-1][1] <= w:
                    print(all_actions[i-1][3])
                    print(res[i-1])
                    print(all_actions[i-1][3])
                    print(res[i-1][w-all_actions[i-1][3]])
                    res[i][w] = max(all_actions[i-1][3] + res[i-1][w-all_actions[i-1][3]], res[i-1][w])
                else:
                    res[i][w] = res[i-1][w]
        w = MAX_COST
        n = len(all_actions)
        results = []

    while w >= 0 and n >= 0:
        e = all_actions[n-1]
        if res[n][w] == res[n-1][w-e[1]] + e[2]:
            results.append(e)
            w -= e[1]
        n -= 1
    return res[-1][-1], results



@timeit
def clean_incorrect_value(data):
    return [value for value in data if (value[1] and value[2]) >= 0]


def add_gain(data):
    [data[i].append(round(((data[i][1] * data[i][2]) / 100), 2)) for i in range(len(data))]
    return True

def multiply_by_100(data):
    return [value*100 for value in data]

def show_results(results):
    rows = [['--', f'{result[0]})', f'{result[1]}', f'{result[2]}',
             f'{result[3]}', f'{result[4]}'] for result in results]
    rows.insert(0, ["--", "NOM ACTION", "PRIX", "GAIN %", "GAIN EN EUROS", "GAIN EN EUROS POUR 500EUROS"])
    max_width = [max(map(len, col)) for col in zip(*rows)]
    [print("  ".join((val.ljust(width) for val, width in zip(row, max_width)))) for row in rows]
    print("\n\r\n\r")
    return True


if __name__ == "__main__":
    data1 = load_csv('dataset1.csv')
    clean_data1 = clean_incorrect_value(data1)
    if add_gain(clean_data1):
        sort_by(clean_data1)
        #pprint.pprint(clean_data1)
        #print(knapsack(clean_data1))


"""
val = all_actions[index][1] 
wt = all_actions[index][3]
W -> MAX_COAST
"""