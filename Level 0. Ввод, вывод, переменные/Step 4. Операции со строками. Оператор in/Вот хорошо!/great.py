gift = input().lower()

candies = 'конфета' in gift or 'конфеты' in gift or 'конфету' in gift or 'торт' in gift or 'конфетки' in gift
books = 'книга' in gift or 'книги' in gift or 'книгу' in gift or 'книг' in gift
bike_or_scooter = 'велосипед' in gift or 'велосипеды' in gift or 'самокат' in gift or 'самокаты' in gift

if candies and books and bike_or_scooter:
    print('Вот хорошо!')
else:
    print('Не все.')


"""
Мама считает, что дарить мне конфеты — плохо. Лучше подарить книгу. 
Папа согласен, что получить в подарок велосипед или самокат — это здорово! 
А я думаю, что хорошо бы получить и конфеты (а лучше набор конфет, ну или хотя бы одну конфету), 
и книгу или книги в любой форме, и велосипед или самокат.

Напишите программу, которая проверит, есть ли все желаемые подарки во введённой строке. 
Если есть все, то выведите:
Вот хорошо!

Если не все, то выведите:
Не все.
"""