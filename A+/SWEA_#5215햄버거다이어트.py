"""
1
5 1000
100 200
300 500
250 300
500 1000
400 400
"""
def perm(n, k, v):
    global maxV
    if n == k:
        tmp = 0
        cal = 0
        for i in range(len(bit)):
            if bit[i] == 1:
                tmp += data[i][0]
                cal += data[i][1]
        if tmp > maxV and cal <= L:
            maxV = tmp
        return
    else:
        bit[k] = 0
        perm(n, k+1, v)
        bit[k] = 1
        perm(n, k+1, v)

T = int(input())
for tc in range(1, T+1):
    N, L = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(N)]

    max_taste = 0
    bit = [0]*N
    maxV = 0
    perm(N, 0, 0)
    print('#{} {}'.format(tc, maxV))
