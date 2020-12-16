'''
2
6 5
2 3
3 4
4 5
5 6
2 5
6 5
1 2
1 3
3 4
2 3
4 5
'''
def bfs(v):
    global result
    visited[v] = 1
    Q = []
    Q.append([v, 0])
    while len(Q):
        start = Q.pop()
        s, depth = start[0], start[1]
        for i in range(1, N+1):
            if visited[i] == 0 and G[s][i] == 1:
                visited[i] = 1
                result += 1
                if depth < 1:
                    Q.append([i, depth+1])

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    G = [[0]*(N+1) for _ in range(N+1)]
    visited = [0]*(N+1)
    for i in range(M):
        s, e = map(int, input().split())
        G[s][e] = 1
        G[e][s] = 1

    depth = result = 0
    friends = sum(G[1])        #상원이 친구 있는지 체크
    if friends != 0:           #1. 친구 있으면 BFS 단계2까지만
        bfs(1)
    print('#{} {}'.format(tc, result))
