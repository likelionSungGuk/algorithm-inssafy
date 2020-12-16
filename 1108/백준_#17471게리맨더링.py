"""
6
5 2 3 4 1 2
2 2 4
4 1 3 6 5
2 4 2
2 1 3
1 2
1 2
"""

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
result = 999999
for i in cases:
    groupA = groupB = 0
    if i[0]:
        v = bfs(i[0][0])
    else:
        continue
    #print(i, v, visited)
    tmp = []
    tmp2 = []
    temp = []
    temp2 = []
    if i[0] and i[1]:
        for j in i[0]:
            if v[j] != 0:
                tmp.append(v[j])
                tmp2.append(j)
        for k in i[1]:
            if v[k] != 0:
                temp.append(v[k])
                temp2.append(k)
    # print(tmp, temp)
    if len(tmp)+len(temp) == 6 and len(tmp) > 0 and len(temp) > 0 and (max(tmp) - min(tmp) <= 1) and (max(temp) - min(temp) <= 1):
        for l in tmp2:
            groupA += people[l]
        for m in temp2:
            groupB += people[m]
        ans = abs(groupA-groupB)

        # print(tmp2, temp2, ans, v)
        if ans < result:
            result = ans
    else:
        continue
# for row in G:
#     print(row)
print(result)
