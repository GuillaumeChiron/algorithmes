# Retourne une liste d'actions la plus optimisée avec la technique du sac à dos
def knapsack(actions, budget):

    budget = budget
    n = len(actions)

    # Mise en place de la matrice (lignes: actions / colonnes: budget)
    matrice = [[0 for _ in range(budget + 1)] for _ in range(n + 1)]
    # Boucle qui itère sur les actions et qui stocke l'action dans une variable
    for a in range(1, n + 1):
        action = actions[a - 1]
        price = action["price"]
        profit = action["profit"]
        # Boucle qui itère sur le budget et ajoute le meilleur profit
        for b in range(1, budget + 1):
            # Cas où l'action est prise en compte
            if price <= b:
                matrice[a][b] = max(
                    matrice[a - 1][b],
                    matrice[a - 1][b - price] + profit,
                )
            # Cas où l'action n'est pas prise en compte
            else:
                matrice[a][b] = matrice[a - 1][b]

    best_profit = matrice[n][budget]
    best_cost = 0
    best_combo = []
    b = budget

    # Boucle qui renvoie la liste d'actions choisie ainsi que le meilleur coût et profit
    for i in range(n, 0, -1):
        if matrice[i][b] != matrice[i - 1][b]:
            action = actions[i - 1]
            best_combo.append(action["action"])
            best_cost += action["price"]
            b -= action["price"]

    return best_profit, best_cost, best_combo


# Retourne une liste d'actions la plus optimisée avec la technique du glouton
def greedy_actions(actions, budget_max):

    # Tri décroissant de la liste prise en paramètre de la fonction
    actions_sorted = sorted(actions, key=lambda x: x["profit"], reverse=True)

    total_cost = 0
    total_profit = 0
    actions_selected = []

    # Boucle qui ajoute la solution si elle respecte le budget
    for i in actions_sorted:
        if total_cost + i["price"] <= budget_max:
            total_cost += i["price"]
            total_profit += i["profit"]
            actions_selected.append(i["action"])

    return total_profit, total_cost, actions_selected
