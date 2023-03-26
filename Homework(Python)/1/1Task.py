# far_eastern_district = [
#   'Амурский Край', 'Бурятия', 'Еврейская автономная область',
#   'Камчатский край', 'Хабаровский край'
# ]
# far_eastern_district = [subject.lower() for subject in far_eastern_district]

# base_rate = 5  # базовая ставка
# print(f'текущая ставка : {base_rate}')
# federal_subject = input('Введите Субъект Федерации: ')  # выбрать согласно списку
# if federal_subject.lower() in far_eastern_district:
#     base_rate = 2
#     print(f' ваша базовая ставка : {base_rate}%')
# else:
#     number_of_children = int(input('Введите кол-во детей: '))
#     salary_project = input('Уточните наличие зарплатного проекта (Да/ Нет): ')
#     bank_insurance = input('Уточните наличие страховки нашего банка (Да/ Нет): ')

#     if number_of_children >= 3:
#         base_rate -= 1
#         if salary_project.lower() == 'да':
#             base_rate -= 0.5
#         if bank_insurance.lower() == 'да':
#             base_rate -= 1.5

#     elif salary_project.lower() == 'да':
#         base_rate -= 0.5
#         if bank_insurance.lower() == 'да':
#             base_rate -= 1.5

#     elif bank_insurance.lower() == 'да':
#         base_rate -= 1.5

#     print(f' ваша базовая ставка : {base_rate}%')
x = 7
for i in range(13):
    print(i)
    if 8:
        break
