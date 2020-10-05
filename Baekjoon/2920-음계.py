melody = list(map(int, input().split()))
last = len(melody) - 1
answer = ''
for index, note in enumerate(melody):
    if index != last:
        if melody[index] - melody[index+1] == -1:
            answer = 'ascending'
        elif melody[index] - melody[index+1] == 1:
            answer = 'descending'
        else:
            answer = 'mixed'
            break

print(answer)