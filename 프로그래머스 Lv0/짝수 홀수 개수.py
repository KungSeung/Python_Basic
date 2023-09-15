def solution(num_list):
    answer = []
    evenNum = 0
    oddNum = 0
    for i in num_list:
        if i % 2 == 0:
            evenNum += 1
        else:
            oddNum += 1
    answer = [evenNum, oddNum]
    return answer