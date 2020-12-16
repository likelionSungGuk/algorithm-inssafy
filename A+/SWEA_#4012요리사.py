"""
1
6
0 37 26 52 77 20
32 0 15 26 75 16
54 33 0 79 37 90
92 10 66 0 92 3
64 7 89 89 0 21
80 49 94 68 5 0
"""
from itertools import combinations

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    M = N//2

    temp = [i for i in range(N)]
    candidates = list(combinations(temp, M))

    minV = 999999
    for i in range(len(candidates)):
        A = candidates[i]
        B = []
        for j in temp:
            if j not in A:
                B.append(j)
        sum_a = sum_b = 0
        a = list(combinations(A, 2))
        b = list(combinations(B, 2))
        for k in a:
            sum_a += arr[k[0]][k[1]]
            sum_a += arr[k[1]][k[0]]
        for l in b:
            sum_b += arr[l[0]][l[1]]
            sum_b += arr[l[1]][l[0]]
        if abs(sum_a-sum_b) < minV:
            minV = abs(sum_a-sum_b)

    print('#{} {}'.format(tc, minV))
