def recur(idx, weight, value):
    global answer

    if weight > B:
        return

    if idx == N:
        answer = max(answer, value)
        return

    # 물건을 넣은 경우
    recur(idx + 1, weight + items[idx][0], value + items[idx][1])

    # 물건을 안 넣은 경우
    recur(idx, weight, value)


N, B = map(int, input().split())

items = [list(map(int, input().split())) for _ in range(N)]

answer = 0
recur(0, 0, 0)
