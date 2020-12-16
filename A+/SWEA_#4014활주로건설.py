"""
1
6 2
3 3 3 2 1 1
3 3 3 2 2 1
3 3 3 3 3 2
2 2 3 2 2 2
2 2 3 2 2 2
2 2 2 2 2 2
"""
"""
0. 행 우선순회, 열 우선순회로 각각의 한 줄을 리스트로 만들고 이때 top,bottom을 같이 구한다.
1. 행에서 가장 높은  높이(top)와 낮은 높이(bottom)와 각각의 갯수를 구한다
2. top - bottom 이 1이면 가능성이 있음. top - bottom이 0이면 평지이므로 바로 가능. >=2는 가능성 없으므로 pass
3. bottom크기가 연속적으로 붙어있고 그 크기가 X보다 크거나 같은지 파악
    3-1. bottom이 연속된 구간이 X보다 크거나 같다면, 
"""
def check(arr):
    cnt = 1
    before = arr[0]
    for i in range(1, len(arr)):
    #내리막
        if arr[i] < before:
            if before-arr[i] > 1:
                return 0
            else:
                if i+X > len(arr): #남은 길이가 X보다 짧으면 나가리
                    return 0
                else:   #남은 길이가 X보다 길면
                    for j in range(i, i+X):
                        if arr[j] != arr[i]:
                            return 0
                    cnt = -X+1
    #오르막
        elif arr[i] > before:
            if arr[i]-before > 1:
                return 0
            else:
                if cnt >= X:
                    cnt = 1
                else:
                    return 0
    #평지
        else:
            cnt += 1
        before = arr[i]
    return 1

T = int(input())
for tc in range(1, T+1):
    N, X = map(int, input().split())
    MAP = [list(map(int, input().split())) for _ in range(N)]

    cases = []
    #열 우선순회(가로)
    for i in range(N):
        tmp = []
        for j in range(N):
            tmp.append(MAP[i][j])
        cases.append(tmp)
    #행 우선순회(세로)
    for i in range(N):
        tmp = []
        for j in range(N):
            tmp.append(MAP[j][i])
        cases.append(tmp)

    #cases의 모든 경우의수를 돌면서 유망한지 아닌지 확인
    ans = 0
    for i in range(len(cases)):
        ans += check(cases[i])

    print('#{} {}'.format(tc, ans))
