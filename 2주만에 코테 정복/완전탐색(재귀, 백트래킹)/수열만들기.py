# 자유도 : 재귀함수 > for 문


def recur(number):
    if number == M:
        print(arr)
        return

    for i in range(1, N + 1):  # 1부터 N까지 돌림
        #        if i in arr: / 중복없이
        #            continue
        arr.append(i)
        print(arr)
        recur(number + 1)
        arr.pop()
        print(arr)


N, M = map(int, input().split())
arr = []
recur(0)
