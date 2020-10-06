numbers = [int(input()) for i in range(3)]
multiple = 1
arr = [0] * 10

for number in numbers:
    multiple *= number

for num in str(multiple):
    arr[int(num)] += 1

for n in arr:
    print(n)