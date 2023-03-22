import requests
from pprint import pprint

with open('/Users/roman/Git/Token') as file:
    TOKEN = file.readline()


with open('Homework(Python)/Итоговая работа/vktoken.ini') as vktoken:
    VKTOKEN = vktoken.readline()
photo_links_dict = {}


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
    
    def upload_file_by_url(self, yandex_path: str, file_url: str):
        download_response = self.upload_file_link(yandex_path=yandex_path)
        href_url = download_response.get('href', '')
        get_response = requests.post(url=href_url, data=file_url)
        if get_response.status_code == 201:
            print('Файл успешно записан')
        get_response.raise_for_status()
        return get_response


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
    
    def users_avatar(self):
        url = self.url + '/photos.get'
        params = {'owner_id': self.id,
                  'album_id': 'profile',
                  'extended': 1,
                  'photo_sizes': 1
                  }
        response = requests.get(url, params={**self.params, **params})
        return response.json()

    def max_size_foto(self):
        response = self.users_avatar()
        result = response['response']['items']
        for item in result:
            key = item['likes']['count']
            for type in item['sizes']:
                if 'w' in type['type']:
                    photo_links_dict[key] = type['url']



if __name__ == '__main__':
    # vk_token = VKTOKEN
    # user_id = '3562537'
    # vk = VK(vk_token, user_id)
    # vk.max_size_foto()
    # print(photo_links_dict)

    # my_file_path = '/Users/roman/Git/Netology/Homework(Python)/5 classes/11.py'
    file_name_for_yandex_disk = '11.jpeg'
    token = TOKEN
    ya_disk = YaDisk(token)
    my_file_url = 'https://sun9-38.userapi.com/impg/E8s25Ph5NUYdbNFgx2LcJcjFiGjOgpyqsetoDQ/bX8SxkMi-3M.jpg?size=1344x1792&quality=95&sign=409f5c32e88176ff1299e06a6fc2ebde&c_uniq_tag=cFbvYRcWG0OspRXdQ-nJi8vUZiI6py1jr1hkXKEgzEA&type=album'
#     # ya_disk.folder_creator('Practice')
    ya_disk.upload_file_by_url(yandex_path=file_name_for_yandex_disk, file_url=my_file_url)