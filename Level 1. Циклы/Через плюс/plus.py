numbers = []

while True:
    numb = int(input())

    if numb > 4:
        break
    numbers.append(numb)

print(numbers, sep='+')
"""
Напишите программу для вывода четырёх цифр числа через плюс.

Формат ввода
Вводятся числа, пока не будет введено число с количеством разрядов, большим четырёх.

Формат вывода
Выводите все 4 разряда каждого числа, разделяя их символом +. Нулевые разряды тоже выводите.
"""