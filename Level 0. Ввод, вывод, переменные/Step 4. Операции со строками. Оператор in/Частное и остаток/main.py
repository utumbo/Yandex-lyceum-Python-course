num1 = int(input())
num2 = int(input())
num3 = int(input())

result = False

if (num1 % 7 == num2 // 2) or (num2 % 7 == num1 // 2):
    result = True
elif (num1 % 7 == num3 // 2) or (num3 % 7 == num1 // 2):
    result = True
elif (num2 % 7 == num3 // 2) or (num3 % 7 == num2 // 2):
    result = True

print(result)

"""
Для трёх введённых чисел определите, есть ли среди них такая пара, 
что остаток от деления на 7 одного числа равен целой части от деления на 2 другого числа? 
Если такая пара есть, выведите True, если нет, то False.
"""