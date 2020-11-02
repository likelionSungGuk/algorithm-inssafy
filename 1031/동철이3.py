"""
1
3
13 0 50
12 70 90
25 60 100
"""
def percent(n):
    return int(n)/100
def dfs(r, ans):
    global n, answer
    if ans <= answer:return
    if r == N:
        answer = max(answer, ans)
        return
    for i in range(N):
        if visited[i] == 0:
            visited[i] = 1
            dfs(r+1, ans*arr[r][i])
            visited[i] = 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(percent, input().split())) for _ in range(N)]
    ans = 1
    answer = 0
    visited = [0]*N
    dfs(0, 1)
    print('#{} {:.6f}'.format(tc, answer*100))
