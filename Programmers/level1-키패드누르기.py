def solution(numbers, hand):
    answer = ''
    key = [[1,2,3],[4,5,6],[7,8,9],['*',0,'#']]
    left_hand = (3,0)
    right_hand = (3,2)

    # number의 좌표 찾기
    for num in numbers:
        for i in range(4):
            for j in range(3):
                if num == key[i][j]:

                    # number의 좌표를 가지고, 손 위치 설정 및 answer 추가
                    if num == 1 or num == 4 or num == 7:
                        left_hand = (i,j)
                        answer += 'L'
                        break
                    elif num == 3 or num == 6 or num == 9:
                        right_hand = (i,j)
                        answer += 'R'
                        break

                    # 절대값으로 거리 찾고 비교해서, 손 위치 설정 및 answer 추가
                    else:
                        abs_left = (( abs(i-left_hand[0]) )+( abs(j-left_hand[1])) )
                        abs_right = (( abs(i-right_hand[0]) )+( abs(j-right_hand[1])) )
                        
                        if abs_left < abs_right:
                            left_hand = (i,j)
                            answer += 'L'
                        elif abs_left > abs_right:
                            right_hand = (i,j)
                            answer += 'R'
                        else:
                            if hand == 'left':
                                left_hand = (i,j)
                                answer += 'L'
                            else:
                                right_hand = (i,j)
                                answer += 'R'

    return answer