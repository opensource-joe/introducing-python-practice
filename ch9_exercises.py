# https://learning.oreilly.com/library/view/introducing-python-2nd/9781492051374/ch09.html#:-:text=Things%20to%20Do

# Practice with examples in the chapter

# Making a function and calling it
# def make_a_sound():
#     print('quack')
# make_a_sound()

# Using an if statement
# def agree():
#     return False
# if agree():
#     print('Splendid')
# else:
#     print('That was unexpected.')
# agree()

# Function with calling parameter
# def echo(anything):
#     return anything + ' '
# print(echo('this is it'))

# Function that takes an input argument and does something with it
# def commentary(color):
#     if color == 'red':
#         return 'It\'s a tomato.'
#     elif color == 'green':
#         return 'It\'s a green pepper.'
#     elif color == 'bee purple':
#         return 'I don\'t know what it is, but only bees can see it.'
#     else:
#         return 'I\'ve never heard of the color ' + color + '.'
# print(commentary('blue'))

# None holds a special place in Python
# thing = None
# if thing:
#     print('It\'s some thing')
# else:
#     print('It\'s no thing')
# print(thing)

# Distinguishing None from False
# thing = None
# if thing is None:
#     print('It\'s nothing')
# else:
#     print('It\'s something')
# print(thing)

# Function that puts together None, True, and False
# def whatis(thing):
#     if thing is None:
#         print(thing, 'is None')
#     elif thing:
#         print(thing, 'is True')
#     else:
#         print(thing, 'is False')
# (whatis(True))

# Specify default parameter values
# def menu(wine, entree, dessert='pudding'):
#     return{'wine': wine, 'entree': entree, 'dessert': dessert}
# print(menu('pinot', 'steak', 'mousse'))

# --------

# 9.1 Define a function called good() that returns the 
# following list: ['Harry', 'Ron', 'Hermione'].

# def good():
#     return ['Harry', 'Ron', 'Hermione']
# print(good())

# 9.2 Define a generator function called get_odds() that returns the odd numbers from range(10). Use a for loop to find and print the third value returned.

# 9.3 Define a decorator called test that prints 'start' when a function is called, and 'end' when it finishes.

# 9.4 Define an exception called OopsException. Raise this exception to see what happens. Then, write the code to catch this exception and print 'Caught an oops'.