def find_minimum_weights(target_range):
    weights = [1, 3, 6, 10, 15]

    dp = [[float('inf')] * (target_range + 1) for _ in range(len(weights))]

    for i in range(len(weights)):
        dp[i][0] = 0

    for i in range(len(weights)):
        for j in range(1, target_range + 1):
            # Nếu không sử dụng quả cân thứ i.
            dp[i][j] = dp[i - 1][j]

            # Nếu sử dụng quả cân thứ i.
            if j >= weights[i]:
                dp[i][j] = min(dp[i][j], dp[i][j - weights[i]] + 1)

    # In kết quả.
    result_weights = []
    i, j = len(weights) - 1, target_range
    while i >= 0 and j > 0:
        if i > 0 and dp[i][j] == dp[i - 1][j]:
            i -= 1
        else:
            result_weights.append(weights[i])
            j -= weights[i]

    return len(result_weights)


s = []
for i in range(0, 400):
    result = find_minimum_weights(i)
    s.append(result)
print(', '.join(map(str, s)))
