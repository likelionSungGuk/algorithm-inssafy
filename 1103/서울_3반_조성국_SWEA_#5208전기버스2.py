#경축! 9차 시도 만에 통과....

T = int(input())
for tc in range(1, T+1):
    arr = list(map(int, input().split()))
    N = arr[0]
    battery_stop = arr[1:]

    energy = battery_stop[0]    #출발 energy
    idx = 0                     
    dist = N-1-idx              #도착지까지 남은 거리
    cnt = 0                     #충전횟수
    while idx < N-1:
        #남은 거리보다 에너지가 많을 때
        if dist <= energy:  #'도착권에 들었음. 더이상 cnt 안늘려줘도 됨'
            print('#{} {}'.format(tc, cnt))
            break

        #남은 거리보다 에너지가 적을 때
        else:
            # 에너지 범위 내에서 어떤 값을 선택하는 것이 좋을 지 선택
            maxV = 0
            move = 0
            for i in range(1, energy+1):
                if battery_stop[idx+i]+i >= maxV:   #에너지값이 크면 클수록, index값이 뒤이면 뒤일수록 최소 cnt의 가능성이 높다. 따라서 maxV를 이에 맞춰 변경시킨다.
                    move = i
                    maxV = battery_stop[idx+i]+i
            # 해당 위치로 이동
            # idx값 조정, dist값 조정, energy값 조정
            dist -= move                            #남은 거리값은 이동거리만큼 빼주고
            idx += move                             #idx값 move만큼 이동
            energy = battery_stop[idx]              #새로운 곳에서 충전한 에너지로 변경 (!이게 중요. energy를 남은 것에 추가하는게 아니라 충전하면 그게 최대값이다.)
            # 충전 카운트 += 1
            cnt += 1
