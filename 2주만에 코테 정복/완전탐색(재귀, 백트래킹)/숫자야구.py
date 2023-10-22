# 어렵게 생각하지 말고
# A라는 친구가 생각할 수 있는 정답의 범위를 모조리 때려박아서
# 조건에 맞다면 카운트를 올리겠다!!

# 세자리 수  100 ~ 999
# 이게 4가지 조건에 통과한다면 카운트 해준다

# 재귀는 1000번 정도 돌면 멈추기 때문에
# 의도적으로 이 값을 늘려준다
import sys

sys.setrecursionlimit(99999999)

def checker(idx, number):
    _number = hint[idx][0]
    _strike = hint[idx][1]
    _ball = hint[idx][2]

    strike = 0
    ball = 0 

    _A = _number // 100
    _B = (number - (_A * 100)) // 10
    _C = _number % 10

    A = number // 100
    B = (number - (A * 100)) // 10
    C = number % 10

    if A == 0 or B == 0 or C == 0:
        return False
    
    if A == B or B == C or A == C:
        return False
    
    if A == _A:
        strike +=1
    if B == _B:
        strike +=1
    if C == _C:
        strike +=1

    if A ==  _B or A == _C:
        ball +=1
    if B ==  _A or B == _C:
        ball +=1
    if  C == _B or C == _A:
        ball +=1

    if strike == _strike and ball == _ball:
        return True

    return False


def recur(hint_idx, number):

    global answer

    if hint_idx == 4:
        answer += 1
        print(number)
        recur(0, number+1)
        return

    # 만약에 힌트에 통과했다면
    # 스트라이크 카운트랑 볼 카운트가 동일하다면, 다음 hint로 넘어간다
    if checker(hint_idx, number):
        recur(hint_idx+1, number)
    # 만약에 힌트에 통과하지 않았다면
    # number 값을 1을 올려준다 and hint를 처음으로 초기화
    else:
        recur(0, number+1)


N = int(input())
hint = [list(map(int, input().split())) for _ in range(N)]
answer = 0
recur(0, 100)
print(answer)