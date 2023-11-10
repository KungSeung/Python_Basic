# 가능성을 지워주는 방법

n = int(input())

arr = sorted(list(map(int, input().split())))

x = int(input())

# 두 개의 마우스 커서, 포인터
s = 0
e = n - 1

# 정답
cnt = 0

while s < e:
    if arr[s] + arr[e] == x:
        cnt += 1

    if arr[s] + arr[e] >= x:
        e -= 1
    else:
        s += 1


print(cnt)
