import vk_api


from data import access_token

class VKApi:

    def __init__(self, access_token):
        self.vk_app = vk_api.VkApi(token=access_token)
     

    def profile_info(self, user_id):
        info = self.vk_app.method('users.get',
                        {'user_id': user_id,
                        'fields': 'city, bdate,sex,relation,home_town'})[0]
        return info


if __name__ == '__main__':

    tools = VKApi(access_token)
    user_id = 1546753
    print(tools.profile_info(user_id))