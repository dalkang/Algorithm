def solution(s):
    answer = []
    # 양 옆의 {{ }} 대괄호 두 개는 빼고 난 후에 남은 '},{'를 기준으로 split
    edit_s = s[2:len(s)-2].split('},{')

    # 리스트 길이를 기준으로 sort
    sorted_array = sorted(edit_s, key=len)

    # ','를 기준으로 split 한 리스트를 돌며 answer에 안 담긴 숫자들만 담기
    for j in sorted_array:
        check = list(map(int, j.split(',')))
        for k in check:
            if k not in answer:
                answer.append(k)

    return answer