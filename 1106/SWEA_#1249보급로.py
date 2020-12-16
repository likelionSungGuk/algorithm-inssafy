'''
1
4
0100
1110
1011
1010
'''
from collections import deque
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    MAP = [list(map(int, input())) for _ in range(N)]   #지도
    dist = [[99999999]*N for _ in range(N)]


    #시작점
    Q = deque()
    Q.append((0, 0))
    dist[0][0] = 0

    while Q:
        r, c = Q.popleft()

        for k in range(4):
            nr = r+dr[k]
            nc = c+dc[k]
            if 0 <= nr < N and 0 <= nc < N:
                if dist[nr][nc] > dist[r][c]+MAP[nr][nc]:
                    dist[nr][nc] = dist[r][c]+MAP[nr][nc]
                    Q.append((nr, nc))

    print('#{} {}'.format(tc, dist[N-1][N-1]))
