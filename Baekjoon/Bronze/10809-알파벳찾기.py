word = input()
alphabet = [-1] * 26
for i in word:
    alphabet[ord(i) - 97] = word.find(i)

print(*alphabet)