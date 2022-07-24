from random import *

def answer():

    while True:

        t = input().lower()

        if t == 'да':
            return True

        elif t == 'нет':
            return False

def is_valid(a):

    if len(a) < 1:
        return False

    for i in range(len(a)):
        if a[i] not in '1234567890':
            return False
    return True

print('Игра в угадывание чисел')

while True:
    try_counter = 0
    n = 100
    print('Желаете изменить правую границу максимальной величины случайного числа(да/нет)?')

    while True:

        if answer():
            print('Введите желаемое число от двух включительно')
            while True:
                t = input()
                if is_valid(t):
                    if int(t) >= 2:
                        n = int(t)
                        break
        break

    print('Игра будет произведена в промежутке:\n[1;' + str(n) + ']')

    rand_num = randint(1, n)

    while True:
        num = ''
        while True:
            num = input()
            if is_valid(num):
                if 1 <= int(num) <= n:
                    num = int(num)
                    break
            print('А может быть введёте число от 1 до', n, '?')

        if num > rand_num:
            print('Слишком много, попробуйте еще раз')
            try_counter += 1
            continue

        elif num < rand_num:
            print('Слишком мало, попробуйте еще раз')
            try_counter += 1
            continue

        else:
            print('Вы угадали, поздравляем!\n Количество попыток:\n' + str(try_counter))
            break

    print('Сыграть снова(да/нет)?')

    if answer():
        continue
    break


