"""
1
1010
212
"""
def binary(n):
    N = len(n)
    num = 0
    for i in range(N-1, -1, -1):
        if n[i] == '1':
            num += 2**(N-i-1)
    return num

def ternary(n):
    N = len(n)
    num = 0
    for i in range(N - 1, -1, -1):
        if n[i] != '0':
            num += 3**(N-i-1)*int(n[i])
    return num

T = int(input())
for tc in range(1, T+1):
    bin = input()
    tri = input()

    binaries = []       #가능한 모든 이진수
    ternaries = []      #가능한 모든 삼진수
    #이진수 변화 가능한 조합 모두 찾아내기
    for i in range(len(bin)):
        temp = list(bin)
        if bin[i] == '1':
            temp[i] = '0'
        else:
            temp[i] = '1'
        binaries.append(temp)
    #삼진수 변화가능한 모양 모두 찾아내기

    for i in range(len(tri)):
        temp2 = list(tri)
        arr = ['0', '1', '2']
        present = arr.index(temp2[i])
        arr.pop(present)
        for j in arr:
            temp2 = list(tri)
            temp2[i] = j
            ternaries.append(temp2)
    result_bin = []
    result_tri = []
    for i in binaries:
        ans = binary(i)
        result_bin.append(ans)
    for i in ternaries:
        ans = ternary(i)
        result_tri.append(ans)

    for i in result_bin:
        if i in result_tri:
            answer = i
            break

    print('#{} {}'.format(tc, answer))
