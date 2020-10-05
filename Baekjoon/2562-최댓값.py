numbers = [int(input()) for i in range(9)]
max_num = max(numbers)
max_index = numbers.index(max(numbers)) + 1

print(max_num)
print(max_index)
