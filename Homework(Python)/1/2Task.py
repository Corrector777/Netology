# Полный список:
# 21 марта – 20 апреля Овен
# 21 апреля – 21 мая Телец
# 22 мая – 21 июня Близнецы
# 22 июня – 22 июля Рак
# 23 июля – 23 августа Лев
# 24 августа – 22 сентября Дева
# 23 сентября – 22 октября Весы
# 23 октября – 22 ноября Скорпион
# 22 ноября – 21 декабря Стрелец
# 22 декабря – 20 января Козерог
# 21 января – 19 февраля Водолей
# 20 февраля – 20 марта Рыбы.
while True:
    month = input('введите месяц: ')
    if month == 'стоп':
        break
    date = int(input('введите число: '))
    zodiak = ''
    if month.lower() == 'январь':
        if 1 <= date <= 20:
            zodiak = 'Козерог'
        if 21 <= date <= 31:
            zodiak = 'Вололей'

    elif month.lower() == 'февраль':
        if 1 <= date <= 19:
            zodiak = 'Водолей'
        if 20 <= date <= 29:
            zodiak = 'Рыбы'

    elif month.lower() == 'март':
        if 1 <= date <= 20:
            zodiak = 'Рыбы'
        if 21 <= date <= 31:
            zodiak = 'Овен'

    elif month.lower() == 'апрель':
        if 1 <= date <= 20:
            zodiak = 'Овен'
        if 21 <= date <= 30:
            zodiak = 'Телец'

    elif month.lower() == 'май':
        if 1 <= date <= 21:
            zodiak = 'Телец'
        if 22 <= date <= 31:
            zodiak = 'Близнец'

    elif month.lower() == 'июнь':
        if 1 <= date <= 21:
            zodiak = 'Близнец'
        if 22 <= date <= 30:
            zodiak = 'Рак'

    elif month.lower() == 'июль':
        if 1 <= date <= 22:
            zodiak = 'Рак'
        if 23 <= date <= 31:
            zodiak = 'Лев'

    elif month.lower() == 'август':
        if 1 <= date <= 23:
            zodiak = 'Лев'
        if 24 <= date <= 30:
            zodiak = 'Дева'

    elif month.lower() == 'сентябрь':
        if 1 <= date <= 23:
            zodiak = 'Дева'
        if 24 <= date <= 31:
            zodiak = 'Весы'

    elif month.lower() == 'октябрь':
        if 1 <= date <= 22:
            zodiak = 'Весы'
        if 23 <= date <= 30:
            zodiak = 'Скорпион'

    elif month.lower() == 'ноябрь':
        if 1 <= date <= 22:
            zodiak = 'Скорпион'
        if 23 <= date <= 30:
            zodiak = 'Стрелец'

    elif month.lower() == 'декабрь':
        if 1 <= date <= 21:
            zodiak = 'Стрелец'
        if 22 <= date <= 31:
            zodiak = 'Козерог'

    else:
        print('Введены некорректные данные. Попробуйте еще раз')
        break
    print(f'ваш знак зодиака: {zodiak}')
    answer = input('продолжаем?(да/нет)')

    if answer.lower() == 'да':
        continue
    else:
        break
