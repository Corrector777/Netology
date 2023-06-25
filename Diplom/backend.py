import vk_api
from datetime import datetime
from data import access_token
from vk_api.exceptions import ApiError
from pprint import pprint
from operator import itemgetter


class VKApi:

    def __init__(self, access_token):
        self.vk_app = vk_api.VkApi(token=access_token)
 
    def profile_info(self, user_id):
        try:
            info = self.vk_app.method('users.get',
                                    {'user_id': user_id,
                                    'fields': 'city, sex, bdate'})[0]
        
        except ApiError as err:
            result = {}
            print(f'ошибка{err}')
        birth_date = info.get('bdate') if info.get('bdate') is not None else None
        user_age, = datetime.now().year - int(birth_date.split('.')[2]) if birth_date is not None and len(birth_date.split('.')) == 3 else None,
        
        result = {'id': info.get('id'),
                  'name': f"{info.get('first_name')}  {info.get('last_name')}",
                  'city': info.get('city')['title'] if info.get('city') is not None else None,
                  'sex': info.get('sex'),
                  'age': user_age
                  }   

        return result
    
    def search_partners(self, search_data, offset):
        sex = 1 if search_data['sex'] == 2 else 2
        city = search_data['city']
        age = search_data['age']
        age_from = age - 3
        age_to = age + 1

        try:
            search_partners = self.vk_app.method('users.search',
                                                 {'count': 10,
                                                  'offset': offset,
                                                  'age_from': age_from,
                                                  'age_to': age_to,
                                                  'sex': sex,
                                                  'hometown': city,
                                                  'has_photo': True})
        
        except ApiError as err:
            search_partners = []
            print(f'ошибка{err}')

        found_partners = search_partners['items']
        result = []
        for partner in found_partners:
            # print(partner)
            if partner['is_closed'] is False:
                result.append({'id': partner['id'],
                               'name': f"{partner['first_name']} {partner['last_name']}"})
    
        return result
    
    def get_photos(self, owner_id):
        try:
            photos = self.vk_app.method('photos.get',
                                       {'owner_id': owner_id,
                                        'album_id': 'profile',
                                        'extended': True})
        
        except ApiError as err:
            photos = {}
            print(f'ошибка{err}')
        
        result = []
        
        for photo in photos['items']:
            # print(photos)
            result.append({'owner_id': photo['owner_id'],
                           'id': photo['id'],
                           'likes': photo['likes']['count'],
                           'comments': photo['comments']['count']}) 
        sorted_result = sorted(result, key=itemgetter('likes', 'comments'), reverse=True)
        return sorted_result[:3]


if __name__ == '__main__':

    user_id = 1546753
    vk_app = VKApi(access_token)
    print(vk_app.profile_info(user_id))
    search_data = vk_app.profile_info(user_id)
    print(vk_app.get_photos(1111353))
    profiles = vk_app.search_partners(search_data, 5)
    while len(profiles) > 0:
        profile = profiles.pop()
        pprint(profile)
        print('_______________')
    if profiles:
        pprint('фото еще есть')
    else:
        print('анкеты кончились')
    owner_id = profile['id']
    pprint(vk_app.get_photos(owner_id))
   
