def solution(board):
    answer = float('inf')
    dy = [1, -1, 0, 0]
    dx = [0, 0, -1, 1]
    queue = deque()
    queue.append((0,0,0,''))
    board[0][0] = 1
    INF = float('inf')
    cost_check = [[INF] * len(board) for _ in range(len(board))]
    cost_check[0][0] = 0

    while queue:
        cost,y,x,dr = queue.popleft()
        if y == (len(board)-1) and x == (len(board)-1):
            if cost <= answer:
                answer = cost

        for i in range(4):
            newY = y + dy[i]
            newX = x + dx[i]
            dr_path = ''
            if 0 <= newY < len(board) and 0 <= newX < len(board):
                if board[newY][newX] != 0:
                    continue
                else:
                    if dr == 'R' or dr == 'D':
                        if dr == 'R' and abs(y-newY) == 1:
                            if cost + 600 <= cost_check[newY][newX]:
                                cost_check[newY][newX] = cost + 600
                                queue.append((cost+600,newY,newX,'D'))
                        elif dr == 'D' and abs(y-newY) == 1:
                            if cost + 100 <= cost_check[newY][newX]:
                                cost_check[newY][newX] = cost + 100
                                queue.append((cost+100,newY,newX,dr))
                        elif dr == 'D' and abs(x-newX) == 1:
                            if cost + 600 <= cost_check[newY][newX]:
                                cost_check[newY][newX] = cost + 600
                                queue.append((cost+600,newY,newX,'R'))
                        elif dr == 'R' and abs(x-newX) == 1:
                            if cost + 100 <= cost_check[newY][newX]:
                                cost_check[newY][newX] = cost + 100
                                queue.append((cost+100,newY,newX,dr))
                    else:
                        if abs(y-newY) == 1:
                            dr = 'D'
                            if cost + 100 < cost_check[newY][newX]:
                                cost_check[newY][newX] = cost + 100
                                queue.append((cost+100,newY,newX,dr))
                            dr = ''
                        if abs(x-newX) == 1:
                            dr = 'R'
                            if cost + 100 < cost_check[newY][newX]:
                                cost_check[newY][newX] = cost + 100
                                queue.append((cost+100,newY,newX,dr))
                            dr = ''

    return answer

from collections import deque