import sys; sys.stdin = open('bio.txt', 'r')
from collections import deque

def switch(arg):
    if arg == 1:
        return 2
    elif arg == 2:
        return 1
    elif arg == 3:
        return 4
    elif arg == 4:
        return 3

def move(r, c, d):
    if d == 1:
        r -= 1
        return r, c, d
    elif d == 2:
        r += 1
        return r, c, d
    elif d == 3:
        c -= 1
        return r, c, d
    elif d == 4:
        c += 1
        return r, c, d

T = int(input())
for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    micro = [list(map(int, input().split())) for _ in range(K)]
    # MAP = [[0]*N for _ in range(N)] #값 저장용
    # MAX = [[0]*N for _ in range(N)] #최대값 저장용
    # DIR = [[0]*N for _ in range(N)] #방향 저장용

    Q = deque()
    # 범위: 0 ~ N-1
    for i in range(len(micro)):
        Q.append(micro[i])
    for k in range(M):
        temp = deque()
        tmp = deque()
        while len(Q):
            # for row in MAP:
            #     print(row)
            # print()
            start = Q.popleft()
            r = start[0]
            c = start[1]
            num = start[2]
            d = start[3]
            r, c, d = move(r, c, d)
            if 0 < r < N-1 and 0 < c < N-1:
                num = num
            else:
                num = num // 2
                d = switch(d)
            temp.append([r, c, num, d])
        MAP = [[0] * N for _ in range(N)]  # 값 저장용
        MAX = [[0] * N for _ in range(N)]  # 최대값 저장용
        DIR = [[0] * N for _ in range(N)]  # 방향 저장용
        for l in temp:
            r = l[0]
            c = l[1]
            num = l[2]
            d = l[3]
            if MAP[r][c] == 0:
                MAP[r][c] += num
                MAX[r][c] = num
                DIR[r][c] = d
            else:
                if MAX[r][c] < num:
                    MAP[r][c] += num
                    MAX[r][c] = num
                    DIR[r][c] = d
                else:
                    MAP[r][c] += num

        for i in range(N):
            for j in range(N):
                if MAP[i][j] != 0:
                    tmp.append([i, j, MAP[i][j], DIR[i][j]])
        Q = tmp


    ans = 0
    for i in range(N):
        for j in range(N):
            ans += MAP[i][j]

    print('#{} {}'.format(tc, ans))
