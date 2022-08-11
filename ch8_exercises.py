# https://learning.oreilly.com/library/view/introducing-python-2nd/9781492051374/ch08.html#:-:text=Things%20to%20Do

# 8.1 Make an English-to-French dictionary called e2f and print it. Here are your starter words: dog is chien, cat is chat, and walrus is morse.

# e2f = {'dog':'chien', 'cat':'chat', 'walrus':'morse'}
# print(e2f)

# 8.2 Using your three-word dictionary e2f, print the French word for walrus.

# print(e2f['walrus'])

# 8.3 Make a French-to-English dictionary called f2e from e2f. Use the items method.

# f2e = {}
# for english, french in e2f.items():
#     f2e[french] = english
# print(f2e)

# 8.4 Print the English equivalent of the French word chien.

# print(f2e['chien'])

# 8.5 Print the set of English words from e2f.

# print(set(e2f.keys()))

# 8.6 Make a multilevel dictionary called life. Use these strings for the topmost keys: 'animals', 'plants', and 'other'. Make the 'animals' key refer to another dictionary with the keys 'cats', 'octopi', and 'emus'. Make the 'cats' key refer to a list of strings with the values 'Henri', 'Grumpy', and 'Lucy'. Make all the other keys refer to empty dictionaries.

# life = {
#     'animals':{
#         'cats':[
#             'Henri',
#             'Grumpy',
#             'Lucy'
#         ],
#         'octopi':{},
#         'emus':{}
#     },
#     'plants':{},
#     'other':{}
# }

# 8.7 Print the top-level keys of life.

# print(life.keys())

# 8.8 Print the keys for life['animals'].

# print(list(life.keys()))

# 8.9 Print the values for life['animals']['cats'].

# print(life['animals'].keys())

# 8.10 Use a dictionary comprehension to create the dictionary squares. Use range(10) to return the keys, and use the square of each key as its value.

# squares = {key: key * key for key in range(10)}
# print(squares)

# 8.11 Use a set comprehension to create the set odd from the odd numbers in range(10).

# odd = {key for key in range(1, 10, 2)}
# print(odd)

# 8.12 Use a generator comprehension to return the string 'Got ' and a number for the numbers in range(10). Iterate through this by using a for loop.

# for thing in ('Got %s' % number for number in range(10)):
#     print(thing)

# 8.13 Use zip() to make a dictionary from the key tuple ('optimist', 'pessimist', 'troll') and the values tuple ('The glass is half full', 'The glass is half empty', 'How did you get a glass?').

# keys = ('optimist', 'pessimist', 'troll')
# values = ('The glass is half full', 'The glass is half empty', 'How did you get a glass?')
# output = dict(zip(keys, values))
# print(output)

# 8.14 Use zip() to make a dictionary called movies that pairs these lists: titles = ['Creature of Habit', 'Crewel Fate', 'Sharks On a Plane'] and plots = ['A nun turns into a monster', 'A haunted yarn shop', 'Check your exits']

# titles = ['Creature of Habit', 'Crewel Fate', 'Sharks on a Plane']
# plots = ['A nun turns into a monster', 'A haunted yarn shop', 'Check your exits']

# output = dict(zip(titles, plots))
# print(output)