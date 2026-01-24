def print_rangoli(size):
    import string
    alpha = string.ascii_lowercase

    width = 4 * size - 3
    lines = []

    # Top half (including middle)
    for i in range(size):
        left = alpha[size-1:i:-1]
        center = alpha[i]
        right = alpha[i+1:size]
        row = "-".join(left + center + right)
        lines.append(row.center(width, "-"))

    # Bottom half
    for i in range(size-2, -1, -1):
        left = alpha[size-1:i:-1]
        center = alpha[i]
        right = alpha[i+1:size]
        row = "-".join(left + center + right)
        lines.append(row.center(width, "-"))

    print("\n".join(lines))


# Input
n = int(input())
print_rangoli(n)