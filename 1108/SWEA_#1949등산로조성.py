from collections import deque
def dfs(r, c, cnt, depth):
    global maxC
    if maxC < cnt+1:
        maxC = cnt+1
    visited[r][c] = 1
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]
    for k in range(4):
        nr = r+dr[k]
        nc = c+dc[k]
        if 0 <= nr < N and 0 <= nc < N and visited[nr][nc] == 0:
            if MAP[nr][nc] < MAP[r][c]:
                dfs(nr, nc, cnt+1, depth)
            elif MAP[nr][nc] - depth < MAP[r][c]:
                before = MAP[nr][nc]
                MAP[nr][nc] = MAP[r][c] - 1
                dfs(nr, nc, cnt+1, 0)
                MAP[nr][nc] = before
    visited[r][c] = 0

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    MAP = [list(map(int, input().split())) for _ in range(N)]

    #최대값 찾기
    maxV = 0
    for i in range(N):
        for j in range(N):
            if MAP[i][j] > maxV:
                maxV = MAP[i][j]

    #최대값 모은 배열(최대 len 5)
    startPoint = deque()
    for i in range(N):
        for j in range(N):
            if MAP[i][j] == maxV:
                startPoint.append([i, j])
    maxC = 0
    visited = [[0] * N for _ in range(N)]
    while len(startPoint):
        r, c = startPoint.popleft()
        dfs(r, c, 0, K)

    print('#{} {}'.format(tc, maxC))
