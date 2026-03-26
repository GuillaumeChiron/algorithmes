def knapsack(actions, budget):

    budget = budget
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

    return best_profit, best_cost, best_combo


def greedy_actions(actions, budget_max):

    actions_sorted = sorted(actions, key=lambda x: x["rendement"], reverse=True)

    total_cost = 0
    total_profit = 0
    actions_selected = []

    for i in actions_sorted:
        if total_cost + i["price"] <= budget_max:
            total_cost += i["price"]
            total_profit += i["profit"]
            actions_selected.append(i["action"])

    return total_profit, total_cost, actions_selected
