from itertools import combinations

def powerset(n, k, v):
    if n == k:
        for i in range(len(bit)):
            if bit[i] == 1:
                v += tmp[i]
                if maxV < v <= C:
                    cases.append(v)
        return
    else:
        bit[k] = 0
        powerset(n, k+1, v)
        bit[k] = 1
        powerset(n, k+1, v)

T = int(input())
for tc in range(1, T+1):
    N, M, C = map(int, input().split())
    MAP = [list(map(int, input().split())) for _ in range(N)]
    bit = [0] * M

    cases = []
    for i in range(N):
        maxV = tmp = 0
        for j in range(N-M+1):
            tmp = MAP[i][j+M]
            powerset(N, 0, 0)


    # print('#{} {}'.format(tc, maxV))
