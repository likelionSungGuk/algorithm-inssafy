'''
1
5
0 0 100 100 70 40 30 10 10 5 90 70 50 20
'''
def find(k, x ,y, dist):
    global minV
    if k == N:
        dist += abs(x-home[0])+abs(y-home[1])
        minV = min(dist, minV)
        return
    if dist > minV:     #백트래킹 - dist가 minV보다 크다면 더 볼 것도 없다.
        return
    else:
        for i in range(N):
            if visited[i] == 0:
                visited[i] = 1
                temp = dist+abs(clients[i][0]-x)+abs(clients[i][1]-y)
                find(k+1, clients[i][0], clients[i][1], temp)
                visited[i] = 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    data = list(map(int, input().split()))
    corp = [data[0], data[1]]
    home = [data[2], data[3]]
    clients = []
    for i in range(4, len(data), 2):
        clients.append([data[i], data[i+1]])

    # corp 출발 -> clients 순회 -> home 도착
    dist = 0    #거리 (누적합)
    visited = [0] * N
    minV = 999999999
    x = corp[0]
    y = corp[1]
    find(0, x, y, dist)
    print('#{} {}'.format(tc, minV))
