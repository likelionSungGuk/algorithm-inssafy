'''
1
3
0 2 1
0 1 1
1 1 1
'''
from collections import deque
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]   #지형도
    INF = 99999999
    distance = [[INF for _ in range(N)] for _ in range(N)]      #dist갱신 저장소

    #출발
    distance[0][0] = 0  #0으로 초기화
    Q = deque()
    Q.append((0,0))
    while Q:
        x, y = Q.popleft()
        for k in range(4):
            nx = x+dx[k]
            ny = y+dy[k]
            if 0 <= nx < N and 0 <= ny < N:
                temp = 1                    #기본요금
                if arr[nx][ny] > arr[x][y]: #높이차만큼 요금 추가
                    temp += arr[nx][ny]-arr[x][y]
                if distance[nx][ny] > distance[x][y] +temp: #갱신
                    distance[nx][ny] = distance[x][y] + temp
                    Q.append((nx, ny))
    for row in distance:
        print(row)
    print('#{} {}'.format(tc, distance[N-1][N-1]))
