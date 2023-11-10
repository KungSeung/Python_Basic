N = int(input())
arr1 = sorted(list(map(int, input().split())))  # 1 ~ 100

M = int(input())
arr2 = sorted(list(map(int, input().split())))

for number in arr2:
    s = 0
    e = N - 1
    flag = False

    while s <= e:  # 교차되지 않았다면
        mid = (s + e) // 2

        # 업인가요? 다운인가요? 정답인가요?
        if arr1[mid] == number:
            flag = True
            break
        elif arr1[mid] > number:
            e = mid - 1
        elif arr1[mid] < number:
            s = mid + 1

    if flag:
        print(1)
    else:
        print(0)
