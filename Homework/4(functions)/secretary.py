documents = [
        {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
        {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
        {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"},
        {"type": "driver license", "number": "5455 028765", "name": "Василий Иванов"},
      ]

directories = {
        '1': ['2207 876234', '11-2', '5455 028765'],
        '2': ['10006'],
        '3': []
      }


# def get_name(doc_number):
#     for dic_document in documents:        
#         if doc_number in dic_document["number"]:
#             return dic_document['name']
#     return 'Документ не найден'
       

# def get_directory(doc_number):
#     for shelf, document_on_shelf in directories.items():
#         if doc_number in document_on_shelf:
#             return shelf
#     return 'Полки с таким документом не найдено'


def add(document_type, number, name, shelf_number):
    new_document_dict = {'type': document_type, 'number': number, 'name': name}
    documents.append(new_document_dict)
    if shelf_number in directories:
        directories[shelf_number].append(number)
    else:
        directories[shelf_number] = [number]
            
            

add('international passport', '311 020203', 'Александр Пушкин', '1')
print(directories, end='_____')
print()
# print(documents)
    

# # не меняйте эту часть программы
# # проверка работы реализованных функций
# # print(get_name('10006'))
# print(get_directory("11-2"))
# # print(get_name("11-2"))
# # add('international passport', '311 020203', 'Александр Пушкин', 3)
# print(get_directory("10006"))
# # print(get_name("311 020203"))
# print(get_directory("311 020204"))