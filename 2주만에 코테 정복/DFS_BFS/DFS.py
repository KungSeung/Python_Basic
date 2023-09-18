N = int(input())
M = int(input())

graph = [[] for _ in range(N + 1)]
# N+1을 한 이유 : 표현하기 쉽게 하기위해서
# graph[1] = [2, 5] -> 첫번째 노드와 링크되어있는 정점들
# graph[2] = [1, 3, 5] -> 두번째 노드와 링크되어있는 정점들

visited = [0 for _ in range(N + 1)]
# visited[1] = 0 / 방문 x
# visited[1] = 1 / 방문 o

# 정점 연결
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


# DFS 재귀함수
# node 1로 시작
# graph[1]에 있는 원소들(nxt)를 가져옴
# recur 함수로 재귀(반복)
def recur(node):
    visited[node] = 1

    for nxt in graph[node]:
        if visited[nxt] == 1:
            continue
        recur(nxt)


recur(1)

print(sum(visited) - 1)
