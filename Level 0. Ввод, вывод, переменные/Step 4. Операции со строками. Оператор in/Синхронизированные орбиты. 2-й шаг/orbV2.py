orbit1 = int(input())
orbit2 = int(input())

result = 'Орбиты не синхронизированы.'

if orbit1 % 9 == 0 and orbit2 % 9 == 0:
    divisor = 9
elif orbit1 % 8 == 0 and orbit2 % 8 == 0:
    divisor = 8
elif orbit1 % 7 == 0 and orbit2 % 7 == 0:
    divisor = 7
elif orbit1 % 6 == 0 and orbit2 % 6 == 0:
    divisor = 6
elif orbit1 % 5 == 0 and orbit2 % 5 == 0:
    divisor = 5
elif orbit1 % 4 == 0 and orbit2 % 4 == 0:
    divisor = 4
elif orbit1 % 3 == 0 and orbit2 % 3 == 0:
    divisor = 3
elif orbit1 % 2 == 0 and orbit2 % 2 == 0:
    divisor = 2
else:
    divisor = None

if divisor is not None:
    part1 = orbit1 / divisor
    part2 = orbit2 / divisor
    result = f"Орбиты относятся как {part1}:{part2}."

print(result)

"""
Напишите программу, которая проверит, синхронизированы ли между собой орбиты двух планет, что означает: есть ли такое число от 2 до 9, на которое можно разделить обе орбиты?

Если есть, то для наибольшего такого числа ваша программа должна вывести фразу:
Орбиты относятся как <число1>:<число2>.

В этой строке <число1> означает целую часть от деления большего из чисел на найденный делитель, а <число2> — целую часть от деления на найденный делитель оставшегося числа.

Если такого делителя найти не удалось, то выведите:
Орбиты не синхронизированы.
"""