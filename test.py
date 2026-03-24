dp = [[0 for _ in range(6)] for _ in range(3)]

print(dp)

for i in range(len(dp)):
    for j in range(len(dp[i])):
        dp[i][j] = j

print(dp)
