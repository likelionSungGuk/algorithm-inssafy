def bfs(v):  # v :시작점
    # 큐생성
    q = []
    # 시작점 넣기
    q.append(v)
    visited[v] = 1
    cnt = 0
    level = 0
    while q:
        s = len(q)  # 현재큐의 길이
        for j in range(s):  # 현재 레벨안에서 반복
            t = q.pop(0)  # 큐에서 하나 가져옴
            for i in adj[t]:
                if visited[i] == 0:
                    q.append(i)
                    visited[i] = 1
                    cnt += 1
        level += 1
        if level == 2: break
    return cnt


T = int(input())
for tc in range(1, T + 1):
    # 그래프 표현 -> 인접리스트
    N, M = map(int, input().split())
    adj = {i: [] for i in range(N + 1)}  # 인접리스트 초기화
    for i in range(M):  # 간선의 갯수만큼 반복
        a, b = map(int, input().split())
        adj[a].append(b)
        adj[b].append(a)  # 무방향그래프
    # print(adj)
    visited = [0] * (N + 1)
    print("#{} {}".format(tc, bfs(1)))