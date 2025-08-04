initial_height = int(input())
height_mountain = int(input())
step = int(input())

heights = []

current_height = initial_height
while current_height <= height_mountain:
    heights.append(current_height)
    current_height += step

current_height = height_mountain - (step + 1)
while current_height >= initial_height:
    heights.append(current_height)
    current_height -= (step + 1)


if heights[-1] != initial_height:
    heights.append(initial_height)

print(" ".join(map(str, heights)))

"""
Подъём в горы — это трудная задача, а вот спускаться легче, можно двигаться быстрее. Напишите программу, которая покажет, как проходит восхождение в горы и спуск.

Формат ввода
Вводятся три числа: начальная высота, высота горы и шаг, с которым мы можем двигаться при восхождении.

Формат вывода
В одну строку через пробел выведите высоты: сначала при восхождении от начальной до конечной с указанным шагом, затем при спуске: от высоты горы до начальной с шагом, на 1 большим того, что был при подъёме.
"""