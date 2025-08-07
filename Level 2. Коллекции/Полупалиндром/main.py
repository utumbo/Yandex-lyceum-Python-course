def find_half_palindrome_index(s):
    left = 0
    right = len(s) - 1
    
    while left < right:
        if s[left] == s[right]:
            left += 1
            right -= 1
        else:
            return left
    
    return len(s)

input_string = input().strip()
index = find_half_palindrome_index(input_string)
print(index)

"""
Палиндром — это строка, которая читается одинаково с начала и с конца. 
А вот если сперва строка похожа на палиндром, но, начиная с какой-то буквы, 
перестаёт быть палиндромом, то назовём её полупалиндромом.

Найдите индекс символа, начиная с которого строка перестаёт быть палиндромом.

Формат ввода
Вводится строка.

Формат вывода
Выведите ответ на задачу.

Пример
Ввод	Вывод
drawbackward
4
"""