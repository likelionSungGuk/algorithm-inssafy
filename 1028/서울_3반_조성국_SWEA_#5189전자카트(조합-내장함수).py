"""
풀이
1. 1에서 출발해서 1로 돌아오므로 총 N 개의 구역이 있으면 N-1를 순회하는 모든 경우의 수 (순열)을 구한다.
2. 모든 경우의 수 중에서 battery를 가장 적게 쓰는 경우의 수를 구한다.

주의사항
1. 순열의 개수를 재귀로 하면 시간초과 발생함. 내장함수 사용으로 변경하면 더 빠르다.
2. 1에서 출발하는 것과 1로 돌아오는 것을 순열에 같이 넣고 battery량을 같이 구해도 결과는 같게 나온다. 하지만 불필요하게 여러번 반복되므로 해당 경우의 수에서 딱 한 번만 할 수 있도록 따로 하는게 시간 절약에 도움이 된다.
"""

from itertools import permutations

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    battery = [list(map(int, input().split())) for _ in range(N)]
    arr = [i+1 for i in range(1, N)]
    perm_list = list(permutations(arr, N-1))
    result = []
    for i in perm_list:
        # i: [2, 3]
        ans = battery[0][i[0]-1] + battery[i[-1]-1][0]
        for j in range(len(i)-1):
            ans += battery[i[j]-1][i[j+1]-1]
        result.append(ans)
    answer = min(result)
    print('#{} {}'.format(tc, answer))
