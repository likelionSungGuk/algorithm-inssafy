"""
1
3
13 0 50
12 70 90
25 60 100
풀이
N-Queen
1. arr 완전탐색을 진행한다.
2. 첫행을 순차적으로 탐색하며 해당 열 배열에 값을 추가해준다.
3. 다음 행으로 넘어가서 다시 행을 탐색하는데, 이때 기존 열 배열에 없는 값만 찾는다.
4. 반복 하면서 그 배열을 지나가는 값들을 곱해준다.
"""
def dfs(r, c, ans):
    global visited
    if r == N-1:
        ans *= arr[r][c]
        return
    else:
        visited[r][c] = 1
        cols.append(c)
        ans *= arr[r][c]
        print(r, c, ans)
        nr = r+1
        Q = []
        for i in range(N):
            if i not in cols:
                Q.append(i)
        while len(Q):
            nc = Q.pop(0)
            if 0 <= nr < N and 0 <= nc < N and visited[nr][nc] == 0:
                dfs(nr, nc, ans)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr= [list(map(int, input().split())) for _ in range(N)]

    ans = 1
    result = []
    visited = [[0] * N for _ in range(N)]
    cols = []
    answer = dfs(0, 0, ans)
    result.append(answer)
    print(result)