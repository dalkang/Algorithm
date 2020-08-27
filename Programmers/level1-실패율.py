def solution(N, stages):
    answer = []
    sorted_stages = sorted(stages)
    users = len(stages)
    rest = users
    percent = []

    i = 0
    for order in range(1, N+1):
        if i < users:
            # N번째 스테이지에 사람이 없는 경우
            if (sorted_stages[i] != order):
                percent.append([0, order])             
            else:
                cnt = 0
                while (i < users) and (sorted_stages[i] == order):
                    cnt += 1
                    i += 1
                percent.append([cnt/rest, order])
                rest -= cnt
        else:
            # 남은 유저가 없는 경우
            percent.append([0, order])

    percent_sorted = sorted(percent, key = lambda x : (-x[0], x[1]))

    for per in percent_sorted:
        answer.append(per[1])

    return answer