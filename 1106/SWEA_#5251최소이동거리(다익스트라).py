import heapq
def dijkstra():     #Prim과 유사
    dist = [987654321]*(V+1)
    visited = [0]*(V+1)

def dijkstra_heap():
    dist = [987654321] * (V + 1)
    visited = [0] * (V + 1)

    heap = []
    dist[0] = 0
    heapq.heappush(heap, (0,0))

    while heap: #heap이 공백이 될 때까지
        w, v = heapq.heappop(heap)

        if not visited[v]:
            visited[v] = 1
            dist[v] = w

            for i in range(V+1):
                if not visited[i] and dist[i] > dist[v] + adj[v][i]:
                    heapq.heappush(heap, (dist[v]+adj[v][i], i))

        return dist[V]


for tc in range(1, int(input())+1):
    V, E = map(int, input().split())

    