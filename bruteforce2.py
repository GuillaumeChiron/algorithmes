from itertools import combinations
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
best_cost = 0
best_profit = 0
best_combo = []

n = len(list_actions)
count = 0
total_possibilities = 2**n

for i in range(n + 1):
    for combo in combinations(list_actions, i):
        count += 1

        total_cost = sum(action["cost"] for action in combo)
        if total_cost <= max_budget:
            total_profit = sum(action["profit"] for action in combo)
            if total_profit > best_profit:
                best_cost = total_cost
                best_profit = total_profit
                best_combo = [action["action"] for action in combo]

# Affiche les combinaisons théoriques,les combinaisons testées, les valeur du cout, du profit ainsi que la liste avec les meilleures action achetées
print(f"Combinaisons théoriques : {total_possibilities}")
print(f"Combinaisons testées : {count}")
print(
    f"Le meilleur profit est de {round(best_profit, 2)}€, pour un cout de {best_cost}€"
)
print(f"Liste des actions: {best_combo}")
