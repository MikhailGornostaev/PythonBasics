yourMoney = int(input('Введите количество денег: '))
courseUsd = int(input('Введите текущий курс доллара: '))
toUsd = yourMoney/courseUsd
print('Ты ввел '+str(yourMoney)+' (рублей)')
print('Конвертированная сумма в USD = ' + str(int(toUsd)))
