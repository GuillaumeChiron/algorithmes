import csv

file = "csv/dataset1.csv"


def load_actions(csv_file):
    list_actions = []
    count = 0

    with open(csv_file, mode="r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for l in reader:

            if float(l["price"]) > 0:

                count += 1
                list_actions.append(
                    {
                        "action": l["name"],
                        "cost": float(l["price"]),
                        "profit": float(l["profit"]),
                    }
                )

    return list_actions, count


list_actions, count = load_actions(file)
max_budget = 500

for i in list_actions:
    print(i)

print(count)
