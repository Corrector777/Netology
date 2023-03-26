import requests
from pprint import pprint
from tqdm import tqdm
from datetime import datetime
import json

with open('/Users/roman/Git/Token.ini') as file:
    YA_TOKEN = file.readline().strip()
    VKTOKEN = file.readline().strip()


class YaDisk:

    def __init__(self, token: str):
        self.token = token
        self.ya_url = 'https://cloud-api.yandex.net'

    def get_header(self):
        return {
            "Content-Type": "application/json",
            "Authorization": f"OAuth {self.token}"}
    
    def get_sorted_file_list(self):
        url = f'{self.ya_url}/v1/disk/resources/files'
        headers = self.get_header()
        res = requests.get(url=url, headers=headers)
        if res.status_code != 200:
            return 'StatusError'
        return res.json()
    
    def folder_creator(self, folder_name):
        url = f'{self.ya_url}/v1/disk/resources'
        headers = self.get_header()
        params = {'path': folder_name}
        res = requests.put(url=url, headers=headers, params=params)
        if res.status_code == 201:
            return f'Folder {folder_name} created'
        if res.status_code == 409:
            return f'ERROR!Folder {folder_name} already created'
        return res
    
    def upload_file_link(self, yandex_path: str):
        headers = self.get_header()
        get_url = f'{self.ya_url}/v1/disk/resources/upload'
        params = {'path': yandex_path}
        response = requests.get(url=get_url, headers=headers, params=params)
        if response.status_code == 200:
            print('Запрос ссылки успешен')
        response.raise_for_status()
        return response.json()

    def upload_file(self, yandex_path: str, my_file_path: str):
        download_response = self.upload_file_link(yandex_path=yandex_path)
        href_url = download_response.get('href', '')
        with open(my_file_path, 'rb') as f:
            get_response = requests.put(url=href_url, data=f)
        if get_response.status_code == 201:
            print('Файл успешно записан')
        get_response.raise_for_status()
        return get_response
    
    def upload_file_by_url(self, yandex_dir, photo_files):
        json_output = []
        upload_url = f'{self.ya_url}/v1/disk/resources/upload'
        for file in tqdm(photo_files, desc="Loading: ", ncols=100, colour='blue'):
            yandex_path = f'{yandex_dir}/{file["name"]}.jpeg'
            file_url = f'{file["url"]}'
            params_for_upload = {
                                'url': file_url,
                                'path': yandex_path,
                                }
            res = requests.post(upload_url, params=params_for_upload, headers=self.get_header())
            # res.raise_for_status()

            json_info = {
                        'name': file['name'],
                        'size': file['type'],
                        'folder': yandex_dir,
                        }
            json_output.append(json_info)
        with open('/Users/roman/Git/Netology/Homework(Python)/Итоговая работа/output.json', 'a') as info:
            json.dump(json_output, info)

        if 300 >= res.status_code >= 201:
            print(f'all files downloaded successfully')
        else:
            print('Error')
        

class VK:

    def __init__(self, vk_token, user_id, version='5.131'):
        self.token = vk_token
        self.id = user_id
        self.version = version
        self.url = 'https://api.vk.com/method'
        self.params = {'access_token': self.token, 
                       'v': self.version
                       }

    def users_info(self):
        url = self.url + '/users.get'
        params = {'user_ids': self.id}
        response = requests.get(url, params={**self.params, **params})
        return response.json()
    
    def users_photo(self):
        user_photo = input("""
        введите , какой альбом вас интересует:
        •wall — фотографии со стены,
        •profile — фотографии профиля,
        •saved — сохраненные фотографии.
        """)
        count = input('Введите кол-во выводимых фотографий')
        url = self.url + '/photos.get'
        params = {'owner_id': self.id,
                  'album_id': user_photo,
                  'extended': 'likes',
                  'photo_sizes': 1,
                  'count': count
                  }
        response = requests.get(url, params={**self.params, **params}).json()
        return response['response']['items']
        
    def get_max_size_photo(self, photo_sizes):

        # pprint(photo_sizes)
        max_size_photo = []
        for photo in photo_sizes:
            # pprint(photo)
            photo_dict = {}
            photo_name = str(photo['likes']['count'])
            for user_photo in max_size_photo:
                if user_photo['name'] == photo_name:
                    photo_name += f"({datetime.utcfromtimestamp(int(photo['date'])).strftime('%Y-%m-%d: %H-%M')})"
            sizes = {'w': 10, 'z': 9, 'y': 8, 'x': 7, 'm': 6, 's': 5}
            sorted_photo_sizes = sorted(photo['sizes'], key=lambda x: sizes.get(x['type'], 0))
            max_sized_photo = sorted_photo_sizes[-1]
            photo_dict.setdefault('name', photo_name)
            photo_dict.setdefault('url', max_sized_photo['url'])
            photo_dict.setdefault('type', max_sized_photo['type'])
            max_size_photo.append(photo_dict)
        return max_size_photo


if __name__ == '__main__':
    def save_photo_to_ya_disk():
        vk_token = VKTOKEN
        ya_token = YA_TOKEN
        user_id = '1288829'
        vk = VK(vk_token, user_id)
        photo_sizes = vk.users_photo()
        photo_files = vk.get_max_size_photo(photo_sizes=photo_sizes)
        ya_disk = YaDisk(token=ya_token)
        directory_name = input('Введите название папки для сохранения файлов: ')
    
        ya_disk.folder_creator(directory_name)
        ya_disk.upload_file_by_url(yandex_dir=directory_name, photo_files=photo_files)

    save_photo_to_ya_disk()
