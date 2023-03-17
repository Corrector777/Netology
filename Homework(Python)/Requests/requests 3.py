import requests
from pprint import pprint

headers = {
    'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'Connection': 'keep-alive',
    'Accept-Encoding': 'gzip, deflate, br',
    'Cookie': 'prov=10ffad1a-9a67-b723-d915-e1f7c8650a4c; SLG_G_WPT_TO=ru; SLG_GWPT_Show_Hide_tmp=1; SLG_wptGlobTipTmp=1',
    'Referer': 'https://api.stackexchange.com/docs/questions',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 OPR/96.0.0.0',
    'sec-ch-ua-platform': 'macOS',
}

params = {
    'key': 'U4DMV*8nvpm3EOpvf69Rxw((',
    'site': 'stackoverflow',
    'fromdate': '1678924800',
    'todate': '1679097600',
    'order': 'desc',
    'sort': 'creation',
    'tagged': 'python',
    '': '',
    }

url = 'https://api.stackexchange.com/2.3/questions'

response = requests.get(url=url, headers=headers, params=params)
pprint(response.json())