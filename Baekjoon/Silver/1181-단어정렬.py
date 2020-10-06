N = int(input())
words = [input() for i in range(N)]
words.sort()
words.sort(key=len)
answer = []
for word in words:
    if word not in answer:
        answer.append(word)
        print(word)