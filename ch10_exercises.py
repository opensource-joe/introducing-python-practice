# https://learning.oreilly.com/library/view/introducing-python-2nd/9781492051374/ch10.html#:-:text=Things%20to%20Do

# 10.1 Make a class called Thing with no contents and print it. Then, create an object called example from this class and also print it. Are the printed values the same or different?

# class Thing:
#     pass
# print(Thing)

# example = Thing()
# print(example)

# 10.2 Make a new class called Thing2 and assign the value 'abc' to a class attribute called letters. Print letters.

# class Thing2:
#     letters = 'abc'

# print(Thing2.letters)
    
# 10.3 Make yet another class called, of course, Thing3. This time, assign the value 'xyz' to an instance (object) attribute called letters. Print letters. Do you need to make an object from the class to do this?

# class Thing3:
#     def __init__(self):
#         self.letters = 'xyz'

# something = Thing3()
# print(something.letters)

# 10.4 Make a class called Element, with instance attributes name, symbol, and number. Create an object of this class with the values 'Hydrogen', 'H', and 1.

# class Element:
#     def __init__(self, name, symbol, number):
#         self.name = name
#         self.symbol = symbol
#         self.number = number

# hydrogen = Element('Hydrogen', 'H', 1)
# print(hydrogen.name, hydrogen.symbol, hydrogen.number)

# 10.5 Make a dictionary with these keys and values: 'name': 'Hydrogen', 'symbol': 'H', 'number': 1. Then, create an object called hydrogen from class Element using this dictionary.

# from dataclasses import dataclass
# @dataclass
# class Element:
#     name: str
#     symbol: str
#     number: int

# hydrogen = Element('Hydrogen', 'H', 1)
# print(hydrogen)

# el_dict = {'name':'Hydrogen', 'symbol':'H', 'number':1}

# class Element:
#     def __init__(self, name, symbol, number):
#         self.name = name
#         self.symbol = symbol
#         self.number = number

# hydrogen = Element(**el_dict)
# print(hydrogen.name, hydrogen.symbol, hydrogen.number)

# 10.6 For the Element class, define a method called dump() that prints the values of the object’s attributes (name, symbol, and number). Create the hydrogen object from this new definition and use dump() to print its attributes.

# el_dict = {'name':'Hydrogen', 'symbol':'H', 'number':1}

# class Element:
#     def __init__(self, name, symbol, number):
#         self.name = name
#         self.symbol = symbol
#         self.number = number
#     def dump(self):
#         print('name=%s, symbol=%s, number=%s' % (self.name, self.symbol, self.number))

# hydrogen = Element(**el_dict)
# hydrogen.dump()

# 10.7 Call print(hydrogen). In the definition of Element, change the name of the method dump to __str__, create a new hydrogen object, and call print(hydrogen) again.

# el_dict = {'name':'Hydrogen', 'symbol':'H', 'number':1}

# class Element:
#     def __init__(self, name, symbol, number):
#         self.name = name
#         self.symbol = symbol
#         self.number = number
#     def __str__(self):
#         return('name=%s, symbol=%s, number=%s' % (self.name, self.symbol, self.number))

# hydrogen = Element(**el_dict)
# print(hydrogen)

# 10.8 Modify Element to make the attributes name, symbol, and number private. Define a getter property for each to return its value.

# class Element:
#     def __init__(self, name, symbol, number):
#         self._name = name
#         self._symbol = symbol
#         self._number = number
#     @property
#     def name(self):
#         return self._name
#     @property
#     def symbol(self):
#         return self._symbol
#     @property
#     def number(self):
#         return self._number

# hydrogen = Element('Hydrogen', 'H', 1)
# print(hydrogen.name, hydrogen.symbol, hydrogen.number)

# 10.9 Define three classes: Bear, Rabbit, and Octothorpe. For each, define only one method: eats(). This should return 'berries' (Bear), 'clover' (Rabbit), or 'campers' (Octothorpe). Create one object from each and print what it eats.

# class Bear:
#     def eats(self):
#         return 'berries'

# class Rabbit:
#     def eats(self):
#         return 'clover'

# class Octothorpe:
#     def eats(self):
#         return 'campers'
    
# b = Bear()
# r = Rabbit()
# o = Octothorpe()

# print(b.eats())
# print(r.eats())
# print(o.eats())

# 10.10 Define these classes: Laser, Claw, and SmartPhone. Each has only one method: does(). This returns 'disintegrate' (Laser), 'crush' (Claw), or 'ring' (SmartPhone). Then, define the class Robot that has one instance (object) of each of these. Define a does() method for the Robot that prints what its component objects do.

# class Laser:
#     def does(self):
#         return 'disentegrate'

# class Claw:
#     def does(self):
#         return 'crush'

# class SmartPhone:
#     def does(self):
#         return 'ring'

# class Robot:
#     def __init__(self):
#         self.laser = Laser()
#         self.claw = Claw()
#         self.smartphone = SmartPhone()
#     def does(self):
#         return '''I have many attachements:
# My laser, to %s.
# My claw, to %s.
# My smartphone, to %s.''' % (
#     self.laser.does(),
#     self.claw.does(),
#     self.smartphone.does()
# )

# robbie = Robot()
# print( robbie.does() )