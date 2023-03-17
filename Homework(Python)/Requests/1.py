import requests


def heroes_intelligence(heroes_list: list): 
    res = requests.get('https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/all.json')
    if res.status_code != 200:
        return 'ResponseError'
    
    characters_list = res.json()
    intelligence_of_heroes_dict = {}
    for character in characters_list:
        name = character['name']
        if name in heroes_list:
            intelligence_of_heroes_dict[name] = character['powerstats']['intelligence']

    the_most_intelligece_hero = max(intelligence_of_heroes_dict.items(),
                                    key=lambda x: x[1])
    
    hero_name, intelligence = the_most_intelligece_hero
    return f'the most intelligece hero is: {hero_name}, his intelligense is: {intelligence}'


print(heroes_intelligence(['Hulk', 'Captain America', 'Thanos']))
