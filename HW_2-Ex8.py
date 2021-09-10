import random

num = int(input('Введите целое число'))
someNumber = random.randint(1, 100)

if num <= someNumber:
    if num == someNumber:
        print('Введенное число равно сгенерированному числу')
    else:
        print('Введенное число меньше сгенерированного числа')
else:
    print('Введенное число больше сгенерированного числа')
