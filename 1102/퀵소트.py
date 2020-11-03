#피봇을 기준으로 자리를 재배치 하고 기준점을 리턴
def partition(arr, low, high):
    pivot = arr[low]    #기준점 설정
    i = low     #i 시작점 설정
    j = high    #j 시작점 설정
    while i < j:   #i와 j가 서로 만나기 전까지 반복
        while i < high and arr[i] <= pivot :
            i+=1    #i를 1늘림 => 오른쪽으로 탐색
        while j > low and arr[j] >= pivot:
            j-=1    #j를 1 감소 => 왼쪽으로 탐색
        #위의 반복을 빠져나옴 -> i는 피봇보다 큰 값찾고, j는 피봇보다 작은 값찾음
        if i < j:  # i가 여전히 j보다 작음 => 그런데 아직 탐색을 다 끝내지 않음
            arr[i],arr[j] = arr[j],arr[i]   #i와 j의 값을 서로 바꿈 => 피봇보다 작은 값과 큰값의 위치 변경
    #위의 반복을 빠져나옴 -> 모든 배열 탐색함 : i와 j가 같거나 위치 역전
    arr[low],arr[j] = arr[j],arr[low]   #피봇의 값과 왼쪽 구간(피봇보다 작은 수들)중 가장 오른쪽을 바꿈
    return j    #피봇의 위치 리턴

def quickSort(arr, low, high):
    if low < high:
        pi = partition(arr,low,high)
        quickSort(arr,low,pi-1)
        quickSort(arr,pi+1,high)

# arr = [10,7,8,9,1,5]
arr = [69,10,30,2,16,8,31,22]
n = len(arr)
quickSort(arr,0,n-1)    #정렬할 배열, 시작,끝 인덱스
print(arr)