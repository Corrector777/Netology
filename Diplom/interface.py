
import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from random import randrange 

from backend import VKApi
from data import group_token, access_token

greeting = ['привет', 'здравствуйте', 'хелоу', 'хай', 'hi', 'дд', 'hello']
goodbye = ['пока', 'прощай', 'бай', 'bye', 'чао', 'удачи', 'исчезни']


class Interface():
    def __init__(self, group_token):
        self.vk_interface = vk_api.VkApi(token=group_token)
        self.longpoll = VkLongPoll(self.vk_interface)
        self.vk_backend = VKApi(access_token)
        self.my_user_info = {}
        
    def message_send(self, user_id, message, attachment=None):
        self.vk_interface.method('messages.send',
                       {'user_id': user_id,
                        'message': message,
                        'attachment': attachment,
                        'random_id': randrange(10 ** 10)})
        
    def events_handling(self):
        for event in self.longpoll.listen():
            if event.type == VkEventType.MESSAGE_NEW and event.to_me:
                user = event.user_id
                message = event.text.lower()
                if message in greeting:
                    self.message_send(user, 'Приветствую тебя, искатель необъятной любви.')
                    self.message_send(user, '_____________________')
                    self.my_user_info = self.vk_backend.profile_info(user)                
                    self.message_send(user, 'Давайте уточним информацию о Вас:')                   
                    self.message_send(user, f' Ваше имя: {self.my_user_info["name"]}')
                    self.message_send(user, f' Ваш пол: {self.my_user_info["sex"]}')
                    self.message_send(user, f' Ваш возраст: {self.my_user_info["age"]}')
                    self.message_send(user, f' Ваш город: {self.my_user_info["city"]}\n_____________________')
                          
                elif message == 'поиск':
                    if self.my_user_info["age"] is None:
                        self.message_send(user, f' Возраста не хватает, введите:')
                        for event in self.longpoll.listen():
                            if event.type == VkEventType.MESSAGE_NEW and event.to_me:
                                
                                self.my_user_info['age'] = event.text.title()
                                break
                        
                    if self.my_user_info["city"] is None:                       
                        self.message_send(user, 'Города нет, введите:')
                        for event in self.longpoll.listen():
                            if event.type == VkEventType.MESSAGE_NEW and event.to_me:
                                self.my_user_info['city'] = event.text.title()
                                break          

                    self.message_send(user, f'Давайте что-то вам подыщем\n_____________________')
                    self.message_send(user, f' \nИскать будем:\n'
                                            f' - пользователя противоположного пола\n'
                                            f'- из города : {self.my_user_info["city"]}\n'
                                            f'- возраст в диапазоне от {int(self.my_user_info["age"]) -3} до {int(self.my_user_info["age"]) + 3}')
                                                          
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

