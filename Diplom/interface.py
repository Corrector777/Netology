
import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.utils import get_random_id


from data import group_token, access_token

greeting = ['привет', 'здравствуйте', 'хелоу', 'хай', 'hi', 'дд', 'hello']
goodbye = ['пока', 'прощай', 'бай', 'bye', 'чао', 'удачи', 'исчезни']


class Interface():
    def __init__(self, group_token):
        self.vk = vk_api.VkApi(token=group_token)
        self.longpoll = VkLongPoll(self.vk)
        
    def message_send(self, user_id, message, attachment=None):
        self.vk.method('messages.send',
                       {'user_id': user_id,
                        'message': message,
                        'attachment': attachment,
                        'random_id': get_random_id()})
        
    def events_handling(self):
        for event in self.longpoll.listen():
            if event.type == VkEventType.MESSAGE_NEW and event.to_me:
                message = event.text.lower()
                if message in greeting:
                    self.message_send(event.user_id, '''Приветствую тебя, искатель необъятной любви.
                                                    ___________________________________________
                                                    На данной стадии я знаю следующие комманды:
                                                    - идентификация (расскажу о тебе)
                                                    - поиск (приступим к вожделенному поиску)
                                                    - пока (будем прощаться)''')
                elif message == 'поиск':
                    self.message_send(event.user_id, 'Приступаю к поиску')
                else:
                    self.message_send(event.user_id, 'Комманда неизвестна')


if __name__ == '__main__':
    bot = Interface(group_token)
    bot.events_handling()
   
