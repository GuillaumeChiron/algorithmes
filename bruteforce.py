import csv

file = "csv/liste_d'actions.csv"
max_budget = 500


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

cost = 0
profit = 0


def action_check(cost, profit, list_actions):

    for i in list_actions:

        if (cost + i["cost"]) >= 500:
            return

        cost += i["cost"]
        profit += i["profit"]
        print(f"{cost} / {profit:.2f}")


action_check(cost, profit, list_actions)
