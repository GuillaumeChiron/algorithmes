dp = [[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]

print(dp)

for i in range(len(dp)):
    for j in range(len(dp[i])):
        dp[i][j] = j

print(dp)
