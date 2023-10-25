# 가장 많이 or 적게 -> '완전탐색'


# 마지막부터 계산을 한다
# 0이 return 된 후에 price를 더해주는 방식
def recur(idx):
    global answer

    if idx == N - 1:
        return 0

    # 퇴사 날짜 넘으면 무시
    if idx > N - 1:
        return -999999999

    # 이미 저장되었다면
    if dp[idx] != -1:
        return dp[idx]

    # 상담을 받는 날에 대하여 max값을 넣어놓는다, 왜냐하면 상담받는게 무조건 이득
    dp[idx] = max(recur(idx + interview[idx][0]) + interview[idx][1], recur(idx + 1))

    return dp[idx]


N = int(input())

interview = [list(map(int, input().split())) for _ in range(N)]

dp = [-1 for _ in range(N + 1)]

answer = 0


recur(0)
print(dp)
print(answer)
