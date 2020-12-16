"""
3
4
9 8 9 8
4 6 9 4
8 7 7 8
4 5 3 5
5
8 2 9 6 6
1 9 3 3 4
8 2 3 3 6
4 3 4 4 9
7 4 6 3 5
7
7 4 1 5 1 7 9
9 4 6 1 4 6 8
9 6 4 8 4 7 4
3 2 6 2 4 2 8
4 9 4 6 2 4 7
1 7 6 8 9 5 8
1 9 4 7 2 9 7
"""
"""
1. 사각형을 가장 크게 순회한다.
2. 순회 중 중간에 이전과 같은 숫자가 있으면 멈추고 다른 루트를 찾는다.
3. 1 <= 출발열 <= N-1, 0<= 출발행 <= N-2
4. max값이 4보다 작으면 의미 없음 -> 모두 -1로 처리
"""
dr = [1, 1, -1, -1]
dc = [1, -1, -1, 1]
def dfs(r, c, t, n):
    global maxV, sr, sc
    if t == 3 and r == sr and c == sc:  #한바퀴 순회 끝났음
        if maxV < n:
            maxV = n
    elif r < 0 or r >= N or c < 0 or c >= N:
        return
    elif arr[r][c] in before:
        return
    else:   #갈 수 있는 루트
        before.append(arr[r][c])
        # 오른쪽 방향 그대로 가거나 왼쪽으로 꺾었을 경우에
        if t == 0 or t == 1:
            dfs(r+dr[t], c+dc[t], t, n+1)
            # t+1방향
            dfs(r+dr[t+1], c+dc[t+1], t+1, n+1)
        elif t == 2:
            # 출발점을 향하는게 아님
            if r+c != sr+sc:
                dfs(r+dr[2], c+dc[2], t, n+1)
            else:
                dfs(r+dr[3], c+dc[3], t+1, n+1)
        # t가 3일때는 직진한다.
        else:
            dfs(r+dr[3], c+dc[3], t, n+1)
        before.remove(arr[r][c])


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]

    maxV = -1
    before = []
    for i in range(N):
        for j in range(N):
            sr = i
            sc = j
            before.append(arr[i][j])
            dfs(i+1, j+1, 0, 1)
            before.remove(arr[i][j])

    print('#{} {}'.format(tc, maxV))
