"""
1
5
2 1 0 1
3 5 3 7 9
"""
def calculator(arr):    #왼쪽에서부터 순서대로 계산
    new_arr = arr[:]
    idx = 0
    left = new_arr[0]
    while idx < len(arr):
        if type(new_arr[idx]) == int:
            idx += 1
            continue
        elif type(new_arr[idx]) == str:
            operator = new_arr[idx]
            right = new_arr[idx+1]
            if operator == '+':
                left = left + right
            elif operator == '-':
                left = left - right
            elif operator == '*':
                left = left * right
            elif operator == '/':
                if right != 0:
                    left = int(left / right)
        idx += 1
    return left

def perm(n, k):
    temp = calcs[:]
    if n == k:
        if temp not in perms:
            perms.append(temp)
    else:
        for i in range(len(calcs)):
            calcs[n], calcs[i] = calcs[i], calcs[n]
            perm(n+1, k)
            calcs[n], calcs[i] = calcs[i], calcs[n]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    calc = list(map(int, input().split()))
    nums = list(map(int, input().split()))
    M = len(nums)

    calcs = []
    for i in range(len(calc)):
        if i == 0:   #더하기
            for j in range(calc[i]):
                calcs.append('+')
        elif i == 1: #빼기
            for j in range(calc[i]):
                calcs.append('-')
        elif i == 2: #곱하기
            for j in range(calc[i]):
                calcs.append('*')
        else:   #나누기
            for j in range(calc[i]):
                calcs.append('/')
    perms = []
    perm(0, M-1)

    result = []
    for i in range(len(perms)):
        new_arr = []
        for j in range(N*2-1):
            if j % 2 == 0:
                new_arr.append(nums[j//2])
            else:
                new_arr.append(perms[i][j//2])
        ans = calculator(new_arr)
        result.append(ans)

    max_result = max(result)
    min_result = min(result)
    answer = max_result - min_result
    print('#{} {}'.format(tc, answer))

"""
#1 24
#2 8
#3 144
#4 8
#5 91
#6 150
#7 198
#8 2160
#9 46652
#10 701696
"""