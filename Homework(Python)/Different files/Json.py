import json


def read_json(file_path, max_len_word=6):
    with open(file_path, encoding='utf 8') as f:
        news = json.load(f)
        words = []
        for item in news['rss']['channel']['items']:
            d = [word for word in item['description'].split(' ') if len(word) > max_len_word]
            words.extend(d)
        print(d)
           

read_json('1.json')