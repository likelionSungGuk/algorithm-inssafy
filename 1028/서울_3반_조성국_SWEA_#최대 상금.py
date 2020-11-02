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
def numbering(arr): #10진수 숫자화
    ans = 0
    for i in range(len(arr)):
        ans += arr[i]*10**(len(arr)-i-1)
    return ans

"""
1. M이 1이면 맨 앞의 자리 수가 최대값이 아닐 경우 가장 뒤 index에 있는 최대값과 swap
2. M이 2 이상이면, 가장 작은 
"""

T = int(input())
for tc in range(1, T + 1):
    N, M = map(str, input().split())
    arr = [int(i) for i in N]
    M = int(M)

    print(arr, M)

    
