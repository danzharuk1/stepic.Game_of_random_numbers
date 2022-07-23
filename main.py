from random import *

rand_num = randint(1, 100)

print('Игра в угадывание чисел')

while True:

    num = int(input())

    if num > rand_num:
        print('Слишком много, попробуйте еще раз')
        continue

    elif num < rand_num:
        print('Слишком мало, попробуйте еще раз')
        continue

    else:
        break

print('Вы угадали, поздравляем!')