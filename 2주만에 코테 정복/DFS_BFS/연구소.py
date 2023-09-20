from collections import deque

N, M = map(int, input().split())

graph = [list(input().rstrip()) for _ in range(N)]

maxi = 0    # 최댓값
flag = 0    # 1의 갯수 / 최대 3개

# if 0을 만났을 때 1을 놓을 수 있다
# 1을 놓고 나머지 두곳에 1을 놓았을 때 
# 안전구역의 넓이를 체크한다

for x in range(N):
    for y in range(M):
        if graph[x][y] == 0:
            graph[x][y] = 1
            flag += 1
            for dx, dy in [[1,0], [-1,0], [0,1], [0,-1]]:
                if graph[x+dx][y+dy] == 0 and flag < 3:
                    graph[x+dx][y+dy] = 1
                    flag+=1

            # 2 채워넣기
            if flag == 3:
                for dx, dy in [[1,0], [-1,0], [0,1], [0,-1]]:
                        



# 1을 놓고 나면
# 2가 상하좌우 1칸씩 퍼져나간다

# 그리고 마지막에 0의 갯수를 체크해서 
# 영역의 크기를 구한다
# 최댓값을 반환한다
if graph[x][y] == 0:
    graph[x][y] = 1

