"""
1
5
2 1 0 1
3 5 3 7 9
"""
from itertools import permutations
def perm(n, k):
    temp = calc[:]
    if n == k:
        if temp not in perms:
            perms.append(temp)
    else:
        for i in range(len(calc)):
            calc[n], calc[i] = calc[i], calc[n]
            perm(n+1, k)
            calc[n], calc[i] = calc[i], calc[n]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    raw_calc = list(map(int, input().split()))
    calc = []
    for i in range(len(raw_calc)):
        for j in range(raw_calc[i]):
            calc.append(i+1)
    nums = list(map(int, input().split()))
    M = len(nums)
    perms = list(permutations(calc, len(calc)))

    result = []
    tmp_max = -99999999
    tmp_min = 9999999
    for i in perms:
        for j in range(len(i)):
            if j == 0:
                tmp = nums[j]
            if i[j] == 1:   #더하기
                tmp += nums[j+1]
            elif i[j] == 2: #빼기
                tmp -= nums[j + 1]
            elif i[j] == 3: #빼기
                tmp *= nums[j + 1]
            elif i[j] == 4: #빼기
                tmp = int(tmp/nums[j+1])
        if tmp >= tmp_max:
            tmp_max = tmp
        elif tmp <= tmp_min:
            tmp_min = tmp
    answer = tmp_max-tmp_min
    print('#{} {}'.format(tc, answer))
