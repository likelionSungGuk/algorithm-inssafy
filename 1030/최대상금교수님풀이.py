arr = [4, 5, 6, 7, 8, 9]
N = len(arr)


visit = [set() for _ in rnage(11)]
def backtrack(k):
    global ans
    num = int(''.join(map(str, arr)))
    if num in visit[k]:
        return
    visit[k].add(num)
    if k == cnt:
        if ans < num:
            ans = num
            print(ans)
    else:
        for i in range(N-1):
            for j in range(i+1, N):
                arr[i], arr[j] = arr[j], arr[i]
                backtrack(k+1)
                arr[i], arr[j] = arr[j], arr[i]

backtrack(0)
print(ans)