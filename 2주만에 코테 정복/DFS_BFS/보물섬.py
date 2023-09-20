from collections import deque

Y, X = map(int, input().split())

# strip : 문자 양쪽 공백 제거
# rstrip : 문자 오른쪽의 공백 제거
# lstrip : 문자 왼쪽의 공백 제거
graph = [list(input().rstrip()) for _ in range(Y)]

# 처음부터 끝까지 다 돌면서
# 가장 먼거리가 어디인지 계속 업데이트 하는 방식
# 완전탐색적 사고인데
# L을 만났을 땐 BFS를 돌린다

maxi = 0

for y in range(Y):
    for x in range(X):
        if graph[y][x] == "L":
            visited = [[0 for _ in range(X)] for _ in range(Y)]
            dist = [[0 for _ in range(X)] for _ in range(Y)]

            # BFS
            q = deque()
            q.append([y, x])  # 시작점
            visited[y][x] = 1

            while q:
                ey, ex = q.popleft()

                # 4 방향 탐색 : 2차원 DP
                for dy, dx in [[0, 1], [1, 0], [-1, 0], [0, -1]]:
                    ny, nx = ey + dy, ex + dx
                    if 0 <= ny < Y and 0 <= nx < X:
                        if graph[ny][nx] == "L":
                            visited[ny][nx] = 1
                            dist[ny][nx] = dist[ey][ex] + 1
                            maxi = max(maxi, dist[ny][nx])
                            q.append[ny][nx]
