minimum = 0

num = int(input())

while num >= 0:
    minimum = min(minimum, num)
    num = int(input())

print(minimum)