T = int(input())
for tc in range(1, T+1):
    N, M = map(str, input().split())
    password = list(M)
    new_password = []
    #16진수를 10진수 변환
    for i in range(len(password)):
        d = ord(password[i])-ord('0') if '0' <= password[i] <= '9' else ord(password[i])-ord('A') + 10
        new_password.append(d)
    output = ''
    for i in new_password:
        for j in range(3, -1, -1):
            if i & (1<<j):
                output+='1'
            else:
                output+='0'
    print('#{} {}'.format(tc, output))
    