import os
import csv
import pprint
"""
- Enlever les valeurs négatives.
- Enlever les 0 gain.
- Calculer les gain en euros
"""
PATH = os.path.join(os.path.dirname(__file__), "data")
MAX_COST = 500


def open_csv(file):
    data = []
    try:
        with open(os.path.join(PATH, file), 'r') as f:
            r = csv.reader(f, delimiter=',')
            for row in r:
                data.append(row)

    except ValueError as e:
        print(f'impossible d\'ouvrir le fichier: {file} ERREUR: {e}')
    return data


def add_gain(file):
    file.pop(0)
    for i in range(len(file)):
        if file[i][1] != '0.0':
            file[i].append((float(file[i][1]) * float(file[i][2]) / 100))
        else:
            file[i].append(float(file[i][2]))
    return file


def show_results(results):
    rows = [['--', f'{result[0]})', f'{result[1]}', f'{result[2]}',
             f'{result[3]}', f'{result[4]}'] for result in results]
    rows.insert(0, ["--", "NOM ACTION", "PRIX", "GAIN %", "GAIN EN EUROS", "GAIN EN EUROS POUR 500EUROS"])
    max_width = [max(map(len, col)) for col in zip(*rows)]
    [print("  ".join((val.ljust(width) for val, width in zip(row, max_width)))) for row in rows]
    print("\n\r\n\r")
    return True