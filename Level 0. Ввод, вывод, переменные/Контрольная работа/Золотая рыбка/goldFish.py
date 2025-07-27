text_gold_fish = input()
numb_str = int(input())

if 'gold' in text_gold_fish and len(text_gold_fish) >= numb_str:
    print('A goldfish!')
elif 'gold' in text_gold_fish or len(text_gold_fish) >= numb_str:
    print('Only one thing!')
else:
    print("Either it's not a fish, or it's not a golden one.")

"""
В аквариум хочется поселить рыбку, и не простую, а золотую. 
А чем золотая рыбка отличается от не золотой? Правильно, длинным хвостом и золотым цветом.

Напишите программу, которая выведет, можно ли считать введённое описание рыбки подходящим или нет.

Формат ввода
Вводится строка с описанием рыбки, а затем число – наименьшая длина хвоста (строки) у золотой рыбки.

Формат вывода
Если в описании есть подстрока gold, а длина строки не меньше введённого числа, то выведите:
A goldfish!

Если выполняется только одно из условий, то выведите:
Only one thing!

Если не выполняется ни одно, то выведите:
Either it's not a fish, or it's not a golden one.
"""