"""
1
3
13 0 50
12 70 90
25 60 100
"""

def dfs(r, c, ans):
    global stack, visited, result
    if r == N-1:
        last = 0
        for i in range(len(visited)):
            if visited[i] == 0:
                ans *= arr[r][c]
                last = i
        visited[last] = 0
        print(c, ans)
        result.append(ans)
        ans = ans // arr[r][c]
        return
    else:
        ans *= arr[r][c]
        visited[c] = 1
        for i in range(len(visited)):
            if visited[i] == 0:
                stack.append(i)
        while len(stack):
            nc = stack.pop()
            dfs(r+1, nc, ans)
            #초기화
            if arr[r][c] != 0 and ans != 0:
                ans = ans // arr[r][c]
            visited[c] = 0
            r = r-1


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    visited = [0] * N
    stack = []
    ans = 1
    result = []
    for i in range(N):
        dfs(0, i, ans)
    #print(result)
    answer = max(result)*100/100**N
    print('#{} {}'.format(tc, answer))