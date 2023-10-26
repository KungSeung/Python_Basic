N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
dp = [[0 for _ in range(len(graph))] for _ in range(N)]

for idx in range(N):
    for RGB in range(3):
        if RGB == 0:  # RED
            dp[idx][RGB] = min(dp[idx - 1][1], dp[idx - 1][2]) + graph[idx][RGB]
        if RGB == 1:  # GREEN
            dp[idx][RGB] = min(dp[idx - 1][0], dp[idx - 1][2]) + graph[idx][RGB]
        if RGB == 2:  # BLUE
            dp[idx][RGB] = min(dp[idx - 1][0], dp[idx - 1][1]) + graph[idx][RGB]
