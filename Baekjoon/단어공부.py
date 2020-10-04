words = input()
lower = list(words.upper())
key = set(lower)
max_key = 0
max_word = ''
for k in key:
    path = lower.count(k)
    if max_key < path:
        max_key = path
        max_word = k
    elif max_key == path:
        max_word = '?'
print(max_word)