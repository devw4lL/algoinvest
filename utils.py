import time
import os
import csv


def timeit(method):
    def timed(*args, **kw):
        ts = time.time()
        result = method(*args, **kw)
        te = time.time()
        print(f'Temps écoulé: {te - ts} pour l\'execution de: {method.__name__}')
        return result

    return timed


def load_csv(path, file):
    data = []
    try:
        with open(os.path.join(path, file), 'r') as f:
            r = csv.reader(f, delimiter=',')
            next(r)
            for row in r:
                data.append([row[0], float(row[1]), float(row[2])])

    except ValueError as e:
        print(f'impossible d\'ouvrir le fichier: {file} ERREUR: {e}')
    return data


def check_incorrect_value(data):
    return False if data[1] <= 0 or data[2] <= 0 else True


def check_menu(data):
    try:
        data = int(data)
        if data in [1, 2, 3]:
            return data
        else:
            raise ValueError
    except ValueError as e:
        return f'ERREUR: Le choix du menu est incorrect: {e}'


def check_files(data, files):
    file = {1: "data_20.csv", 2: "dataset1.csv", 3: "dataset2.csv"}
    try:
        data = int(data)
        if data in [1, 2, 3]:
            return file[data]
        else:
            raise ValueError
    except ValueError as e:
        print(f'ERREUR: Le choix du fichier est incorrect: {e}\n' 
              f'{files}')
        check_files(input('Entrer le numero du fichier a analyser:\n'), files)


