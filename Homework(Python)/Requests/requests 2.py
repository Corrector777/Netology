import requests
from pprint import pprint

with open('/Users/roman/Git/Token') as file:
    TOKEN = file.readline()


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


if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    my_file_path = '/Users/roman/Git/Netology/Homework(Python)/5 classes/11.py'
    file_name_for_yandex_disk = '12.py'
    token = TOKEN
    ya_disk = YaDisk(token)
    # ya_disk.folder_creator('Practice')
    ya_disk.upload_file(yandex_path=file_name_for_yandex_disk, my_file_path=my_file_path)
