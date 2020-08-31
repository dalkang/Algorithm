arr = [list(map(int, input().split(' '))) for _ in range(10)]
dy = [0, 1]
dx = [1, 0]
stack = [(1,1)]

while stack:
    y,x = stack.pop()
    if arr[y][x] == 2:
        arr[y][x] = 9
        break
    else:
        arr[y][x] = 9
        
    for i in range(2):
        newY = y + dy[i]
        newX = x + dx[i]
        if 0 <= newY < 10 and 0 <= newX < 10:
            if arr[newY][newX] == 0:
                arr[newY][newX] = 9
                stack.append((newY,newX))
                break
            elif arr[newY][newX] == 2:
                arr[newY][newX] = 9
                break

for j in range(10):
    for k in range(10):
        print(arr[j][k], end=' ')
    print()