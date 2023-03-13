your_list = ['2018-01-01', 'yandex', 'cpc', 100]
my_list = [1, 2 , '4ff', 192.44, '168.0.2.5', 'первый ключ', 'первое значение' ]


def dict_maker(list):
    my_dict = {list[-2]: list[-1]}
    for i in list[-3::-1]:
        my_dict = {i: my_dict}
    return my_dict


print(dict_maker(your_list))
print('\n')
print(dict_maker(my_list))