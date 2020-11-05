"""
5 4
1 0 1 0 0
1 0 0 0 0
1 0 1 0 1
1 0 0 1 0
"""
import sys; sys.setrecursionlimit(10**5)
def dfs(r, c):
    visited[r][c] = 1
    dr = [-1, 0, 1, 0, -1, 1, 1, -1]
    dc = [0, 1, 0, -1, 1, 1, -1, -1]
    for k in range(8):
        nr = r+dr[k]
        nc = c+dc[k]
        if 0 <= nr < M and 0 <= nc < N and visited[nr][nc] == 0:
            if arr[nr][nc] == 1:
                dfs(nr, nc)
while True:
    N, M = map(int, input().split())
    if N == 0 and M == 0: break
    else:
        arr = [list(map(int, input().split())) for _ in range(M)]
        visited = [[0]*N for _ in range(M)]
        # 섬 수
        cnt = 0

        for i in range(M):
            for j in range(N):
                if arr[i][j] == 1 and visited[i][j] == 0:
                    dfs(i,j)
                    cnt += 1
        print(cnt)
