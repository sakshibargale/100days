from collections import defaultdict

# Read n and m
n, m = map(int, input().split())

# Default dictionary to store positions
d = defaultdict(list)

# Read group A words and store their positions (1-indexed)
for i in range(1, n + 1):
    word = input().strip()
    d[word].append(i)

# Read group B words and print results
for _ in range(m):
    word = input().strip()
    if word in d:
        print(*d[word])
    else:
        print(-1)