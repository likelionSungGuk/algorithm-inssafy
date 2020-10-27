from itertools import combinations
from copy import deepcopy
# 벽세우기
def wall(k):
    new_arr = deepcopy(arr)
    for i in walls_comb[k]:
        new_arr[i[0]][i[1]] = 1
    return new_arr

# virus 살포
def bfs(new_arr, r, c):
    visited[r][c] = 1
    Q = []
    Q.append([r,c])
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]
    while len(Q):
        s = Q.pop(0)
        for i in range(4):
            nr = s[0] + dr[i]
            nc = s[1] + dc[i]
            if 0 <= nr < N and 0 <= nc < M:
                if new_arr[nr][nc] == 0 and visited[nr][nc] == 0:
                    new_arr[nr][nc] = 2
                    Q.append([nr, nc])
                elif new_arr[nr][nc] == 1:
                    continue
    return new_arr

#안전영역 구하기
def safe(new_arr):
    cnt = 0
    for i in range(N):
        for j in range(M):
            if new_arr[i][j] == 0:
                cnt += 1
    return cnt

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]
#바이러스 초기 위치 tc: 1 - [[0, 0], [1, 5]]
virus = []  #바이러스 위치
walls = []  #벽 설치 가능 위치
for i in range(N):
    for j in range(M):
        if arr[i][j] == 2:
            virus.append([i, j])
        elif arr[i][j] == 0:
            walls.append([i, j])
# 벽 3개 설치 조합
walls_comb = list(combinations(walls, 3)) 
# wall -> virus -> safety cnt
safety = []     #안전영역 크기 종합 리스트
walls_arr = []
# wall함수를 돌면서 return 되는 new_arr를 walls_arr에 append
for i in range(len(walls_comb)):
    temp = wall(i)
    walls_arr.append(temp)
# 벽을 세운 모든 경우의 수에서 virus bfs를 한 뒤 safety에 append
for i in range(len(walls_arr)):
    new_arr = walls_arr[i]
    for j in virus:
        result = bfs(new_arr, j[0], j[1])
        if j == virus[-1]:
            safe_cnt = safe(result)
            safety.append(safe_cnt)
print(max(safety))
