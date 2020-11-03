"""
BAD GATEWAY 떴습니다.
"""
def merge(left, right):        #병합과정
    global cnt
    result = []
    if left[-1] > right[-1]:
        cnt += 1
    while len(left) > 0 or len(right) > 0:
        if len(left) > 0 and len(right) > 0:
            if left[0] <= right[0]:
                left_first = left[0]
                result.append(left_first)
                left = left[1:]
                #result.append(left.pop(0))
            else:
                right_first = right[0]
                result.append(right_first)
                right = right[1:]
                #result.append(right.pop(0))
        elif len(left) > 0:
            left_first = left[0]
            result.append(left_first)
            left = left[1:]
        elif len(right) > 0:
            right_first = right[0]
            result.append(right_first)
            right = right[1:]
    return result

def mergeSort(arr):    #분할과정
    if len(arr) == 1:
        return arr
    mid = len(arr)//2
    left = arr[0:mid]
    right = arr[mid:]
    left = mergeSort(left)
    right = mergeSort(right)
    if left[-1] > right[-1]:
        cnt += 1
    left_idx = right_idx = total_idx = 0
    while left_idx < len(left) and right_idx < len(right):



T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    cnt = 0
    mergeSort(arr)
    ans_mid = arr[len(arr)//2]
    print('#{} {} {}'.format(tc, ans_mid, cnt))
