import json


def read_json(file_path: str):
    with open(file_path, encoding='utf 8') as f:
        news = json.load(f)
        print(news)


read_json('1.json')