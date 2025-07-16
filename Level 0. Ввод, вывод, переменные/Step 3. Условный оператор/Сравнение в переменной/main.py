import math

n = int(input())
sqrt_n = int(math.sqrt(n))

if sqrt_n * sqrt_n == n:
    print("Квадрат")
else:
    print("Не квадрат")