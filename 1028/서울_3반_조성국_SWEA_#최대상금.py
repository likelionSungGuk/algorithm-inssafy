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
T = int(input())
for tc in range(1, T+1):
    N, M = map(str, input().split())
    arr = [int(i) for i in N]
    M = int(M)
