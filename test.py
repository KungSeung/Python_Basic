# import itertools

# N = int(input())

# ans = []
# for i in range(N):
#     M = int(input())
#     arr = list(map(int, input().split()))

#     arrSum = 0
#     for j in range(1, len(arr) + 1):
#         numList = list(itertools.combinations(arr, j))

#         for k in numList:
#             arrSum += sum(k) / j

#     ans.append(arrSum / (2 ** len(arr) - 1))

# for i, num in enumerate(ans):
#     formatted_number = "{:.20f}".format(num).rstrip("0").rstrip(".")
#     print("#{0} {1}".format(i + 1, formatted_number))

N = int(input())
ansArr = []

for _ in range(N):
    lenArr = int(input())
    arr = list(map(int, input().split()))

    # 일단 max 값을 넣어놔 그리고 그 날 지나면 arr 쪼개서 갱신
    maxPrice = max(arr)
    ans = 0
    while len(arr) > 0:
        for i in range(len(arr)):
            if arr[i] == maxPrice:
                for j in range(i):
                    ans += arr[j]
                arr = arr[i + 1 :]
                break

    ansArr.append(ans)
    ans = 0

for i, ans in enumerate(ansArr):
    print("#{0} {1}".format(i, ans))
