import csv

file = "csv/liste_d'actions.csv"


def load_actions(csv_file):
    liste_actions = []

    with open(csv_file, mode="r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for l in reader:

            liste_actions.append(
                {
                    "action": l["name"],
                    "cost": int(l["price"]),
                    "profit": int(l["profit"]),
                }
            )

    return liste_actions


list_actions = load_actions(file)
max_budget = 500


# Retourne la liste des meilleures actions avec le meilleur profit
def brute_force(list_actions: list, budget_max: int):

    best_cost = 0
    best_profit = 0
    best_combo = []

    calls = 0

    # Analyse chaques possiblilités (prendre ou pas l'action)
    def check_action(index, actual_cost, actual_profit, actual_combo):
        nonlocal best_cost
        nonlocal best_profit
        nonlocal best_combo
        nonlocal calls

        # Condition d'arrêt de la recursivité
        if index == len(list_actions):

            calls += 1
            print(calls, actual_cost, round(actual_profit, 2), actual_combo)

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
        new_cost = actual_cost + action["cost"]
        if new_cost <= budget_max:
            new_profit = actual_profit + action["profit"]
            new_combo = actual_combo + [action["action"]]

            check_action(index + 1, new_cost, new_profit, new_combo)

    # lance une première fois la fonction check_action
    check_action(0, 0, 0, [])

    print(calls)

    # Retourne les valeur du cout, du profit ainsi que la liste avec les meilleures action achetées
    return best_cost, round(best_profit, 2), best_combo


print(brute_force(list_actions, max_budget))
