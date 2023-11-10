# 다이나믹 프로그래밍( 바텀업 DP ) 문제 중에서도
# 아이큐테스트에 해당 / 아이디어를 가지고 있으면 쉽다
# 하지만 처음에 아이디어를 도달하지 못하면 너무 어렵다

# LIS : Longest Increasing Subsequence
# LCS : Longest Common Subsequence

N = int(input())
arr = list(map(int, input().split()))

dp = [1 for _ in range(N)]

for i in range(N):
    for j in range(i):  # 내 기준 왼쪽에 있는 숫자까지만 확인
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))
