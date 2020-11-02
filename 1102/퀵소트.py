def partition(arr, low, high): #pivot을 기준으로 자리를 재배치 하고 기준점을 리턴
    pivot = arr[low]
    i = low         #i(왼쪽) 시작점
    j = high        #j(오른쪽) 시작점
    while i <= j:
        while i <= high and arr[i] <= pivot:
            i += 1  #i를 1늘림(오른쪽으로 탐색)
        while j >= low and arr[j] >= pivot:
            j -= 1    #j -1(왼쪽으로 탐색)
        if i < j:   #위 반복에서 빠져나오고 swap
            arr[i], arr[j] = arr[j], arr[i]
    arr[low], arr[j] = arr[j], arr[low]
    return j
def quickSort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quickSort(arr, low, pi-1)   #새로 정해진 partition의 왼쪽부터 처음까지
        quickSort(arr, pi+1, high)  #새로 정해진 partition의 오른쪽부터 끝까지

arr = [10, 7, 8, 9, 1, 5]
#arr = [69, 10, 30, 2, 16, 8, 31, 22]
n = len(arr)
quickSort(arr, 0, n-1)  #배열, 시작idx, 끝idx
print(arr)