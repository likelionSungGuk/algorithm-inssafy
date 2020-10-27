"""
7 5
.......
.o...*.
.......
.*...*.
.......
"""
"""
풀이
1. 먼지들간의 거리가 가까운 순서대로 순회
2. 중간에 가구(X)가 없는 것을 우선적으로 순회
"""
N, M = map(int, input().split())
floor = [list(input()) for _ in range(M)]

#로봇청소기 시작 위치, 더러운 것의 위치 찾기
start = []
dirts = []
for i in range(M):
    for j in range(N):
        if floor[i][j] == 'o':
            start.append([i, j])
        elif floor[i][j] == '*':
            dirts.append([i, j])


