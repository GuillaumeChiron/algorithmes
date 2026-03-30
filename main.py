from fonctions import (
    load_actions,
    display_result_bruteforce,
    display_result_optimized,
)
from bruteforce import brute_force_recursive, brute_force_itertools
from optimized import knapsack, greedy_actions
from sienna import load_actions_sienna, knapsack_sienna, greedy_actions_sienna

FILE = "csv/liste_d'actions.csv"
DATASET1 = "csv/dataset1.csv"
DATASET2 = "csv/dataset2.csv"

actions = load_actions_sienna(DATASET2)

best_profit, best_cost, best_combo = knapsack_sienna(actions, 50000)
display_result_optimized(best_profit, best_cost, best_combo)

print(" ")

total_profit, total_cost, actions_selected = greedy_actions_sienna(actions, 50000)
display_result_optimized(total_profit, total_cost, actions_selected)
