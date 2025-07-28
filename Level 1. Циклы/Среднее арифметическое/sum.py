res = 0.0
count = 0

while True:
    numb = float(input())

    if numb == -1:
        break
    else:
        res += numb
        count += 1

if count > 0:
    average = res / count
    print(average)

"""
Вводятся числа, пока не будет введено число -1 
(-1 в подсчётах не участвует, служит только признаком окончания ввода).
"""