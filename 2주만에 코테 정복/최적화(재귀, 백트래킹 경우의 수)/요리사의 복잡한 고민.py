def recur(idx, A, B, C, D, E, use):
    global spendMoney

    if idx == N:
        # 재료 사용 x
        if use == 0:
            return
        # 재료 최소 1개 사용 & 모든 영양소 충족
        if a <= A and b <= B and c <= C and d <=D:
            print(A, B, C, D, E)
            spendMoney = min(spendMoney, E)
        return
    
    # 재료를 사용한 경우
    recur(idx + 1, A+nut[idx][0], B+nut[idx][1], C+nut[idx][2], D+nut[idx][3], E+nut[idx][4], use+1)
    
    # 재료를 사용하지 않은 경우
    recur(idx + 1, A, B, C, D, E, use)

N = int(input())
a, b, c, d = list(map(int, input().split()))
nut = [list(map(int, input().split())) for _ in range(N)]

spendMoney = 1000000
recur(1, 0, 0, 0, 0, 0, 0)
print(spendMoney)