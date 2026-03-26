import csv

file = "csv/dataset1.csv"


def load_actions(csv_file):
    list_actions = []

    with open(csv_file, mode="r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for l in reader:

            if float(l["price"]) > 0:

                profit = float(l["profit"])
                price = float(l["price"])
                action = l["name"]
                rendement = float((profit / price) * 100)

                list_actions.append(
                    {
                        "action": action,
                        "price": price,
                        "profit": profit,
                        "rendement": rendement,
                    }
                )

    return list_actions


list_actions = load_actions(file)

actions_sorted = sorted(list_actions, key=lambda x: x["rendement"], reverse=True)

print(len(actions_sorted))

budget = 500
n = len(actions_sorted)

test = "Ceci est un test"
