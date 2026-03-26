from itertools import combinations
import csv

file = "csv/liste_d'actions.csv"


def find_column(fieldnames, candidates):
    for candidate in candidates:
        if candidate in fieldnames:
            return candidate
    raise KeyError(f"Unable to find expected column. Known columns: {fieldnames}")


def load_actions(csv_file):
    list_actions = []

    with open(csv_file, mode="r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        if reader.fieldnames is None:
            return list_actions

        fieldnames = reader.fieldnames
        action_col = find_column(fieldnames, ["Actions #"])
        cost_col = find_column(
            fieldnames,
            [
                "Coût par action (en euros)",
                "CoÃ»t par action (en euros)",
                "cout par action (en euros)",
            ],
        )
        profit_percent_col = find_column(
            fieldnames,
            [
                "Bénéfice (après 2 ans)",
                "BÃ©nÃ©fice (aprÃ¨s 2 ans)",
                "benefice (apres 2 ans)",
            ],
        )

        for l in reader:
            rendement = float(l[profit_percent_col].replace("%", ""))
            cost = float(l[cost_col])
            profit = cost * (rendement / 100)

            list_actions.append(
                {
                    "action": l[action_col],
                    "cost": cost,
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

print(f"Combinaisons theoriques : {total_possibilities}")
print(f"Combinaisons testees : {count}")
print(f"Le meilleur profit est de {round(best_profit, 2)} EUR, pour un cout de {best_cost} EUR")
print(f"Liste des actions: {best_combo}")
