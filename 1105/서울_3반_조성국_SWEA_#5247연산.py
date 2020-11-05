"""
문제를 잘 읽어야 한다....
자연수, 백만 이하...
"""
from collections import deque
def bfs(N, cnt):
    Q = deque()
    used = {}
    Q.append([N, cnt])
    while len(Q):
        s, cnt = Q.popleft()
        if s == M:
            return cnt
        if used.get(s, 0):
            continue
        elif 0 <= s < 1000000:
            used[s] = 1
            cnt += 1
            for j in range(4):
                if j == 0:
                    Q.append([s+1, cnt])
                elif j == 1:
                    Q.append([s-1, cnt])
                elif j == 2:
                    Q.append([s*2, cnt])
                elif j == 3:
                    Q.append([s-10, cnt])

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    cnt = 0

    print('#{} {}'.format(tc, bfs(N, cnt)))
