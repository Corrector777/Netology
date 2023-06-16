
import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.utils import get_random_id

# from backend import VKApi
from data import group_token, access_token

greeting = ['привет', 'здравствуйте', 'хелоу', 'хай', 'hi', 'дд', 'hello']
goodbye = ['пока', 'прощай', 'бай', 'bye', 'чао', 'удачи', 'исчезни']


class Interface():
    def __init__(self, group_token):
        self.vk_interface = vk_api.VkApi(token=group_token)
        self.longpoll = VkLongPoll(self.vk_interface)
        
    def message_send(self, user_id, message, attachment=None):
        self.vk_interface.method('messages.send',
                       {'user_id': user_id,
                        'message': message,
                        'attachment': attachment,
                        'random_id': get_random_id()})
        
    def id_return(self):
        for event in self.longpoll.listen():
            if event.type == VkEventType.MESSAGE_NEW and event.to_me:
                user = event.user_id
        return user


    def events_handling(self):
        for event in self.longpoll.listen():
            if event.type == VkEventType.MESSAGE_NEW and event.to_me:
                user = event.user_id
                message = event.text.lower()
                if message in greeting:
                    self.message_send(user, 'Приветствую тебя, искатель необъятной любви.')
                elif message == 'поиск':
                    self.message_send(user, f'Приступаю к поиску пары для пользователя {user}')
                else:
                    self.message_send(user, '''Комманда неизвестна.
                                                    ___________________________________________
                                                    На данной стадии я знаю следующие комманды:
                                                    - привет 
                                                    - поиск (приступим к вожделенному поиску)
                                                    - пока (будем прощаться)''')


if __name__ == '__main__':
    bot = Interface(group_token)

    bot.events_handling()
   
