# 최적화 방법 2가지

# 1. _find 최적화 = 경로 단축
# 2. _union 최적화 = Union by Rank(랭크를 두고 합친다)


def _union(A, B):  # 최대 높이를 확인해서 합쳐준다! 효과적으로!
    A = _find(A)
    B = _find(B)

    if A == B:
        return

    # 어차피 랭크(높이) 값이 크니까 더해줄 필요가 없다
    if rank[A] < rank[B]:
        par[A] = B
    elif rank[B] < rank[A]:
        par[B] = A
    else:
        par[A] = B  # 반대로 해도 상관없음! 반대로 하면 rank[A] += 1이 됨
        rank[B] += 1


def _find(A):
    # 스스로를 부모로 칭하고 있다 = 부모가 없다!
    if par[A] == A:
        return A
    else:
        # 값을 넣어준다 -> 경로 단축(고속도로를 낸다, 한번 계산 해놓고 다음에 계산 안함)
        par[A] = _find(par[A])
        return _find(par[A])


N, M = map(int, input().split())

rank = [0 for _ in range(N + 1)]  # 노드

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
