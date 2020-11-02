#1. [분할] 최소단위(숫자1개)가 될 때 까지 반으로 계속 쪼갠다. (재귀)
#2. [병합] 두 개씩 정렬. 이후 한 칸 위 단위로 올라가면서 다시 정렬.
def merge(left, right):    #합병과정
    result = [] #정렬 결과를 담을 배열
    while len(left) > 0 or len(right) > 0:  #배열에 자료가 있는 동안 반복
        if len(left) > 0 and len(right) > 0:#양쪽 모두에 자료가 있는 경우, 왼쪽과 오른쪽에서 하나씩 빼서 비교
            if left[0] <= right[0]:         #왼쪽이 더 작으면 왼쪽에서 pop
                result.append(left.pop(0))
            else:                           #오른쪽이 더 작으면 오른쪽에서 pop
                result.append(right.pop(0))
        elif len(left) > 0:     #왼쪽에만 자료가 있는 경우, 왼쪽 배열의 순서대로 하나씩 뒤에 추가 (왼쪽에는 정렬이 되어있으므로)
            result.append(left.pop(0))
        elif len(right) > 0:     #오른쪽에만 자료가 있는 경우, 오른쪽 배열의 순서대로 하나씩 뒤에 추가
            result.append(right.pop(0))
    return result

def merge_sort(arr): #분할과정
    if len(arr) == 1:
        return arr
    left = []   # 왼쪽배열
    right = []  # 오른쪽배열
    mid = len(arr) // 2
    #1. 반복문으로 활용
    for i in range(len(arr)):
        if i < mid:
            left.append(arr[i])
        else:
            right.append(arr[i])
    #2 슬라이싱
    # left = arr[0:mid]
    # right = arr[mid:]
    left = merge_sort(left)
    right = merge_sort(right)
    print(left, right)
    return merge(left, right)

arr = [69, 10, 30, 2, 5, 16, 8, 31, 22]
arr_result = merge_sort(arr)
#print(arr_result)