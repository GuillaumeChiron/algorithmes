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

for a in range(1, len(actions) + 1):
    for w in range(1, budget + 1):
        cost = actions[a - 1]["cost"]
        profit = actions[a - 1]["profit"]
        if cost <= budget:
            dp[a][w] += dp[a][w - 1] + profit

print(dp)
