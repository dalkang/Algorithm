T = int(input())

for t in range(1, T+1):
    N = int(input())
    check = []
    i = 1
    while len(check) != 10:
        path = list(str(N * i))
        for p in path:
            if p not in check:
                check.append(p)
        i += 1

    print("#%d %d" % (t, N*(i-1)))        