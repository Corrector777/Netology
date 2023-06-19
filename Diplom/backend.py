import vk_api
from datetime import datetime
from data import access_token
from vk_api.exceptions import ApiError


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
                  'age': None    #user_age
                  }
        # if result['age'] == None:

        return result


if __name__ == '__main__':

    user_id = 1546753
    vk_app = VKApi(access_token)
    print(vk_app.profile_info(user_id))