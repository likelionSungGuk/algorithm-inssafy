def find(k, percent):
    global maxV
    if k == N:  #순열을 다고르면
        if maxV < percent:    #확률중 가장 좋은거 고르기
            maxV = percent
        return
    if percent < maxV:        #백트래킹. 퍼센트는 곱할수록 작아지므로 percent가 현재 maxV보다 작으면 더 할 필요도 없음
        return
    for i in range(N):
        if not visited[i] and p[k][i] != 0 :
            visited[i] = True
            find(k+1,percent*p[k][i])
            visited[i] = False

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    p = [ list(map(int,input().split())) for _ in range(N)]
    for i in range(N):
        for j in range(N):
            p[i][j] /= 100
    # for row in p:
    #     print(row)
    sel = [0] * N
    visited = [False] * N
    maxV = 0    #최대값 저장
    find(0,1)
    print(maxV*100)