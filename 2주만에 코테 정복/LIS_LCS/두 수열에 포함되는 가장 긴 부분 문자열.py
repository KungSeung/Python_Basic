# 잘 모르겠으면 완전탐색!
# 완전탐색을 최적화 시키는 과정에서 답은 무조건 나오게 되어있다

# 끝에 문자열이 같다면
# 앞에 문자열과 상관없이 +1이 된다
M = list(str(input()))
N = list(str(input()))

dp = [[0 for _ in range(len(N) + 1)] for _ in range(len(M) + 1)]

for i in range(1, len(M) + 1):
    for j in range(1, len(N) + 1):
        if M[i - 1] == N[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])

print(dp)
