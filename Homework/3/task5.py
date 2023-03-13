from pprint import pprint

geo_logs = [
    {'visit1': ['Москва', 'Россия']},
    {'visit2': ['Дели', 'Индия']},
    {'visit3': ['Владимир', 'Россия']},
    {'visit4': ['Лиссабон', 'Португалия']},
    {'visit5': ['Париж', 'Франция']},
    {'visit6': ['Лиссабон', 'Португалия']},
    {'visit7': ['Тула', 'Россия']},
    {'visit8': ['Тула', 'Россия']},
    {'visit9': ['Курск', 'Россия']},
    {'visit10': ['Архангельск', 'Россия']}
]

# x = list()
# # print(x)
# for i in geo_logs:
#     # print(i)
#     # input()
#     for j in i.values():
#         # print(j)
#         if 'Россия' in j:
#             x.append(i)
# pprint(x)

# print(f'\nid = {id(geo_logs)}\n')

# COUNTRY = 'Россия'

# for index, geo_log in enumerate(list(geo_logs)):
#     visit_value = list(geo_log.values())[0]
#     if COUNTRY not in visit_value:
#         geo_logs.remove(geo_log)
# pprint(geo_logs)
# print(f'\nid = {id(geo_logs)}\n')


# Вариант 2
# print(f'\nid= {id(geo_logs)}\n')
# for elem in geo_logs[:]:
#     for value in elem.values():
#         print(COUNTRY in value)
#         if COUNTRY not in value:
#             geo_logs.remove(elem)
# print(geo_logs)
# print(f'\nid= {id(geo_logs)}\n')


# Вариант 3
# print(f'\nid= {id(geo_logs)}\n')
# temp = []
# for index in range(len((geo_logs))):
#     for key in geo_logs[index]:
#         if 'Россия' in geo_logs[index][key]:
#             temp.append(geo_logs[index])
# geo_logs = temp
# print(geo_logs)
# print(f'\nid= {id(geo_logs)}\n')
