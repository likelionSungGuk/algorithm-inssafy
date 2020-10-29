T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split()) # N: 컨테이너 수, M: 트럭 수
    containers = list(map(int, input().split()))
    trucks = list(map(int, input().split()))
    containers.sort(reverse=True)
    trucks.sort(reverse=True)
    C = len(containers)
    T = len(trucks)

    result = 0
    for i in range(T):
        for j in range(C):
            if containers[j] != 0 and trucks[i] >= containers[j]:
                result += containers[j]
                trucks[i] = 0
                containers[j] = 0
                break

    print('#{} {}'.format(tc, result))
