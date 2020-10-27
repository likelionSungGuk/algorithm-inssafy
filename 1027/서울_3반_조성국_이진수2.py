"""
3
0.625
0.1
0.125
"""
T = int(input())
for tc in range(1, T+1):
    N = float(input())
    binary = ''
    for k in range(1, 13):
        if N != 0:
            if N >= (1/2)**k:
                N = N-(1/2)**k
                binary+='1'
            else:
                binary+='0'
        else:
            break
        if k == 12 and N != 0:
            binary = 'overflow'

    print('#{} {}'.format(tc, binary))
