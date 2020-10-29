"""
10
123 1
2737 1
757148 1
78466 2
32888 2
777770 5
436659 2
431159 7
112233 3
456789 10
"""
"""
왼쪽에 있는 수보다 오른쪽에 있는 수가 더 큰 것이 있나?
 - 그렇다면 그 중에 가장 큰 수를 맨 왼쪽으로 옮긴다.
 - 아니면 다음 숫자로 점프한다

"""

T = int(input())
for tc in range(1, T+1):
    N, M = map(str, input().split())
    arr = [int(i) for i in N]
    M = int(M)

    cnt = 0
    while cnt < M:
        start = arr[cnt]
        max_ans = 0

        cnt += 1

    print(arr)