import json
import collections


def read_json(file_path, max_len_word=6, top_words=10):
    with open(file_path, encoding='utf 8') as f:
        news = json.load(f)
        words = []
        for item in news['rss']['channel']['items']:
            d = [word for word in item['description'].split(' ') if len(word) > max_len_word]
            words.extend(d)
            counter_words = collections.Counter(words)
        print(counter_words.most_common(top_words))

           
read_json('Netology/Homework(Python)/Different files/1.json')