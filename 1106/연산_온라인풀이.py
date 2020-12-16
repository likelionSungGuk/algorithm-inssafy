def calc(num, idx):
    if idx == 0:
        return num + 1
    elif idx == 1:
        return num - 1
    elif idx == 2:
        return num * 2
    elif idx == 3:
        return num - 10

def BFS():
    queue = [0] * 1000000
    front = rear = -1       #포인터 방식으로 이동하며 queue에 저장(append를 대신함)

    rear += 1
    queue[rear] = (N, 0)
    memo[N] = 0

    while front != rear:
        front += 1
        curr_n, curr_cnt = queue[front]

        if curr_n == M:
            return curr_cnt
        for i in range(4):
            next_n = calc(curr_n, i)

            if 0 < next_n <= 1000000 and memo[next_n] != -1:
                memo[next_n] = memo[curr_n] + 1
                rear += 1
                queue[rear] = (next_n, curr_cnt+1)
    return memo[M]

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())

    memo = [-1] * 1000001