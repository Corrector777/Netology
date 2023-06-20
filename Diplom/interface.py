
import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from random import randrange 

from backend import VKApi
from data import group_token, access_token

greeting = ['привет', 'здравствуйте', 'хелоу', 'хай', 'hi', 'дд', 'hello']
goodbye = ['пока', 'прощай', 'бай', 'bye', 'чао', 'удачи', 'исчезни', 'стоп']
search = ['поиск', 'поехали', 's', 'п']


class Interface():
    def __init__(self, group_token):
        self.vk_interface = vk_api.VkApi(token=group_token)
        self.longpoll = VkLongPoll(self.vk_interface)
        self.vk_backend = VKApi(access_token)
        self.my_user_info = {}
        self.offset = 0
        self.partner_profiles = []
        self.flag = True
            
    def message_send(self, user_id, message, attachment=None):
        self.vk_interface.method('messages.send',
                       {'user_id': user_id,
                        'message': message,
                        'attachment': attachment,
                        'random_id': randrange(10 ** 10)})
        
    def get_partner_photos(self, partner_profiles, user):
        if self.partner_profiles:
            partner_profile = self.partner_profiles.pop()
            partner_photos = self.vk_backend.get_photos(partner_profile['id']) 
            self.message_send(user, f'Имя: {partner_profile["name"]}\n страница: vk.com/id{partner_profile["id"]}')
            for num, photo in enumerate(partner_photos, start=1):
                attachment = f'photo{photo["owner_id"]}_{photo["id"]}'
                self.message_send(user, f' Фото номер {num}', attachment=attachment) 
            self.message_send(user, 'для продолжения набери "поиск"')
        else:
            self.message_send(user, f'{self.my_user_info["name"]}\n Результат поиска пуст!\nИзмените введенные данные(город, возраст)\nДля этого введите "привет"')
            self.flag = True

    def events_handling(self):
        for event in self.longpoll.listen():
            if event.type == VkEventType.MESSAGE_NEW and event.to_me:
                user = event.user_id
                message = event.text.lower()
                self.my_user_info = self.vk_backend.profile_info(user) 

                if message in greeting:
                    full_user_info = self.my_user_info
                    self.sex = 'мужской' if self.my_user_info["sex"] == 2 else 'женский'
                    self.age = 'Не определен' if self.my_user_info["age"] is None else self.my_user_info["age"]
                    self.city = 'Не определен' if self.my_user_info["city"] is None else self.my_user_info["city"]
                    self.search_sex = 'женщину' if self.my_user_info["sex"] == 2 else 'мужчину'
                    self.message_send(user, 'Приветствую тебя, искатель необъятной любви.')
                    self.message_send(user, '_____________________')             
                    self.message_send(user, 'Давайте уточним информацию о Вас:')                   
                    self.message_send(user, f' Ваше имя: {self.my_user_info["name"]}')
                    self.message_send(user, f' Ваш пол: {self.sex}')
                    self.age = 'Не определен' if self.my_user_info["age"] is None else self.my_user_info["age"]
                    self.message_send(user, f'Ваш возраст: {self.age}')
                    self.message_send(user, f' Ваш город: {self.city}\n_____________________\n\n')
                    if self.my_user_info["age"] is None:
                        self.message_send(user, f' Возраста не хватает, введите:')
                        for event in self.longpoll.listen():
                            if event.type == VkEventType.MESSAGE_NEW and event.to_me:
                                if event.text.isdigit():
                                    full_user_info['age'] = int(event.text.title())
                                    break
                                else:
                                    self.message_send(user, f' Неккоретно указан возраст(должны быть только цифры):')
                                     
                    if self.my_user_info["city"] is None:                       
                        self.message_send(user, 'Города нет, введите:')
                        for event in self.longpoll.listen():
                            if event.type == VkEventType.MESSAGE_NEW and event.to_me:
                                full_user_info['city'] = event.text.title()
                                break
                    
                    self.message_send(user, f' \nИскать будем:\n'
                                            f' - {self.search_sex}\n'
                                            f'- из города : {self.my_user_info["city"]}\n'
                                            f'- возраст в диапазоне от {int(full_user_info["age"]) -3} до {int(full_user_info["age"]) + 1}')
                    self.flag = False 
                    self.message_send(user, f' Все данные о Вас на борту, {full_user_info["name"]}!!\n\n Введите комманду "поиск" для начала подбора...\nИли комманду "стоп" если в данных есть ошибка')

                elif message in search and self.flag is False:
                    print('searching...')                        
                    self.message_send(user, 'Ищу варианты...\n_____________________')

                    if self.partner_profiles:
                        self.get_partner_photos(self.partner_profiles, user)
                       
                    else:
                        self.offset += 5
                        self.partner_profiles = self.vk_backend.search_partners(full_user_info, self.offset)
                        self.get_partner_photos(self.partner_profiles, user)
                        
                elif message in search and self.flag is True:
                    self.message_send(user, f'Не торопись\n\nДавай собирем все данные\n\n Скажи: "привет"')

                elif message in goodbye:
                    self.message_send(user, f'До скорых встреч, {self.my_user_info["name"]}\n Для начала введите "привет"')
                    self.flag = True

                else:
                    self.message_send(user, ''' Комманда неизвестна.
                                                    ___________________________________________
                                                    На данной стадии я знаю следующие комманды:
                                                    - ['привет', 'здравствуйте', 'хелоу', 'хай', 'hi', 'дд', 'hello'] - приветсвие
                                                    - ['поиск', 'поехали', 's', 'п'] - поиск профилей
                                                    - ['пока', 'прощай', 'бай', 'bye', 'чао', 'удачи', 'исчезни'] - будем прощаться''')
                    


if __name__ == '__main__':
    bot = Interface(group_token)

    bot.events_handling()

