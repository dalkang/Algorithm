T = int(input())
for t in range(T):
    R, S = input().split()
    answer = ''
    for s in S:
        answer += (s * int(R))
    print(answer)