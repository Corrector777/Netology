from pprint import pprint


def cook():
    with open('recipes.txt') as recipes: 
        cook_book = {}  
        for dish in recipes:
            ingridients_list = []
            dish_name = str(dish.strip())
            ingridients_count = int(recipes.readline().strip())
            for i in range(ingridients_count):
                ingridients = recipes.readline()
                ingridient_name, quantity, measure = ingridients.strip().split('|')
                ingridients_dict = {'ingridient_name': ingridient_name,
                                    'quantity': int(quantity),
                                    'measure': measure}
                ingridients_list.append(ingridients_dict)
            cook_book[dish_name] = ingridients_list
            recipes.readline()
    return cook_book
# pprint(cook_book)


def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for dish in dishes:
        cook_book = cook()      
        if dish in cook_book:
            for i in cook_book[dish]:
                name = i['ingridient_name']
                quantity = int(i['quantity']) * person_count     
                if i['ingridient_name'] in shop_list:
                    shop_list[name]['quantity'] += quantity   
                else:
                    shop_list[name] = {'measure': i['measure'],
                                       'quantity': quantity}

    return shop_list


pprint(get_shop_list_by_dishes(['Омлет', 'Запеченный картофель'], 2))