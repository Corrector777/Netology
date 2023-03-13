boys = ['Peter', 'Alex', 'John', 'Arthur', 'Richard']
girls = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha', '1']
boys.sort()
girls.sort()
if len(boys) == len(girls):
    for boy_name, girl_name in zip(boys, girls):
        print(f'{boy_name} и {girl_name}')

else:
    print('Кто-то может остаться без пары! Спаривание невозможно:)')