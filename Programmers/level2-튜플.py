def solution(s):
    answer = []
    # 양 옆의 {{ }} 대괄호 두 개는 빼고 난 후에 남은 '},{'를 기준으로 split, 리스트 길이로 sorted
    sorted_s = sorted(list(s[2:len(s)-2].split('},{')), key=len)

    # ','를 기준으로 split 한 set에서 answer set을 빼서 겹치지 않는 것 담기
    for s in sorted_s:
        answer += list( set(map(int, s.split(','))) - set(map(int, answer)) )

    return answer