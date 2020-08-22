def solution(board, moves):
    stack = []
    cnt = 0
    for m in moves:
        for b in range(len(board)):
            if board[b][m-1]:
                stack.append(board[b][m-1])
                board[b][m-1] = 0
                b = 0
                break
        if 2 <= len(stack):
            if stack[len(stack)-2] == stack[len(stack)-1]:
                stack.pop()
                cnt += 1
                stack.pop()
                cnt += 1
    print(cnt)

solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4])

# 구상
# 1. moves에 적힌 순서대로 스택에 옮긴다(빈 경우는 그냥 패스)
# 1-1. moves 원소로 x축 고정, y축 옮겨가며 제일 먼저 나온 것 스택에 담기
# 2. 스택에 담고난 후 len(board)-2와 len(board)-1과 같은지 검사, 같으면 pop()하고 cnt += 1 하는 과정 두번
# 3. cnt 출력

# 오류 수정한 것들
# 1. 4가 돼야 하는데 6이 나와서 보니까 맨 위에 있는 걸 담고 나서 그 아래 것까지 담고 있었음, break로 빠져나와야 했음
# 2. 그리고 for문 빠져나와도 결과가 같아서 디버깅 해보니까 for문이 리셋 안 되고 숫자가 그대로 남아 있었음, for문 변수 초기화 시키고 break 하기
# 3. 그래도 똑같길래 보니까 담은 걸 0으로 안 만들어줘서 계속 같은 것만 담고 있었음, 담고 나면 또 안 담게 0으로 만들어줌