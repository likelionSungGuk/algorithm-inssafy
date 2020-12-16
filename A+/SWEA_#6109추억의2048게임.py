"""
2
5 up
4 8 2 4 0
4 4 2 0 8
8 0 2 4 4
2 2 2 2 8
0 2 2 0 0
2 down
16 2
0 2
"""
from collections import deque
#상 우 하 좌
dr = [1, 0, -1, 0 ]
dc = [0, -1, 0, 1]
T = int(input())
for tc in range(1, T+1):
    M, D = map(str, input().split())
    N = int(M)
    arr = [list(map(int, input().split())) for _ in range(N)]

    #방향에 따라 dir 설정해주기
    if D == 'up':
        dir = 0
    elif D == 'right':
        dir = 1
    elif D == 'down':
        dir = 2
    else:
        dir = 3

    if dir == 0:
        for r in range(N):
            Q = deque()
            for c in range(N):
                if arr[c][r]:
                    Q.append(arr[c][r])
                    arr[c][r] = 0
            idx = 0
            while Q:
                if len(Q) > 1:
                    first, second = Q.popleft(), Q.popleft()
                    if first == second:
                        arr[idx][r] = first+second
                    else:
                        arr[idx][r] = first
                        Q.appendleft(second)
                    idx+=1
                else:
                    arr[idx][r] = Q.popleft()
    elif dir == 2:  #down
        for r in range(N):
            Q = deque()
            for c in range(N-1, -1, -1):
                if arr[c][r]:
                    Q.append(arr[c][r])
                    arr[c][r] = 0
            idx = N-1
            while Q:
                if len(Q) > 1:
                    first, second = Q.popleft(), Q.popleft()
                    if first == second:
                        arr[idx][r] = first+second
                    else:
                        arr[idx][r] = first
                        Q.appendleft(second)
                    idx-=1
                else:
                    arr[idx][r] = Q.popleft()
    elif dir == 3:   #left
        for r in range(N):
            Q = deque()
            for c in range(N):
                if arr[r][c]:
                    Q.append(arr[r][c])
                    arr[r][c] = 0
            idx = 0
            while Q:
                if len(Q) > 1:
                    first, second = Q.popleft(), Q.popleft()
                    if first == second:
                        arr[r][idx] = first + second
                    else:
                        arr[r][idx] = first
                        Q.appendleft(second)
                    idx += 1
                else:
                    arr[r][idx] = Q.popleft()

    elif dir == 1:   #right
        for r in range(N):
            Q = deque()
            for c in range(N-1, -1, -1):
                if arr[r][c]:
                    Q.append(arr[r][c])
                    arr[r][c] = 0
            idx = N-1
            while Q:
                if len(Q) > 1:
                    first, second = Q.popleft(), Q.popleft()
                    if first == second:
                        arr[r][idx] = first + second
                    else:
                        arr[r][idx] = first
                        Q.appendleft(second)
                    idx -= 1
                else:
                    arr[r][idx] = Q.popleft()

    print('#{}'.format(tc))
    for row in arr:
        for i in row:
            print(i, end=' ')
        print()
