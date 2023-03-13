queries = [
  'смотреть сериалы онлайн',
  'новости спорта',
  'афиша кино',
  'курс доллара',
  'сериалы этим летом',
  'курс по питону',
  'сериалы про спорт',
  're',
  'rr',
  'dd dd dd dd dd',
  'ee eee ee e e',
]

number_of_querries = len(queries)
my_dict = {}
for query in queries:
    words_count = (len(query.split()))
    if words_count in my_dict:
        my_dict[words_count] += 1
    else:
        my_dict[words_count] = 1

for count, value in sorted(my_dict.items()):
    print(f'Запросов из {count} слов = {value} раз(а)\
           или  {value / number_of_querries :.2%}')