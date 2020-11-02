"""
1
5
2 1 0 1
3 5 3 7 9
"""
def dfs(n, ans):
    global max_ans, min_ans, N
    if n >= N-1:    #n이 0부터 시작해서 N-1에 도착하면 nums의 끝에 도달한 것이므로 return으로 재귀 빠져나감. 이때 max값과 min값을 저장해둠.
        if ans > max_ans:
            max_ans = ans
        if ans < min_ans:
            min_ans = ans
        return
    else:
        for i in range(4):      #calc의 연산자들을 모두 활용
            if calc[i]:         #연산자가 아직 남아 있을 경우,
                calc[i] -= 1
                if i == 0:      #연산자가 +인 경우
                    n_ans = ans + nums[n+1]
                elif i == 1:
                    n_ans = ans - nums[n+1]
                elif i == 2:
                    n_ans = ans * nums[n+1]
                elif i == 3:
                    n_ans = int(ans/nums[n+1])
                dfs(n+1, n_ans) #연산자 하나 쓰고서 그 다음 계속 DFS탐색 지속
                calc[i] += 1    #다시 회귀할 때는 연산자 복구

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    calc = list(map(int, input().split()))  #연산자
    nums = list(map(int, input().split()))  #숫자

    max_ans = -9999999999
    min_ans = 9999999999
    ans = nums[0]       #start
    dfs(0, ans)
    print('#{} {}'.format(tc, max_ans-min_ans))
