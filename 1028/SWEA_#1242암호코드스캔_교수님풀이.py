h2b={
    '0': '0000',
    '1': '0001',
    '2': '0010',
    '3': '0011',
    '4': '0100',
    '5': '0101',
    '6': '0110',
    '7': '0111',
    '8': '1000',
    '9': '1001',
    'A': '1010',
    'B': '1011',
    'C': '1100',
    'D': '1101',
    'E': '1110',
    'F': '1111',
}
pwd = {
    112: 0,
    122: 1,
    221: 2,
    114: 3,
    231: 4,
    132: 5,
    411: 6,
    213: 7,
    312: 8,
    211: 9,
}
def search(N, M, b):
    v = [[0] * M for _ in range(N)] #방문배열
    s = 0
    for i in range(N):
        j = M-1                     #뒤에서부터 시작
        while (j > 0):
            #1이고 아직 방문 안했으면 시작
            if (b[i][j] == '1' and v[i][j] == 0):
                p = [0]*8           #코드를 저장하기 위한 배열
                c = j
                for k in range(7, -1, -1):  #7칸씩 읽는다 이때 뒤에서 3개만 의미가 있음
                    cnt = [0, 0, 0]         #뒤에서 부터 읽어서 1과 0의 칸수를 저장
                    while (b[i][c] == '0'):  #뒤에서 세 칸 아닌 친구들은 그냥 c를 왼쪽으로 옮기면서 SKIP
                        c -= 1
                    while (b[i][c] == '1'):
                        cnt[0] += 1
                        c -= 1              #c를 왼쪽으로 한 칸 씩 이동해서 읽기
                    while (b[i][c] == '0'):
                        cnt[1] += 1
                        c -= 1
                    while (b[i][c] == '1'):
                        cnt[2] += 1
                        c -= 1
                    #비율이므로 cnt의 최소값으로 나눠줌
                    d = min(cnt)
                    p[k] = pwd[cnt[0]//d*100 + cnt[1]//d*10 +cnt[2]//d]

                #이제 정상적인 암호인지 확인
                check = (p[0] + p[2] + p[4] + p[6]) * 3+p[1] + p[3]+ p[5] + p[7]
                if check % 10 == 0:
                    s += sum(p)         #정상이면 누적합
                #방문처리
                x = i
                while b[x][j] == '1':           #행방향이 1일 동안
                    for y in range(j, c-1, -1): #왼쪽으로 이동하면서
                        v[x][y] = 1
                    x += 1
                j = c
            else:       #1이 아니거나 이미 방문한 곳이면
                j -= 1
    return s


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    h = [input() for _ in range(N)]
    b = ['']*N
    for i in range(N):
        for j in range(M):
            b[i] += h2b[h[i][j]]

    ans = search(N, M*4, b)
    print('#{} {}'.format(tc, ans))
