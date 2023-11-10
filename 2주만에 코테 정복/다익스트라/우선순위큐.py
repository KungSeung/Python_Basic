# 우선순위 큐
# 그렇다면 얘는 뭐냐?
# 부모보다 작은 자식이 없게 정렬을 함( 이진 트리 )
import heapq

N, M = map(int, input().split())

start = int(input())

links = [[] for _ in range(N + 1)]
# 1e9 : 1,000,000,000 을 뜻함 / distance
dist = [1e9 for _ in range(N + 1)]

for _ in range(M):
    A, B, C = map(int, input().split())
    links[A].append([B, C])

q = []
heapq.heappush(q, [0, start])
dist[start] = 0

while q:  # q 배열이 아무것도 없으면 false가 된다
    # 우선순위 큐를 이용해서, 거리를 보고 정렬할거다
    node = heapq.heappop(q)
    for nxt, weight in links[node]:
        # 1. 각각의 노드에 값을 업데이트
        # 2. 만약에 여러 경로가 있다면 min 비교!
        # 3. 시작점으로부터 거리를 봐서, 짧은 순서대로 거리를 탐색!
        if dist[node] + weight < dist[nxt]:
            dist[nxt] = min(dist[node] + weight, dist[nxt])
            heapq.heappush(q, [dist[nxt], nxt])


# BFS > 가중치
# 1. 노드에 거리를 업데이트
# 2. 여러 경로 최솟값 비교
# 3. 거리가 짧은 순서대로 업데이트
# 우선순위큐를 써야 제대로된 시간안에 수행이 된다
# 우선순위큐는 어떤 원리인가?
# 우선순위큐는 어떻게 구현해야 하는가?
