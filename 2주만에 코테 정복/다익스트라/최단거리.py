# 가중치(=거리)가 양수일때 '최단거리'를 구한다

# 3가지 아이디어
# 1. 가중치 값으로 업데이트
# 2. 최단거리 구하기
# 3. 가중치가 낮은 순서대로 업데이트

from collections import deque

N, M = map(int, input().split())

start = int(input())

links = [[] for _ in range(N + 1)]
visited = [0 for _ in range(N + 1)]
# 1e9 : 1,000,000,000 을 뜻함 / distance
dist = [1e9 for _ in range(N + 1)]

for _ in range(M):
    A, B, C = map(int, input().split())
    links[A].append([B, C])

# bfs!

q = deque()
q.append(start)
visited[start] = 1
dist[start] = 0


# 얘는 너무 구리다
# 노드가 너무 많으면 매번 처음부터 끝까지 확인하고
# remove하고, append하는게 너무 느리다!
def shortest_finder():
    mini = 1e9
    idx = 0
    for i in range(1, N + 1):
        if dist[i] <= mini:
            idx = i
            mini = dist[i]
    return idx


while q:  # q 배열이 아무것도 없으면 false가 된다
    node = q.popleft()
    for nxt, weight in links[node]:
        # 1. 각각의 노드에 값을 업데이트
        # 2. 만약에 여러 경로가 있다면 min 비교!
        # 3. 시작점으로부터 거리를 봐서, 짧은 순서대로 거리를 탐색!
        dist[nxt] = min(dist[node] + weight, dist[nxt])
        q.append(nxt)
        visited[nxt] = 1

        idx = shortest_finder()

        if idx in q:
            q.remove(idx)
            q.appendleft(idx)
