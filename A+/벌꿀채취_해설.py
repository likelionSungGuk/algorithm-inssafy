def choose(r, c):
    global first, second
    honey = arr[r][c:c+M]

    max_cost = 0
    for i in range(1<<N):
        sum_honey = sum_cost = 0
        for j in range(M):
            if i & (1<<j):
                sum_honey = honey[j]
                sum_cost = honey[j]**2
        if sum_honey <= C:
            max_cost = max(max_cost, sum_cost)
        elif max_cost > first[0]:
            if r == first[1] and c < first[2]+M: #행이 같고 열이 M범위 내에 있을때
                first = [max_cost, r, c]
            else:
                second = first[:]           #갱신
                first = [max_cost, r, c]
        elif max_cost > second[0]:
            if r!= first[1] or c >= first+M:
                second = [max_cost, r, c]

def calc(idx, sum_honey, sum_cost):
    global max_cost2
    if sum_honey > C:
        return

    max_cost2 = max(max_cost2, sum_cost)

    for i in range(idx, M):
        calc(i+1, sum_honey+honey2[i], sum_cost+honey2[i]**2)

for tc in range(1, int(input())+1):
    N, M, C = map(int, input().split())  #변의길이, 채취할 벌통의 길이, 일꾼최대벌꿀양
    arr = [list(map(int, input().split())) for _ in range(N)]

    first = [0, 0, 0]   #값, 행, 열
    second = [0, 0, 0]   #값, 행, 열

    honey_list = []
    #순회하면서 벌통 뽑아보기
    for i in range(N):
        for j in range(N-M+1):
            choose(i, j)
            honey2 = arr[i][j:j+M]
            max_cost2 = 0
            calc(0, 0, 0)
            honey_list.append((max_cost2, i, j))

    honey_list.sort(reverse=True)
    first2 = honey_list.pop(0)
    for cost, r, c in honey_list:
        if r == first2[1] and first2[2]-M < c < first[2]+M: continue
        second2 = [cost, r, c]
        break
    print('#{} {}'.format(tc, first[0]+second[0]))
    print('#{} {}'.format(tc, first2[0]+second2[0]))