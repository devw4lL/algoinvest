import os

from action import Action
from solutions import Solutions
from bruteforce import Bruteforce
from optimisation import KpDynamic
from utils import timeit, load_csv, check_incorrect_value, check_menu, check_files


MAX_COST = 500 * 100
PATH = os.path.join(os.path.dirname(__file__), "data")
welcome = f'Bienvenu dans le questionnaire d\'action AlgoInvest\n' \
          f'Veuillez identiquer le numéro du menu de votre choix:\n' \
          f'--> 1 pour une résolution par bruteforce.\n' \
          f'--> 2 pour une resolution par knapsack (optimisé).\n' \
          f'--> 3 Quitter.\n'

files = f'Choisir un set de donnees:\n' \
        f'--> 1 data_20.csv (set de 20 action).\n' \
        f'--> 2 dataset1.csv (set de 1000 actions Sienna).\n' \
        f'--> 3 dataset2.csv (set de 1000 actions Sienna).\n'

if __name__ == "__main__":
    running = True
    print(welcome)
    while running:
        choice = check_menu(input('Entrer le numero du menu: '))
        solutions = Solutions()
        if choice == 1:
            print(files)
            file = check_files(input('Entrer le numero du fichier a analyser: \n'), files)
            brute_force = Bruteforce(solutions)
            brute_force.knapsack_bruteforce([Action(action).convert_to_cents() for action in load_csv(PATH, file)],
                                            MAX_COST)
            solutions.add_profit()
            solutions.sort_by_best_profit()
            print(solutions)
        elif choice == 2:
            print(files)
            file = check_files(input('Entrer le numero du fichier a analyser: \n'), files)
            kp_dynamic = KpDynamic(solutions)
            kp_dynamic.knapsack([Action(action).convert_to_cents() for action in load_csv(PATH, file) if
                                 check_incorrect_value(action)], MAX_COST)
            solutions.add_price()
            print(solutions)
        elif choice == 3:
            exit()
        else:
            print(choice)
