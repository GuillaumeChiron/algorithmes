import csv

file = "csv/liste_d'actions.csv"


def load_actions(csv_file):
    liste_actions = []

    with open(csv_file, mode="r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for l in reader:

            rendement = int(l["Bénéfice (après 2 ans)"].replace("%", ""))
            profit = float(l["Coût par action (en euros)"]) * (rendement / 100)

            liste_actions.append(
                {
                    "action": l["Actions #"],
                    "cost": int(l["Coût par action (en euros)"]),
                    "profit": profit,
                }
            )

    return liste_actions


list_actions = load_actions(file)
max_budget = 500


# Retourne la meilleur combinaison d'actions avec le meilleur cout et le meilleur profit
def brute_force(list_actions, max_budget):

    best_cost = 0
    best_profit = 0
    best_combo = []

    # Analyse l'action et teste les possibilités avec ou sans l'action
    def check_action(index, actual_cost, actual_profit, actual_combo):
        nonlocal best_cost
        nonlocal best_profit
        nonlocal best_combo

        # consition d'arrêt de la fonction
        if index == len(list_actions):
            if actual_profit > best_profit:
                best_profit = actual_profit
                best_cost = actual_cost
                best_combo = actual_combo.copy()
            return

        # recupère l'action à l'index precis et la stock dans action
        action = list_actions[index]

        # test le cas où on ne prend pas l'action

        # test le cas où on prend l'action

    check_action(0, 0, 0, [])

    return best_cost, best_profit, best_combo
