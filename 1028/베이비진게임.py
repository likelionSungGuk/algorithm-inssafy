def check():
    if len(A) < 3:
        return 0
    else:
        for i in range(len(A)):
            if A.count(A[i]) >= 3:  #A[i]와 똑같은 숫자가 3개 이상이면 triplet이므로 1을 return
                return 1
            elif ((A.count(A[i] - 1) > 0) and (A.count(A[i] - 2) > 0)) or ((A.count(A[i] - 1) > 0) and (A.count(A[i] + 1) > 0)) or ((A.count(A[i] + 1) > 0) and (A.count(A[i] + 2) > 0)):
                return 1

            if B.count(B[i]) >= 3:
                return 2
            elif ((B.count(B[i] - 1) > 0) and (B.count(B[i] - 2) > 0)) or ((B.count(B[i] - 1) > 0) and (B.count(B[i] + 1) > 0)) or ((B.count(B[i] + 1) > 0) and (B.count(B[i] + 2) > 0)):
                return 2
        return 0

T = int(input())
for tc in range(1, T+1):
    nums = list(map(int, input().split()))
    A = []
    B = []
    for _ in range(6):
        A.append(nums.pop(0))
        B.append(nums.pop(0))
        # print(A, B)
        ans = check()
        if ans > 0:
            break
    print('#{} {}'.format(tc, ans))
