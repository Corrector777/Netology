ids = {'user1': [213, 213, 213, 15, 213],
       'user2': [54, 54, 119, 119, 119],
       'user3': [213, 98, 98, 35]}
my_set = set()
for value in ids.values():
    for item in value:
        my_set.add(item)
print(list(my_set))