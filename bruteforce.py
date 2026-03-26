from itertools import combinations


# Retourne la liste des meilleures actions avec le meilleur profit
def brute_force_recursive(list_actions: list, budget_max: int):

    best_cost = 0
    best_profit = 0
    best_combo = []
    count = 0
    total_possibilities = 2 ** len(list_actions)

    # Analyse chaques possiblilités (prendre ou pas l'action)
    def check_action(index, actual_cost, actual_profit, actual_combo):
        nonlocal best_cost
        nonlocal best_profit
        nonlocal best_combo
        nonlocal count

        # Condition d'arrêt de la recursivité
        if index == len(list_actions):
            count += 1

            if actual_profit > best_profit:
                best_cost = actual_cost
                best_profit = actual_profit
                best_combo = actual_combo.copy()
            return

        # Initialise l'action au bon index
        action = list_actions[index]

        # Cas où l'action n'est pas prise en compte
        check_action(index + 1, actual_cost, actual_profit, actual_combo)

        # Cas où l'action est prise en compte
        new_cost = actual_cost + action["price"]
        if new_cost <= budget_max:
            new_profit = actual_profit + action["profit"]
            new_combo = actual_combo + [action["action"]]

            check_action(index + 1, new_cost, new_profit, new_combo)

    # lance une première fois la fonction check_action
    check_action(0, 0, 0, [])

    return total_possibilities, count, best_profit, best_cost, best_combo


# Retourne la liste des meilleures actions avec le meilleur profit
def brute_force_itertools(list_actions, budget):
    best_cost = 0
    best_profit = 0
    best_combo = []

    n = len(list_actions)
    count = 0
    total_possibilities = 2**n

    # Boucle qui retourne toutes les combinaisons possible de la liste d'actions
    for i in range(n + 1):
        for combo in combinations(list_actions, i):
            count += 1

            total_cost = sum(action["price"] for action in combo)
            if total_cost <= budget:
                total_profit = sum(action["profit"] for action in combo)
                if total_profit > best_profit:
                    best_cost = total_cost
                    best_profit = total_profit
                    best_combo = [action["action"] for action in combo]

    return total_possibilities, count, best_profit, best_cost, best_combo
