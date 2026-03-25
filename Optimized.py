import csv

file = "csv/dataset1.csv"


def load_actions(csv_file):
    list_actions = []

    with open(csv_file, mode="r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for l in reader:

            if float(l["price"]) > 0:

                profit = float(l["profit"])
                price = int(float(l["price"]) * 100)
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


def knapsack(list, budget, n):

    matrice = [[0 for _ in range(budget + 1)] for _ in range(n + 1)]

    for a in range(1, n + 1):

        action = list[a - 1]
        price = int((action["price"]))
        profit = action["profit"]

        for w in range(1, budget + 1):

            if price <= w:
                matrice[a][w] = max(
                    matrice[a - 1][w], matrice[a - 1][w - price] + profit
                )
            else:
                matrice[a][w] = matrice[a - 1][w]

    best_profit = matrice[n][budget]
    best_cost = 0
    best_combo = []
    w = budget

    for i in range(n, 0, -1):
        if matrice[i][w] != matrice[i - 1][w]:
            action = actions_sorted[i - 1]
            best_combo.append(action["action"])
            best_cost += action["price"]
            w -= action["price"]

    best_cost = best_cost / 100

    return best_profit, best_cost, best_combo


list_actions = load_actions(file)
actions_sorted = sorted(list_actions, key=lambda x: x["rendement"], reverse=True)
budget = 50000
n = len(actions_sorted)
best_profit, best_cost, best_combo = knapsack(actions_sorted, budget, n)

print(
    f"L'achat des {len(best_combo)} actions suivantes:\n {best_combo}\n pour un coût total de {best_cost}€ à générer {round(best_profit, 2)}€ de profit"
)
