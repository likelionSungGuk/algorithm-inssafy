def dfs(v):
    visited[v] = 1
    for w in range(len(G[v])):
        if G[v][w] == 1 and visited[w] == 0:
            dfs(w)

N = int(input())
M = int(input())
G = [[0]*(N+1) for _ in range(N+1)]
visited = [0]*(N+1)
for i in range(M):
    s, e = map(int, input().split())
    G[s][e] = 1
    G[e][s] = 1

dfs(1)
ans = sum(visited) -1
print(ans)