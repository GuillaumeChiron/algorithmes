import csv

file = "csv/liste_d'actions.csv"


# Fonction qui permet de récupérer les données d'un fichier csv et retourner une liste de ces données
def load_actions(csv_file):
    list_actions = []

    with open(csv_file, mode="r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for l in reader:

            rendement = float(l["Bénéfice (après 2 ans)"].replace("%", ""))
            profit = float(l["Coût par action (en euros)"]) * (rendement / 100)

            list_actions.append(
                {
                    "action": l["Actions #"],
                    "cost": float(l["Coût par action (en euros)"]),
                    "profit": profit,
                }
            )

    return list_actions


list_actions = load_actions(file)
max_budget = 500


# Retourne la liste des meilleures actions avec le meilleur profit
def brute_force(list_actions: list, budget_max: int):

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
        new_cost = actual_cost + action["cost"]
        if new_cost <= budget_max:
            new_profit = actual_profit + action["profit"]
            new_combo = actual_combo + [action["action"]]

            check_action(index + 1, new_cost, new_profit, new_combo)

    # lance une première fois la fonction check_action
    check_action(0, 0, 0, [])

    # Affiche les combinaisons théoriques,les combinaisons testées, les valeur du cout, du profit ainsi que la liste avec les meilleures action achetées
    print(f"Combinaisons théoriques : {total_possibilities}")
    print(f"Combinaisons testées : {count}")
    print(
        f"Le meilleur profit est de {round(best_profit, 2)}€, pour un cout de {best_cost}€"
    )
    print(f"Liste des actions: {best_combo}")


(brute_force(list_actions, max_budget))
