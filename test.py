actions = [
    {"name": "A", "cost": 100, "profit": 20},
    {"name": "B", "cost": 180, "profit": 30},
    {"name": "C", "cost": 250, "profit": 50},
    {"name": "D", "cost": 120, "profit": 24},
    {"name": "E", "cost": 200, "profit": 35},
]

budget = 500
n = len(actions)

dp = [[0 for _ in range(budget + 1)] for _ in range(n + 1)]

for a in range(1, n + 1):
    action = actions[a - 1]
    price = action["cost"]
    profit = action["profit"]
    print(action["name"])

    for w in range(budget + 1):
        if price <= w:
            dp[a][w] = max(dp[a - 1][w], dp[a - 1][w - price] + profit)
        else:
            dp[a][w] = dp[a - 1][w]

print(dp[n][budget])
