stats = {'yandex': [120], 'vk': [115], 'google': [99], 'email': [42], 'ok': [98, 4, 6]}
# sum_of_rates = 0
# lections_count = 0
# for key, value in stats.items():
#     sum_of_rates += sum(stats[key])
#     lections_count += len(value)
# print(lections_count)

# print(f'{sum_of_rates/lections_count: .1f}')

a = list(map(sum, stats.values()))
b = list(map(len, stats.values())) 
print(sum(a))
print(b)
    
    # if value == max(stats.values()):
    #     print({f'канал с максимальным объемом продаж: {key}'})

# print(len(stats))

# a = sum(stats.values())
# print(a)
