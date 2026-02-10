from itertools import permutations

# Take input
S, k = input().split()
k = int(k)

# Sort the string to maintain lexicographic order
S = sorted(S)

# Generate and print permutations
for p in permutations(S, k):
    print(''.join(p))