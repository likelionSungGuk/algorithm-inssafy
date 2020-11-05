"""
1
2 3
0 1 1
0 2 1
1 2 6
"""
T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    adj = {i:[] for i in range(E)}
    for i in range(E):
        n1, n2, w = map(int, input().split())
        adj[n1].append([n2, w])
        adj[n2].append([n1, w])

    print(adj)

