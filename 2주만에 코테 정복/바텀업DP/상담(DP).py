# 가장 많이 or 적게 -> '완전탐색'

# DP 문제의 2가지 유형
# 1. 완전탐색적 사고, 주문이 가능한 DP
# 2. 손코딩! 아이큐 테스트에 가까운 문제 -> 써봐야만 규칙을 알 수 있음


# 점화식 -> for 반복문으로 바꾼다

# 문제1 : 상담
N = int(input())
interview = [list(map(int, input().split())) for _ in range(N + 1)]
dp = [0 for _ in range(N + 1)]


# 역순(바텀업이라서?) : [::-1]
for idx in range(N + 1)[::-1]:
    if idx == interview[idx][0] + N:
        dp[idx] = dp[idx + 1]
    else:
        dp[idx] = max(dp[idx + interview[idx][0]] + interview[idx][1], dp[idx + 1])


print(dp)

# 문제2 : 냅색

N, B = map(int, input().split())

items = [list(map(int, input().split())) for _ in range(N)]

for idx in range(N + 1):
    for weight in range(B + 1):
        if weight < B:
            dp[idx][weight] = dp[idx - 1][weight]
        else:
            dp[idx][weight] = max(
                dp[idx - 1, weight - items[idx][0]] + items[idx][1], dp[idx, weight]
            )
