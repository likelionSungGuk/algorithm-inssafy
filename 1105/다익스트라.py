'''
#단방향 가중치 그래프
6 11        
0 1 3
0 2 5
1 2 2
1 3 6
2 1 1
2 3 4
2 4 6
3 4 2
3 5 3
4 0 3
4 5 6
'''
V, E = map(int, input().split())
adj = {i:[] for i in range(V)}
for i in range(E):
    n1, n2, c = map(int, input().split())   #시작, 끝, 가중치
    adj[n1].append([n2, c])                       #인접 리스트

#print(adj)
INF = 999999
dist = [INF] * V                 #각 정점까지의 최단거리
selected = [False] * V           #확정적으로 선택된 정점
#시작점
dist[0] = 0
cnt = 0
while cnt <= V-1:
    #최소값 찾기
    minV = INF
    u = -1
    for i in range(V):
        #아직 최단거리가 결정 안되고 최소인 정점을 선택
        if not selected[i] and minV > dist[i]:
            minV = dist[i]
            u = i
    #위 for문을 다 돌고나면 u에는 가장 작은 최단거리값이 확정됨
    selected[u] = True
    cnt += 1

    #간선완화 (edges relaxation)
    for w, cost in adj[u]:              #w: 도착정점, cost: 가중치
        if dist[w] > dist[u]+cost:
            dist[w] = dist[u] + cost    #갱신
print(dist)
