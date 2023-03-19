import time
from datetime import datetime, timedelta
import requests


def actual_date():  # Определяем функцию где будем получать текущее время
    current_date = datetime.today() - timedelta(days=2)  # Из текущей даты отнимаем два дня
    return current_date.strftime('%Y-%m-%d')  # Преобразуем дату в удобный формат


def convert_date_from_timestamp(data):  # Определяем функцию, которая преобразует timestamp в удобный вид
    current_date = datetime.fromtimestamp(data)  # Передаем timestamp, получаем дату с временем и сохраняем в переменную
    return current_date  # Возвращаем данные


def request_overflow(page):  # Определяем функцию, которая выполняет запрос. На вход функция принимает номер страницы
    headers = {'Accept': 'application/json',
               'Connection': 'keep-alive'}

    params = {
        'key': 'U4DMV*8nvpm3EOpvf69Rxw((',
        'site': 'stackoverflow',
        'fromdate': '1678924800',
        'todate': '1679097600',
        'order': 'desc',
        'sort': 'creation',
        'tagged': 'python',
        'page': page,
        }
    url = 'https://api.stackexchange.com/2.3/questions'

    response = requests.get(url=url, headers=headers, params=params)
    response.raise_for_status()
    return response.json()


def response_result():  # Определяем функцию, где будем выводить на консоль все вопросы
    page = 1  # Создаем переменную, означающую что это первая страница
    while True:  # Определяем бесконечный цикл, чтобы получить все данные, т.к. может быть несколько страниц с данными
        response = request_overflow(page)  # Вызываем функцию, которая делает запрос и передаем в нее переменную, содержащую страницу. Ответ сохраняем в переменную
        search_result = response["items"]  # Получаем из ответа запроса данные
        for item in search_result:  # Проходим в цикле по данным
            print(f'Page number: {page}\n')
            print(item['title'])  # Печатаем заголовок
            print(item['link'])  # Печатаем ссылку вопросса на ресурсе
            print(convert_date_from_timestamp(item['creation_date']))  # В функцию преобразования даты передаем дату создания вопроса
            print(f'\n{"-" * 30}\n')
        if not response['has_more']:  # Если больше данных нет, то прерываем бесконечный цикл. Данный ключ находится в ответе от сервера
            break
        page += 1  # Увеличиваем страницу на один
        time.sleep(0.3)  # Делаем паузу на пол секунды, чтобы не заблокировал ресурс из-за большого количества запросов за короткий промежуток времени

if __name__ == '__main__':
    response_result()  # Вызываем функцию вывода вопросов