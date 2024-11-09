def possible_grid_dimensions(c1, c2):
    diff = abs(ord(c1) - ord(c2))
    factors = []
    for i in range(1, int(diff**0.5) + 1):
        if diff % i == 0:
            factors.append((i, diff // i))
            factors.append((diff // i, i))

    valid_dimensions = []
    for rows, cols in factors:
        # Ensure both characters can fit in the same row
        if cols >= max(ord(c1) % cols, ord(c2) % cols):
            valid_dimensions.append((rows, cols))

    valid_dimensions.sort()
    for rows, cols in valid_dimensions:
        print(rows, cols)

T = int(input())
for _ in range(T):
    c1, c2 = input().split()
    possible_grid_dimensions(c1, c2)
    print()