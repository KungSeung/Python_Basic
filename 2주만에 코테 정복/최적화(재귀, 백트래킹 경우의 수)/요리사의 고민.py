# use : 재료를 아예 사용 안할 수 없다.
def recur(idx, dan, zzan, use):
    global answer

    # 종료 코드가 항상 위에 존재
    if idx == N:
        if use == 0:    # 아무 재료도 사용하지 않았다면
            return 
        result = abs(dan - zzan)
        answer = min(answer, result)
        return

    # 재료를 사용한다면
    recur(idx+1, dan+ingre[idx][0], zzan*ingre[idx][1], use + 1)

    # 재료를 사용하지 않는다면
    recur(idx+1, dan, zzan, use)



N = int(input())

ingre = [list(map(int, input().split())) for _ in range(N)]
answer = 99999999999999999999999
recur(0, 0, 1, 0)
print(answer)