length = int(input())
height = int(input())
width = int(input())
botls = int(input())

cube = length * height * width

if cube % botls == 0:
    botls_need = cube // botls
elif cube % botls != 0:
    botls_need = (cube // botls) + 1

print(botls_need)

"""
В новый аквариум нужно налить чистой воды. Напишите программу, которая определит,
 сколько бутылок воды нужно купить, чтобы заполнить аквариум полностью.
"""