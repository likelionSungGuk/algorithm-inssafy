'''
5 7
WLLWWWL
LLLWLLL
LWLWLWW
LWLWLLL
WLLWLWW
'''
def bfs(r, c):
    global maxV, visited
    visited[r][c] = 1
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]
    Q = []
    Q.append([r, c])
    while len(Q):
        s = Q.pop(0)
        sr, sc = s[0], s[1]
        for i in range(4):
            nr = sr+dr[i]
            nc = sc+dc[i]
            if 0 <= nr < N and 0 <= nc < M and arr[nr][nc] == 'L' and visited[nr][nc] == 0:
                Q.append([nr, nc])
                visited[nr][nc] = visited[sr][sc] + 1
                if maxV <= visited[nr][nc]:
                    maxV = visited[nr][nc]
    visited = [[0] * M for _ in range(N)]
    return maxV

N, M = map(int, input().split())
arr = [list(map(str, input())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
result = []

maxV = 0
for i in range(N):
    for j in range(M):
        if arr[i][j] == 'L':
            ans = bfs(i, j)
        #visited = [[0] * M for _ in range(N)]
print(maxV-1)
