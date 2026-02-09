m = int(input())
setA = set(map(int, input().split()))

n = int(input())
setB = set(map(int, input().split()))

result = sorted(setA.symmetric_difference(setB))

for i in result:
    print(i)
