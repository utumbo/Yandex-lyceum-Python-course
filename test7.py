a = [2, 2, 3]
b = [5, 4, 1]

total_a = a[0] * a[1] * a[2]
total_b = b[0] * b[1] * b[2]

if total_a > total_b:
    return total_a - total_b
elif total_a < total_b:
    return total_b - total_a