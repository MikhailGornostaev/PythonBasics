import random

num = int(input('Введите целое число'))

someNumber1 = random.randint(1, 100)
someNumber2 = random.randint(1, 100)

# result check
# print(someNumber1, someNumber2)

if num == someNumber1 and num == someNumber2:
    print('Введенное число равно двум сгенерированным числам')
elif num > someNumber1 and num > someNumber2:
    print('Введенное число больше первого и второго введенных чисел')
elif num < someNumber1 and num < someNumber2:
    print('Введенное число меньше первого и второго введенных чисел')
elif someNumber1 < num < someNumber2:
    print('Введенное число больше первого сгенерированного числа, но меньше второго')
else:
    print('Введенное число больше второго сгенерированного числа, но меньше первого')
