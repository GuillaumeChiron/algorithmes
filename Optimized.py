import csv

file = "csv/dataset1.csv"
file2 = "csv/dataset2.csv"


def load_actions(csv_file):
    list_actions = []

    with open(csv_file, mode="r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for l in reader:
            if float(l["price"]) > 0:
                profit = float(l["profit"])
                price = int(float(l["price"]) * 100)
                action = l["name"]
                rendement = (profit / price) * 100

                list_actions.append(
                    {
                        "action": action,
                        "price": price,
                        "profit": profit,
                        "rendement": rendement,
                    }
                )

    return list_actions


def knapsack(actions, budget):

    n = len(actions)
    matrice = [[0 for _ in range(budget + 1)] for _ in range(n + 1)]

    for a in range(1, n + 1):
        action = actions[a - 1]
        price = action["price"]
        profit = action["profit"]

        for b in range(1, budget + 1):
            if price <= b:
                matrice[a][b] = max(
                    matrice[a - 1][b],
                    matrice[a - 1][b - price] + profit,
                )
            else:
                matrice[a][b] = matrice[a - 1][b]

    best_profit = matrice[n][budget]
    best_cost = 0
    best_combo = []
    b = budget

    for i in range(n, 0, -1):
        if matrice[i][b] != matrice[i - 1][b]:
            action = actions[i - 1]
            best_combo.append(action["action"])
            best_cost += action["price"]
            b -= action["price"]

    return best_profit, best_cost / 100, best_combo


def display_result(best_profit, best_cost, best_combo):
    print(
        f"L'achat des {len(best_combo)} actions suivantes:\n"
        f"{best_combo}\n"
        f"pour un cout total de {best_cost} EUR a genere {round(best_profit, 2)} EUR de profit"
    )


list_actions = load_actions(file)
list_actions2 = load_actions(file2)


budget = 50000

best_profit, best_cost, best_combo = knapsack(list_actions, budget)
display_result(best_profit, best_cost, best_combo)

best_profit2, best_cost2, best_combo2 = knapsack(list_actions2, budget)
display_result(best_profit2, best_cost2, best_combo2)
