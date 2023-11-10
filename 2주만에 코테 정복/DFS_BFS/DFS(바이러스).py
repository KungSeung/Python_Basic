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


# 재귀에서 for문을 돌 때 굳이 return이 없어도 다시
# 함수에 들어가는 거 아니면 return을 안해줘도 된다
# 함수는 return문이 없으면 아무 결과를 반환하지 않기 때문에
# none값을 반환하고 끝이 난다!
# 즉 return문이 없어도 함수는 마지막 줄에 가면 끝이 난다는 것~
def recur(node):
    visited[node] = 1

    for nxt in graph[node]:
        if visited[nxt] == 1:
            continue
        recur(nxt)


recur(1)

print(sum(visited) - 1)
