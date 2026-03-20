import csv
from itertools import combinations

file = "csv/dataset1.csv"


def load_actions(csv_file):
    list_actions = []
    count = 0

    with open(csv_file, mode="r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for l in reader:

            if float(l["price"]) > 0:

                profit = float(l["profit"])
                price = float(l["price"])

                list_actions.append(
                    {
                        "action": l["name"],
                        "price": price,
                        "profit": profit,
                        "rendement": float((price * profit) / 100),
                    }
                )

    return list_actions


list_actions = load_actions(file)
max_budget = 500
cost = 0

actions_sorted = sorted(list_actions, key=lambda x: x["rendement"], reverse=True)

for i in actions_sorted:
    print(i["rendement"])
