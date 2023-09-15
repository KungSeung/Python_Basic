def solution(array):
    answer = 0
    
    num = 0
    maxNum = 0
    
    for i in array:
        if i == answer:
            continue
            
        for j in array:
            if i == j:
                num += 1

        if num == maxNum:
            answer = -1
            
        if num > maxNum:
            maxNum = num
            answer = i
            print(f'maxNum : {maxNum}, num : {num}, i : {i}')
            print(max(array))
        
        num = 0
               
    return answer


def solution(array):
    answer = 0
    # 원소 1개씩
    # set(집합) : 원소 중복 없음 / 불규칙적인 배열
    set_array = set(array)
    
    max_count = 0
    # 각 원소의 개수를 구하고 가장 많은 개수를 가지고 있는
    # 원소를 저장, 같으면 -1
    for i in set_array:
        count = array.count(i)
        if max_count < count:
            max_count = count
            answer = i
        elif max_count == count:
            answer = -1
    return answer