"""
2
12 10
1B3B3B81F75E
16 2
F53586D76286B2D8
"""

hex_dict = {'A': 10,'B': 11,'C': 12,'D': 13,'E': 14,'F': 15}
def hex_to_dec(num):
    ans = 0
    length = len(num)
    for i in range(len(num)):
        if ord(num[i]) >= 65:    #문자
            ans += hex_dict[num[i]]*16**(length-i-1)
        else:
            ans += int(num[i])*16**(length-i-1)
    return ans

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = list(input())
    M = N // 4  #한 변에 있는 숫자의 개수 == 회전수 +1

    all_cases = []  #16진수로 가능한 모든 경우의 수
    for j in range(M):
        for i in range(0, N, M):
            tmp = ''
            a = arr[i:i+M]
            for i in a:
                tmp += i
            if tmp not in all_cases:
                all_cases.append(tmp)
        first = arr.pop(0)
        arr.append(first)
    
    dec_all_cases = []  #10진수로 변환한 모든 경우의수
    for k in all_cases:
        dec = hex_to_dec(k)
        dec_all_cases.append(dec)
    dec_all_cases.sort(reverse=True)
    print('#{} {}'.format(tc, dec_all_cases[K-1]))
