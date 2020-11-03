def merge(a):
    global cnt
    if len(a) == 1:
        return a
    mid = len(a)//2
    left = a[0:mid]
    right = a[mid:]
    #1. 재귀로 끝까지 분할
    left = merge(left)
    right = merge(right)
    if left[-1] > right[-1]:
        cnt += 1

    idxl = idxr = i = 0
    #2. 양쪽 동시에 비교하기
    while idxl < len(left) and idxr < len(right):
        if left[idxl] < right[idxr]:
            a[i] = left[idxl]
            idxl += 1
        else:
            a[i] = right[idxr]
            idxr += 1
        i += 1

    #3. 한쪽씩 나머지 처리하기
    if idxl < len(left):
        a[i:] = left[idxl:]
    if idxr < len(right):
        a[i:] = right[idxr:]
    print(a)
    return a

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    cnt = 0
    answer = merge(arr)
    mid = answer[len(arr)//2]
    print('#{} {} {}'.format(tc, mid, cnt))