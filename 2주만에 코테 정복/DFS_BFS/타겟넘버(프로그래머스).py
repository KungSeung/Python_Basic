from collections import deque


def soluton(numbers, target):
    answer = 0
    queue = deque()
    n = len(numbers)
    queue.append([numbers[0], 0])
    queue.append([-1 * numbers[0], 0])
    while queue:
        print(queue)
        temp, idx = queue.popleft()
        idx += 1
        if idx < n:
            queue.append([temp + numbers[idx], idx])
            queue.append([temp - numbers[idx], idx])
        else:
            if temp == target:
                answer += 1

    return answer


print(soluton([4, 1, 2, 1], 4))
