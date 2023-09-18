# deque를 쓸려면 import 해줘야함
from collections import deque

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

# 양방향 원소 입력 가능
# q.pop() / q.popleft()
# q.append() / q.appendleft()
q = deque()

q.append(1)

while len(q) > 0:  # q가 0이 된다면 멈춤
    node = q.popleft()  # 1
    visited[node] = 1

    for nxt in graph[node]:
        if visited[nxt] == 1:
            continue
        q.append(nxt)

print(visited)
