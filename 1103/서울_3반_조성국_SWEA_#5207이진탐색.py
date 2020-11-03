"""
3
3 3
1 2 3
2 3 4
3 5
1 3 5
2 4 6 8 10
5 5
1 3 5 7 9
1 2 3 4 5
"""
def search(arr, target, left, right):
    before = 0
    while left <= right:
        mid = (left + right) // 2
        #print("left, mid, right, arr[mid]", left, mid, right, arr[mid])
        if arr[mid] == target:
            return 1
        elif arr[mid] > target:  #중간값보다 작을 때(좌측탐색)
            right = mid-1
            current = 1
            mid = (left + right) // 2
        else:                    #중간값보다 클 때 (우측탐색)
            left = mid+1
            current = 2
            mid = (left + right) // 2
        if before == current:
            return 0
        before = current
    return 0


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort()
    B.sort()
    left = 0
    right = len(A) - 1

    result = []
    for i in range(len(B)):
        target = B.pop(0)
        result.append(search(A, target, left, right))

    print('#{} {}'.format(tc, sum(result)))
