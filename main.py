from fonctions import (
    load_actions,
    display_result_bruteforce,
    display_result_optimized,
)
from bruteforce import brute_force_recursive, brute_force_itertools
from optimized import knapsack, greedy_actions
from sienna import load_actions_sienna, knapsack_sienna, greedy_actions_sienna

file = "csv/liste_d'actions.csv"

actions = load_actions(file)

best_profit, best_cost, best_combo = greedy_actions(actions, 500)
display_result_optimized(best_profit, best_cost, best_combo)
print(" ")

best_profit, best_cost, best_combo = knapsack(actions, 500)
display_result_optimized(best_profit, best_cost, best_combo)
print("")

total_possibilities, count, best_profit, best_cost, best_combo = brute_force_itertools(
    actions, 500
)
display_result_bruteforce(
    total_possibilities, count, best_profit, best_cost, best_combo
)
