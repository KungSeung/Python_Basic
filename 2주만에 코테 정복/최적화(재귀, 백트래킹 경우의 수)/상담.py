# 가장 많이 or 적게 -> '완전탐색'

def recur(idx, price):

    global answer

    if idx == N:
        print(price)
        answer = max(answer, price)
        return

    # 퇴사 날짜 넘으면 무시
    if idx > N-1:
        return
    
    # 상담을 한다면
    recur(idx + interview[idx][0], price + interview[idx][1])

    # 상담을 안한다면
    recur(idx+1, price)

N = int(input())

interview = [list(map(int, input().split())) for _ in range(N)]

answer = 0
recur(0, 0)
print(answer)