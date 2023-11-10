# 단순 연결이면 양방향으로 연결되어 있게 코드 변경 필요!

N = int(input())

graph = [[] for _ in range(N + 1)]
par = [0 for _ in range(N + 1)]  # 부모 노드가 누군지
child_num = [0 for _ in range(N + 1)]  # 자식 노드의 갯수

for _ in range(N - 1):
    a, b = map(int, input().split())

    graph[a].append(b)
    graph[b].append(a)


def recur(node, prv):
    par[node] = prv  # 윗 정보를 아래로(전위순회)
    print(par)

    for nxt in graph[node]:
        if nxt == prv:  # 역주행 방지 코드
            continue
        recur(nxt, node)

    child_num[prv] += 1  # 아랫 정보를 위로(후위순회)


# 출발지점 : root = 1, prv(이전 노드) = 0
recur(1, 0)

# print(par)
