'''
1
2 3
0 1 1
0 2 1
1 2 6
'''
def make_set(x):
    p[x] = x

def find_set(x):
    if p[x] != x:
        p[x] = find_set(p[x])
    return p[x]        

def union(x, y):
    p[find_set(y)] = find_set(x)
    
for tc in range(1, int(input())+1):
    V, E = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(E)]
    p = [0] * (V+1)
    #가중치정렬
    edges = sorted(edges, key=lambda x: x[2])    #2번 idx로 정렬해라

    for i in range(V+1):
        make_set(i)

    ans = 0 #답
    cnt = 0 #간선 선택
    idx = 0 #while문 idx올리면서 간선&정점 탐색

    while cnt < V:
        x = edges[idx][0]
        y = edges[idx][1]

        if find_set(x) != find_set(y):  #같은 집합이 아니라면, union을 할 수 있다
            union(x,y)
            cnt += 1
            ans += edges[idx][2]        #선택한 간선의 가중치 값을 누적

        idx += 1

    print('#{} {}'.format(tc, ans))
