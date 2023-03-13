votes = [1, 1, 1, 1, 1, 1, 2, 3, 3, 3, 3, 4]
counter = 0
item = votes[0]
for vote in votes:
    # print(votes.count(vote))
    if votes.count(vote) > counter:
        counter = votes.count(vote)
        print(counter, end="---->")
        item = vote
        print(item)
    # print(item)


# print(max_vote)


# my_dict = {}
# for vote in votes:
#     if vote in my_dict:
#         my_dict[vote] += 1
#     else:
#         my_dict[vote] = 1

# for key, val in my_dict.items():
#     if val == max(my_dict.values()):
#         print(key)


# List = [2, 1, 1, 2, 1, 3]
# dict = {}
# count, itm = 0, ''
# for item in List:
#     print(item)
#     print(dict)
#     dict[item] = dict.get(item, 0) + 1
#     print(dict[item])
#     if dict[item] >= count:
#         count, itm = dict[item], item
# print(itm)
 

# d = {}
# x = [2, 8, 3, 1, 6, 8, 8, 8, 98, 11]
# for i in x:
#     d[i] = x.count(i)
# print(max(d, key=d.get))

# print(max(votes, key=votes.count))

# votes = [1,2,2,2,3]
# d = {}
# for v in votes:
#     # print(v)
#     d.setdefault(v, 0)
#     d[v] += 1
#     # print(d)
#     sorted_by_count = sorted(d.items(), key=lambda a: a[1], reverse=True)
# print(sorted_by_count)
# print(type(sorted_by_count[0]))


# def vote(votes):
#     mydict = {}
#     for v in votes: 
#         if v in mydict:
#             mydict[v] += 1
#         else:
#             mydict.update({v: 1})
       
#     for k, v in mydict.items():
#         if max(mydict.values()) == v:
           
#             return k
        

# print(vote([1,1,1,2,3]))
# print(vote([1,2,3,2,2]))