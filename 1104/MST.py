"""
7 11
0 5 60
0 1 32
0 2 31
0 6 51
1 2 21
2 4 46
2 6 25
3 4 34
3 5 18
4 5 40
4 6 51
"""
V, E = map(int, input().split())
adj = [[0] * V for _ in range(V)]
for i in range(E):
    a, b, c = map(int, input().split())
    adj[a][b] = c   #무방향 가중치 그래프
    adj[b][a] = c

INF = 999999    #무한대
key = [INF]*V   #가중치를 저장할 key배열
mst = [0]*V     #mst인지 아닌지 저장

#시작점 선택: 0번으로 선택
key[0] = 0
cnt = 0     #정점 선택 횟수 (cnt가 정점의 수 V와 같아지면 MST끝)
result = 0  #MST 가중치 저장

while cnt <= V-1:
    #key가 최소인 정점 u 찾기
    minV = INF
    minIdx = 0
    for i in range(V):
        if not mst[i] and minV > key[i]:
            minV = key[i]
            minIdx = i
    mst[minIdx] = True  #mst에 포함하기
    result += minV
    cnt += 1
    #u에 인접한 정점의 key값을 갱신
    #u에 인접한 정점 w중 아직 MST가 아니고 u-w 가중치가 u의 key값보다 작으면
    for w in range(V):
        if adj[minIdx][w] > 0 and key[w] > adj[minIdx][w] and not mst[w]:
            #key값 갱신
            key[w] = adj[minIdx][w]
print(key)
print(result)
