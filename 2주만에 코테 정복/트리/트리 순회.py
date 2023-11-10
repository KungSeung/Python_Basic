# 트리!

# Tree(나무) = Root + Seed
# 족보 ( 가족관계도 ) = 조상 + 자손

# 트리의 조건
# 1. 모든 노드들은 연결되어 있어야 한다
# 2. 사이클이 발생하면 안된다( 내 자식이 조상? 말 안됨 )

# 조상이 정해진 트리 : Rooted Tree
# 조상이 정해지지 않은 트리 : Tree -> 조상을 바꿔가면서 계산하라는 뜻!

# 전위순회 : 다른 노드로 출발하기 전에 나를 출력( 내 정보를 아래로 )
# 후위순회 : 자식 노드(왼쪽, 오른족 둘 다) 갔다와서 나를 출력( 자식 정보를 위로 )
# 중위순회 : 왼쪽 자식 노드 갔다가 오른쪽 자식 노드로 넘어가기 전에 나를 출력

# 기본적으로 2개의 자식노드를 왔다 갔다 할 수 있는 코드
# 자식 수가 많아지면 조금 for문이 붙는다

N = int(input())

graph = [[] for _ in range(130)]

for _ in range(N):
    a, b, c = map(str, input().split())
    # 아스키 코드로 변환
    a = ord(a)
    b = ord(b)
    c = ord(c)

    graph[a].append(b)
    graph[a].append(c)


def recur(node):
    if node == 46:  # '.' 일 경우 돌아오기
        return

    print(chr(node), end="")
    recur(graph[node][0])
    recur(graph[node][1])


recur(65)
