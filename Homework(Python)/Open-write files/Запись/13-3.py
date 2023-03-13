import os


def write_file(path: str):
    path = '/Users/roman/Vs-Code/Netology(Python)/Homework/Open-write files/Запись/'
    files_list = os.listdir(path)
    file_comparison = {}
    for file in files_list:
        if file.rfind('.txt', -4) >= 0:
            f_string = []
            with open(os.path.join('/Users/roman/Vs-Code/Netology(Python)/Homework/Open-write files/Запись/' ,file), encoding='utf-8') as f:
                for string in f:
                    f_string.append(string)
            file_comparison[file] = f_string

    with open('/Users/roman/Vs-Code/Netology(Python)/Homework/Open-write files/Запись/result/result.txt', 'w') as result:
        for file_name, row in sorted(file_comparison.items(), key=lambda x: len(x[1])):
            result.write('имя файла: ' + file_name + '\n')
            result.write('кол-во строк: ' + str(len(row)) + '\n')
            if '\n' not in row:
                row += '\n\n'
            result.writelines(row)
            
    return file_comparison


print(write_file('/Users/roman/Vs-Code/Netology(Python)/Homework/Open-write files/Запись'))
print(write_file('Netology(Python)/Homework/Open-write files/Запись/'))




# from glob import glob

# text_list = []

# for text_file in glob('[0-3].txt'):
#     with open(text_file, 'r', encoding='utf-8') as text:
#         data_from_text = text.read()
#         splitted_text = data_from_text.split('\n')
#         text_list.append((len(splitted_text), text_file, data_from_text))
#         text_list.sort()

# with open('res.txt', 'w', encoding='utf-8') as res_file:
#     for length, name, strings in text_list:
#         res_file.write(name + '\n')
#         res_file.write(str(length) + '\n')
#         res_file.writelines(strings + '\n\n')

# _______________________________

# file_comparison = {}

# # file_names = ['1.txt', '2.txt', '3.txt']

# for file in glob('[0-3].txt'):
#     print(file)
#     f_string = []
#     with open(file) as f:
#         for string in f:
#             f_string.append(string)
#         file_comparison[file] = f_string

#     sorted_tuple = sorted(file_comparison.items(), key=lambda x: len(x[1]))
#     file_comparison = dict(sorted_tuple)

# with open('result.txt', 'w') as result:
#     for file_name, row in sorted(file_comparison.items(), key=lambda x: len(x[1])):
#         result.write('имя файла: ' + file_name + '\n')
#         result.write('кол-во строк: ' + str(len(row)) + '\n')
#         if '\n' not in row:
#             row += '\n\n'
#         result.writelines(row)

# print(file_comparison)





# file_comparison = {}

# with open('1.txt') as f1:
#     string_count_f1 = 0
#     string_f1 = []
#     for string in f1:
#         string_count_f1 += 1
#         string_f1.append(string)
#     file_comparison[string_count_f1] = {'1.txt': string_f1}

# with open('2.txt') as f2:
#     string_count_f2 = 0
#     string_f2 = []
#     for string in f2:
#         string_count_f2 += 1
#         string_f2.append(string)
#     file_comparison[string_count_f2] = {'2.txt': string_f2}

# with open('3.txt') as f3:
#     string_count_f3 = 0
#     string_f3 = []
#     for string in f3:
#         string_count_f3 += 1
#         string_f3.append(string)
#     file_comparison[string_count_f3] = {'3.txt': string_f3}

#     # print(file_comparison)

#     sorted_tuple = sorted(file_comparison.items(), key=lambda x: x[0])
#     file_comparison = dict(sorted_tuple)

# print(file_comparison)

# with open('result.txt', 'w') as result:
#     for i, j in file_comparison.items():
#         result.write('кол-во строк: ' + str(i) + '\n')
#         for x in j:
#             result.write(str(x) + '\n')
#             result.writelines(j[x])
#             result.write('\n')

