
yourMoney = int(input('Введите количество денег: '))

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
