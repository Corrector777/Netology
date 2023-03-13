def discriminant(a, b, c):	
    discriminant_value = b ** 2 - 4 * a * c
    return discriminant_value


def solution(a, b, c):
    discriminant_func = discriminant(a, b, c)
    if discriminant_func > 0:
        x_1 = round((b*(-1) - discriminant_func ** (0.5)) / (2 * a), 1)
        x_2 = round((b*(-1) + discriminant_func ** (0.5)) / (2 * a), 1)
        anwser =(x_1, x_2)
        print(*sorted(anwser))
    elif discriminant_func == 0:
        x_1 = b * (-1) / (2 * a)
        print(x_1)
    else:
        print('корней нет')  


# не меняйте эту часть программы
# вывод решения для коэфициентов, заданных в условии задачи
solution(-1, -2, 15)  
solution(1, -13, 12)  
solution(-4, 28, 4) 
solution(1, 1, 1)  