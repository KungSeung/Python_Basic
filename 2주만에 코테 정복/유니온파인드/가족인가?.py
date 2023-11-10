# 두 노드, 두 숫자, 두 무언가

# => 같은 집합 안에 있나요??

# union / find 할 것이다

# 핵심 : 가장 위에 있는 조상을 파악해서
# 이 친구들이 연결되어 있는가? 를 아는게 중요하다


def _union(A, B):
    par[B] = A


def _find(A):
    # 스스로를 부모로 칭하고 있다 = 부모가 없다!
    if par[A] == A:
        return A
    else:
        return _find(par[A])


N, M = map(int, input().split())

# [0, 1, ... , 7]
par = [i for i in range(N + 1)]

for _ in range(M):
    x, A, B = map(int, input().split())
    if x == 0:
        _union(A, B)

    else:
        # A의 조상과 B의 조상이 같은지
        if _find(A) == _find(B):
            print("YES")
        else:
            print("NO")
