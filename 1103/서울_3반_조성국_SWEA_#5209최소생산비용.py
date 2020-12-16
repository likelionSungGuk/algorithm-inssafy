def find(k, ans):
    global minV
    if k == N:
        minV = min(ans, minV)
        return
    if ans > minV:  #백트래킹  - 더 볼 것도 없음
        return
    for i in range(N):
        if visited[i] == 0:
            visited[i] = 1
            find(k+1, ans+arr[k][i])
            visited[i] = 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    minV = 999999
    visited = [0] * N
    find(0, ans)
    print('#{} {}'.format(tc, minV))
