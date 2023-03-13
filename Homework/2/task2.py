cook_book = [
  ['салат',
      [
        ['картофель', 100, 'гр.'],
        ['морковь', 50, 'гр.'],
        ['огурцы', 50, 'гр.'],
        ['горошек', 30, 'гр.'],
        ['майонез', 70, 'мл.'],
      ]
   ],
  ['пицца',
      [
        ['сыр', 50, 'гр.'],
        ['томаты', 50, 'гр.'],
        ['тесто', 100, 'гр.'],
        ['бекон', 30, 'гр.'],
        ['колбаса', 30, 'гр.'],
        ['грибы', 20, 'гр.'],
      ],
   ],
  ['фруктовый десерт',
      [
        ['хурма', 60, 'гр.'],
        ['киви', 60, 'гр.'],
        ['творог', 60, 'гр.'],
        ['сахар', 10, 'гр.'],
        ['мед', 50, 'мл.'],
      ]
   ]
]

# for dish in range(len(cook_book)):
#     dish_name = (cook_book[dish][0])
#     print(dish_name)
#     for recipe in range(len(cook_book[dish][1])):
#         dish_ingridients = cook_book[dish][1]
#         print(dish_ingridients[recipe][0], end=',')
#         print(dish_ingridients[recipe][1], end=',')
#         print(dish_ingridients[recipe][2])


# print(cook_book[0][1])
persons_count = int(input('Введите кол-во персон: '))


# for dish in range(len(cook_book)):
#   print(f'\n{cook_book[dish][0].capitalize()}:')
#   for i in range(len(cook_book[dish][1])):
#     print(f'{cook_book[dish][1][i][0]}')
#      print(f'{cook_book[dish][1][i][0]}, '
#               f'{cook_book[dish][1][i][1] * persons_count}'
#               f'{cook_book[dish][1][i][2]}')
        


# persons_count = int(input('Введите кол-во персон: '))

for dish in cook_book:
    # print(dish)
    print(f'\n{dish[0].capitalize()}:')
    for i in dish[1]:
      # print(i)
      print(f'{i[0]}, '
            f'{i[1] * persons_count}'
            f'{i[2]}')



# print('Салат:')
# for i in range(len(cook_book[0][1])):
#     print(f'{cook_book[0][1][i][0]}, {cook_book[0][1][i][1] * persons_count}'
#           f'{cook_book[0][1][i][2]}')

# print('''Пицца:''')
# for i in range(len(cook_book[0][1])):
#     print(f'{cook_book[1][1][i][0]}, {cook_book[1][1][i][1] * persons_count}'
#           f'{cook_book[1][1][i][2]}')

# print('\nФруктовый десерт:')
# for i in range(len(cook_book[0][1])):
#     print(f'{cook_book[2][1][i][0]}, {cook_book[2][1][i][1] * persons_count}'
#           f'{cook_book[2][1][i][2]}')
