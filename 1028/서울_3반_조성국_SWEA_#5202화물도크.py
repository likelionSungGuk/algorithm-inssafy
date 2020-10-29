"""
1. 종료시간을 기준으로 정렬
2. 다음 시작시간이 이전 종료시간보다 작으면 선택 X, 더 크면 선택
"""
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    arr_sort = sorted(arr, key=lambda x: x[1])  #종료시간이 빠른 기준으로 정렬

    s, e = arr_sort[0][0], arr_sort[0][1]  #s,e = 4, 14
    cnt = 1
    for k in range(1, len(arr_sort)):
        if arr_sort[k][0] < e:
            continue
        else:
            cnt += 1
            s = arr_sort[k][0]
            e = arr_sort[k][1]

    print('#{} {}'.format(tc, cnt))
