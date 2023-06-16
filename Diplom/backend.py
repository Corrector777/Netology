import vk_api


from data import access_token, group_token
from interface import Interface


class VKApi:

    def __init__(self, access_token, group_token):
        self.vk_app = vk_api.VkApi(access_token)
        self.vk_inteface = Interface(group_token)
        self.id = ''

    def profile_info(self):
        self.id = self.vk_inteface.id_return()
        info = self.vk_app.method('users.get',
                        {'user_id': self.id,
                        'fields': 'city, bdate,sex,relation,home_town'})[0]
        return info


if __name__ == '__main__':

    tools = VKApi(access_token, group_token)

    print(tools.profile_info())