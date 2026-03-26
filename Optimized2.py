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


def greedy_actions(list_actions, budget_max):

    list_actions_sorted = sorted(
        list_actions, key=lambda x: x["rendement"], reverse=True
    )

    total_cost = 0
    total_profit = 0
    actions_selected = []

    for i in list_actions_sorted:
        if total_cost + i["price"] <= budget_max:
            total_cost += i["price"]
            total_profit += i["profit"]
            actions_selected.append(i["action"])

    return total_profit, total_cost, actions_selected


def display_result(best_profit, best_cost, best_combo):
    print(
        f"L'achat des {len(best_combo)} actions suivantes:\n"
        f"{best_combo}\n"
        f"pour un cout total de {round(best_cost, 2)} EUR a genere {round(best_profit, 2)} EUR de profit"
    )


budget = 500
list_actions = load_actions(file)
total_profit, total_cost, actions_selected = greedy_actions(list_actions, budget)
display_result(total_profit, total_cost, actions_selected)
