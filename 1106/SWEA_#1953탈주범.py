from collections import deque
def dir(x):
    if x == 1:      #상우하좌
        move = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        return move
    elif x == 2:    #상하
        move = [(-1, 0), (1, 0)]
        return move
    elif x == 3:    #좌우
        move = [(0, 1), (0, -1)]
        return move
    elif x == 4:    #상우
        move = [(-1, 0), (0, 1)]
        return move
    elif x == 5:    #우하
        move = [(0, 1), (1, 0)]
        return move
    elif x == 6:    #좌하
        move = [(1, 0), (0, -1)]
        return move
    elif x == 7:    #상좌
        move = [(-1, 0), (0, -1)]
        return move
    else:
        return


T = int(input())
for tc in range(1, T+1):
    N, M, R, C, L = map(int, input().split())   #행, 열, 맨홀r, 맨홀c, 소요시간(L)
    MAP = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0]*M for _ in range(N)]

    #
    up = [1, 2, 4, 7]
    down = [1, 2, 5, 6]
    left = [1, 3, 6, 7]
    right = [1, 3, 4, 5]

    #출발점
    Q = deque()
    Q.append((R, C))
    visited[R][C] = 1
    while Q:
        r, c = Q.popleft()
        possible = dir(MAP[r][c])
        if possible is not None:
            for i in range(len(possible)):
                nr = r+possible[i][0]
                nc = c+possible[i][1]
                if 0 <= nr < N and 0 <= nc < M and MAP[nr][nc] != 0 and visited[nr][nc] == 0:
                    if possible[i][0] == -1 and MAP[nr][nc] in down:
                        visited[nr][nc] = visited[r][c] + 1
                        if visited[nr][nc] > L:
                            break
                        Q.append((nr, nc))
                    if possible[i][0] == 1 and MAP[nr][nc] in up:
                        visited[nr][nc] = visited[r][c] + 1
                        if visited[nr][nc] > L:
                            break
                        Q.append((nr, nc))
                    if possible[i][1] == 1 and MAP[nr][nc] in left:
                        visited[nr][nc] = visited[r][c] + 1
                        if visited[nr][nc] > L:
                            break
                        Q.append((nr, nc))
                    if possible[i][1] == -1 and MAP[nr][nc] in right:
                        visited[nr][nc] = visited[r][c] + 1
                        if visited[nr][nc] > L:
                            break
                        Q.append((nr, nc))

    result = 0
    # for row in visited:
    #     print(row)
    for i in range(N):
        for j in range(M):
            if 0 < visited[i][j] <= L:
                result += 1

    print('#{} {}'.format(tc, result))
