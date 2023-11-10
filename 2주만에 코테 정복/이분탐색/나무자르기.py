N, M = map(int, input().split())
forest = list(map(int, input().split()))

s = 1
e = max(forest)

while s <= e:  # 교차되기 전까지!
    mid = (s + e) // 2

    # 얼마나 나무를 채취했는가?
    wood = 0
    for tree in forest:
        if tree >= mid:
            wood += tree - mid

    # 업인가요? 다운인가요?
    if wood >= M:  # 최소를 만족함
        s = mid + 1
    else:
        e = mid - 1

print(e)
