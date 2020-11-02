def check(n, pos):
    global result
    if pos <= result:
        return
    if n == N:
        if pos > result:
            result = pos
        return
    for i in range(N):
        if visited[i] == 0:
            visited[i] = 1
            check(n + 1, pos * possibility[n][i] / 100)
            visited[i] = 0


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    possibility = [list(map(int, input().split())) for _ in range(N)]
    result = 0
    visited = [0] * N
    for i in range(N):
        visited[i] = 1
        check(1, possibility[0][i] / 100)
        visited[i] = 0
    result = round(result * 100, 6)

    print('#{}'.format(tc), end=' ')
    print('{:.6f}'.format(result))