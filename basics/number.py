from collections import defaultdict

n, m = map(int, input().split())

d = defaultdict(list)

# Group A
for i in range(1, n + 1):
    word = input()
    d[word].append(i)

# Group B
for i in range(m):
    word = input()
    if word in d:
        print(*d[word])
    else:
        print(-1)
