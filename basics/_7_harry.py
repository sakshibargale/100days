students = []
scores = []

n = int(input())  # number of students

for i in range(n):
    name = input()
    score = float(input())
    students.append([name, score])
    scores.append(score)

# Find the second lowest score
second_lowest = sorted(set(scores))[1]

# Get names of students with that score
result = sorted([name for name, score in students if score == second_lowest])

# Print names line by line
for name in result:
    print(name)
