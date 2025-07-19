n = int(input())
if n % 3 == 0:
   n = n // 3
elif n % 2 == 0:
   n = n // 2
else:
   n = n - 1
print(n)