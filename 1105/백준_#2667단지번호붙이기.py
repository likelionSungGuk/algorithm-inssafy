def dfs(r, c):
    global home_cnt, cnt
    visited[r][c] = 1
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]
    for k in range(4):
        nr = r+dr[k]
        nc = c+dc[k]
        if 0 <= nr < N and 0 <= nc < N and visited[nr][nc] == 0:
            if arr[nr][nc] == 1:
                home_cnt += 1
                # arr[nr][nc] = 0
                dfs(nr, nc)

N = int(input())
arr = [list(map(int, input())) for _ in range(N)]
visited = [[0]*N for _ in range(N)]
# 단지 수
cnt = 0
home_cnt = 1
# 단지 내 가구 수 배열
result = []

for i in range(N):
    for j in range(N):
        if arr[i][j] == 1 and visited[i][j] == 0:
            dfs(i,j)
            cnt += 1
            result.append(home_cnt)
            home_cnt = 1
result.sort()

print(cnt)
for i in range(len(result)):
    print(result[i])