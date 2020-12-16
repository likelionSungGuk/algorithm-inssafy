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
def dfs(r, c, sr, sc, i):
    global result, maxV
    #하우 - 하좌 - 상좌 - 상우
    dr = [1, 1, -1, -1]
    dc = [1, -1, -1, 1]
    if r == sr and c == sc and len(result) > 2:
        if maxV < len(result):
            maxV = len(result)
            return
    if arr[r][c] not in result:
        visited[r][c] = 1
        result.append(arr[r][c])


    while i < 4:
        nr = r+dr[i]
        nc = c+dc[i]
        #1. 다음으로 넘어갈 수 있는 경우인가
        if 0 <= nr < N and 0 <= nc < N:
            dfs(nr, nc, sr, sc, i)
            return
            # 2. 다음으로 넘어갈 수 없는 경우라면
            # 2-1. 출발점과 같은가?
            # 2-2. 나가리
        else:
            i+=1
    return


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    maxV = -1
    for i in range(N-1):
        for j in range(1, N):
            result = []
            visited = [[0] * N for _ in range(N)]
            dfs(i, j, i, j, 0)
            visited = [[0] * N for _ in range(N)]
    if maxV < 4:
        maxV = -1

    print('#{} {}'.format(tc, maxV))
