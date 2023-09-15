# 왜인지 테스트케이스 1,9번이 통과가 안됨
# 무언가가 틀렸다
def solution(lines):
    answer = 0
    
    # 문제는 선분이 딱 '3'개라는 것이다
    newList = []
    overLine = []
    for i in range(0, len(lines)):
        arr = [j for j in range(lines[i][0], lines[i][1] + 1)]
        newList.append(arr)
    
    # 교집합 찾기 : intersection -> &
    # add 1개의 원소만 추가
    # update 여러개 원소 추가
    # for문 쓴 이유는 선분이 더 많은 줄 알았음
    for i in range(0, len(lines)):
        for j in range(i+1, len(lines)):
            s1 = set(newList[i])
            s2 = set(newList[j])
            if len(s1 & s2) > 1:
                overLine.append(s1 & s2)
            else:
                s1 = set()
                overLine.append(s1)
    
    print(overLine)
    length = len(overLine[0] | overLine[1] | overLine[2])
  
    # 겹치는 부분 없음
    if length == 0:
        return 0
    else:
        return length - 1 
    

# 두번째 풀이
def solution(lines):
    # 범위가 -100 ~ 100 이므로 0 ~ 200으로 바꿔준다
    table = [set([]) for _ in range(200)]

    # enumerate() : 인덱스와 원소로 이루어진 tuple 반환
    for index, line in enumerate(lines):
        x1, x2 = line
        for x in range(x1, x2):
            table[x + 100].add(index)
    
    answer = 0
    for line in table:
        if len(line) > 1:
            answer += 1
        
    return answer