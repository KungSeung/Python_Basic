answer = 0


def DFS(L, s, ability, check):
    global answer
    n = len(ability)  # 학생 수
    m = len(ability[0])  # 종목 개수

    if L == m:
        print(L, s)
        answer = max(answer, s)  # 능력치 합의 최댓값을 구함
    else:
        for i in range(n):
            if check[i] == 0:
                check[i] = 1
                print(L + 1, "[{}][{}]".format(i, L), s)
                DFS(L + 1, s + ability[i][L], ability, check)
                check[i] = 0


def solution(ability):
    global answer
    check = [0] * len(ability)
    DFS(0, 0, ability, check)
    # Level, sum, ability, check
    # L : level (고를 수 있는 학생 수 중 몇 명째 선택한 것인지), sum : 능력치의 합

    return answer


ability = [[40, 10, 10], [20, 5, 0], [30, 30, 30], [70, 0, 70], [100, 100, 100]]

solution(ability)
