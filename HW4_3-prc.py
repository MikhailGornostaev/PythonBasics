import re

yourMoney = (input('Введите количество денег: '))

if yourMoney.startswith('-'):
    print('Введите положительное число.')
elif re.search(r'[!@#$%^&*()\[=+;\'{}\"/A-Za-z]', yourMoney):
    print('Вы ввели не число.')
elif yourMoney == '':
    print('Вы ввели пустое поле. Введите число.')
else:
    yourMoney = int(float(yourMoney))

    print('Ты ввёл', yourMoney, '(RUB)')

    toUsd = yourMoney / 73
    toEur = yourMoney / 86
    toChf = yourMoney / 79
    toGbp = yourMoney / 101
    toCny = yourMoney / 11

    print('Конвертированная сумма в USD =', int(toUsd))
    print('Конвертированная сумма в EUR =', int(toEur))
    print('Конвертированная сумма в CHF =', int(toChf))
    print('Конвертированная сумма в GBP =', int(toGbp))
    print('Конвертированная сумма в CNY =', int(toCny))
