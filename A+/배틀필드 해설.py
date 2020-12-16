def search_tank():
    for i in range(H):
        for j in range(W):
            if game[i][j] in tank:
                r = i
                c = j
                dir = tank.index(game[i][j])
                answer = (r, c, dir)
                return answer


tank = ['^', 'v', '<', '>']
dir_dict = {'U': 0, 'D': 1, 'L': 2, 'R': 3}

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

for tc in range(1, int(input())+1):
    H, W = map(int, input().split())
    game = [list(input()) for _ in range(H)]

    N = int(input())
    cmd_list = list(input())

    #1. 탱크 위치 찾기
    r = c = dir = -1

    r, c, dir = search_tank()

    #2. 명령어 처리
    for cmd in cmd_list:
        #2-1 포탄 발사
        if cmd == 'S':
            nr = r+dr[dir]
            nc = c+dc[dir]
            while 0<=nr<H and 0<=nc<W:
                # if nr<0 or nr >=H or nc < 0 or nc >= W:     #맵 밖을 벗어남
                #     break
                if game[nr][nc] == '#':
                    break
                if game[nr][nc] == '*':
                    game[nr][nc] = '.'
                    break
                nr += dr[dir]
                nc += dc[dir]
        #2-2 방향전환
        else:
            dir = dir_dict[cmd]
            #전차방향 바꾸기
            game[r][c] = tank[dir]

            nr =r+dr[dir]
            nc =c+dc[dir]

            if 0 <= nr < H and 0 <= nc < W and game[nr][nc] == '.':
                game[nr][nc] = tank[dir]
                game[r][c] = '.'
                r, c = nr, nc

    print('#{}'.format(tc), end=' ')
    for row in game:
        print(''.join(row))
