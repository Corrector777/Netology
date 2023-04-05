from datetime import datetime
from tqdm import tqdm
from pprint import pprint
import requests
import io
import json


"""
Для корректной работы необходимо извлечь два токена из Файла Tokens.txt
"""
with open('/Users/roman/Git/Netology/Homework(Python)/Итоговая работа/vktoken.ini') as file_object:
    TOKEN_VK = file_object.readline().strip()
    TOKEN_YANDEX = file_object.readline().strip()


class UsersVK:

    def __init__(self):
        self.vk_token = TOKEN_VK
        self.url = 'https://api.vk.com/method/'
        self.params = {
            'access_token': self.vk_token,
            'v': '5.131'
        }

    def get_photo(self, vk_id: str):
        """
        Метод запрашивает фото профиля пользователя и возвращает json-файл с информацией о фото.
        :vk_id  id пользователя VK
        """
        count = int(input('Введите количество фотографий для получения: '))
        album_id = input('Выберите (из предложенного списка) из какого альбома начать скачку фотографий, '
                         'и введите в соответствии с названием:\n'
                         'wall - фотографии со стены\n'
                         'profile - фотографии профиля\n'
                         'saved -  сохраненные фотографии. Возвращается только с ключом доступа пользователя.\n'
                         'Ввод: ')
        url_photo = self.url + 'photos.get'
        params = {
            'owner_id': vk_id,
            'album_id': album_id,
            'extended': 'likes',
            'photo_sizes': '1',
            'count': count
        }
        res = requests.get(url_photo, params={**self.params, **params}).json()

        return res['response']['items']

    def parsed_photo(self, photos_info: list):
        """
        Метод парсит json-файл с профиля пользователя VK
        :param photos_info: json файл с описанием фото пользователя VK
        :return: список словарей с url на фотографии
        """
        pprint(photos_info)
        type_sizes = ['w', 'z', 'y', 'x', 'm', 's']
    
        user_profile_photos = []
        for photo in photos_info:
            photo_dict = {}
            name_photo = str(photo['likes']['count'])
            for user_photo in user_profile_photos:
                if user_photo['name'] == name_photo:
                    name_photo += f"({datetime.utcfromtimestamp(int(photo['date'])).strftime('%Y-%m-%d: %H-%M')})"
            for alpha in type_sizes:
                size = [x for x in photo['sizes'] if x['type'] == alpha]
                type_size = alpha
                if size:
                    break

            photo_dict.setdefault('name', name_photo)
            photo_dict.setdefault('url', size[0]['url'])
            photo_dict.setdefault('type_size', type_size)
            user_profile_photos.append(photo_dict)

        return user_profile_photos


class UsersYD:

    def __init__(self):
        self.token = TOKEN_YANDEX
        self.url = 'https://cloud-api.yandex.net/v1/disk/resources/'
        self.headers = {
            'Authorization': f'OAuth {self.token}',
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        }

    def create_folder(self, name_dir: str):
        """
        Метод создает папку на Яндекс Диске пользователя
        :param name_dir: название папки
        :return: None
        """
        params = {
            'path': f'/{name_dir}/'
        }
        requests.put(self.url, headers=self.headers, params=params)

    def upload_file(self, files: list, name_dir: str):
        """
        Метод загружает на Яндекс Диск пользователя фото
        :param files: Список со словарями, которые содержат ссылки на фото
        :param name_dir: Наименование папки, в которую необходимо совешить загрузку
        :return: Прогресс-бар с ходом загрузки, результат загрузки и создает json-файл с информацией
        о загруженных фотографиях.
        """
        upload_url = self.url + 'upload'
        data_json = []

        for file in tqdm(files, desc="Loading: ", ncols=100, colour='green'):
            params_for_upload = {
                'url': file['url'],
                'path': f"{name_dir}/{file['name']}",
                'disable_redirects': 'true'
            }
            res = requests.post(upload_url, params=params_for_upload, headers=self.headers)
            status = res.status_code
            data = {
                        "file_name": f"{file['name']}.jpg",
                        "size": file['type_size']
                }
            data_json.append(data)
        with open('data.json', 'a') as outfile:
            json.dump(data_json, outfile, indent=0)

        if 400 > status:
            print(f'Фотографии загружены на: https://disk.yandex.ru/client/disk/{name_dir}')
        else:
            print('Ошибка загрузки')


def main():
    id_vk = '1288829'
    user_vk = UsersVK()
    name_directory = input('Введите название для новой папки: ')
    json_photo = user_vk.get_photo(id_vk)
    # pprint(json_photo)
    parsed_photo = user_vk.parsed_photo(json_photo)
    user_yd = UsersYD()
    user_yd.create_folder(name_directory)
    user_yd.upload_file(parsed_photo, name_directory)


if __name__ == '__main__':
    main()

    #    def get_max_size_photo(self, photo_sizes: list) -> dict | None:
    #     sizes = ['w', 'z', 'y', 'x', 'm', 's']
    #     new_dict = {size['type']: size for size in photo_sizes}
    #     for size in sizes:
    #         if size in new_dict:
    #             return new_dict[size]