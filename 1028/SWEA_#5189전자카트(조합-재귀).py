def comb(n, k):
    if n == k:
        temp = arr[:]
        if temp not in comb_list:
            comb_list.append(temp)
    else:
        for i in range(len(arr)):
            arr[n], arr[i] = arr[i], arr[n]
            comb(n+1, k)
            arr[n], arr[i] = arr[i], arr[n]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    battery = [list(map(int, input().split())) for _ in range(N)]

    # N! 만큼의 경우의 수 중에서 마지막에 1로 끝나는 것들만 선택
    arr = [i+1 for i in range(N)]
    comb_list = []
    comb(0, N)
    cases = []
    for i in comb_list:
        if i[-1] == 1:
            i.insert(0, 1)
            cases.append(i)

    result = []
    for i in cases:
        ans = 0
        # i: [1, 2, 3, 1]
        for j in range(len(i)-1):
            ans += battery[i[j]-1][i[j+1]-1]
        result.append(ans)
    answer = min(result)
    print('#{} {}'.format(tc, answer))
