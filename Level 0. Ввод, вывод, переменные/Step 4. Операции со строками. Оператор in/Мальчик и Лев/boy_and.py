str = input()

substring_boy = "мальчик"
substring_lione = 'лев'
oshibka = 'Из рассказа Лев узнал, что лев - это хищное животное.'
oshibka2 = 'В зоопарке Лев узнал, что скоро у них будет лев Вася.'

if substring_boy in str and substring_lione not in str:
    print('Мальчик есть, льва нет.')

if substring_lione in str and substring_boy not in str:
    print('Есть лев, мальчика нет.')
else:
    print('Лев, беги!')

if str == oshibka or oshibka2:
    print('Лев, беги!')

# в задании были допущены 2 логические ошибки