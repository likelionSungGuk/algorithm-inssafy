from copy import deepcopy
from collections import deque

def powerset(k):
    if k == N:
        bit2 = deepcopy(bit)
        all_cases.append(bit2)
    else:
        bit[k] = 1
        powerset(k+1)
        bit[k] = 0
        powerset(k+1)

def bfs(k):
    Q = deque()
    Q.append((k, 1))
    while len(Q):
        s, n = Q.popleft()
        if visited[s] == 0:
            visited[s] = n
        for i in range(N):
            if G[s][i] == 1 and visited[i] == 0:

                Q.append((i, n+1))
    return visited


N = int(input())
people = list(map(int, input().split()))
adj = [list(map(int, input().split()))[1:] for _ in range(N)]

G = [[0]*N for _ in range(N)]
for k in range(len(adj)):
    for l in range(len(adj[k])):
        G[k][adj[k][l]-1] = 1
        G[adj[k][l]-1][k] = 1


bit = [0] * N
all_cases = []
powerset(0) # 부분집합으로 모든 경우의 수 구하기 [1, 0, 1, 1, 1, 1]의 바이너리 형태

cases = []  # 숫자형으로 변환
for i in all_cases:
    tmp = []
    temp = []
    for j in range(N):
        if i[j] == 1:
            tmp.append(j)
        else:
            temp.append(j)
    cases.append([tmp, temp])

visited = [0]*N

a = [[4], [0, 1, 2, 3, 5]]
print(bfs(a[0][0]))