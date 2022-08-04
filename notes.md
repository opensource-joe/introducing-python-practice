# Notes file

- Introducing Python, 2nd Ed. by Bill Lubanovic
- Book on O'Reilly: https://learning.oreilly.com/library/view/introducing-python-2nd/9781492051374/
- Code: https://github.com/madscheme/introducing-python

***Zen of Python - import this***

***MD preview - shift command V***

## Chapter 1

- Computer languages are made of *data* (like nouns in spoken languages) and *instructions* or *code* (like verbs).
- Using *for* and *iterators* is a more direct way of making a loop than manually incrementing some counter variable.

## Chapter 2

- Programs keep track of *where* (memory location) their bits are, and *what* (data type) they are. To your computer, it's all just bytes.
- Python wraps each data value - booleans, integers, floats, strings, even large data structures, functions, and programs - in memory as an *object*.
- The *type* determines whether the data *value* contained by the box can be changed (*mutable*) or is constant (*immutable*).
- Python is *strongly typed*, which means that the type of an object does not change, even if its value is mutable.
- There are two ways to express data values in Python: 1) literal and 2) variable.
- Variables are names for values in your computer's memory that you want to use in a program. They can contain only these characters:
    - Lowercase letters (a through z)
    - Uppercase letters (A through Z)
    - Digits (0 through 9)
    - Underscore (_)
    - They are *case sensitive*: thing, Thing, and THING are different names
    - They must begin with a letter or an underscore, not a digit
    - Names that begin with an underscore are treated specially
    - They cannot be one of Python's reserved words (also known as keywords - >>> help('keywords'))
- Programs - everything on the right side needs to have a value (this is called being *initialized*)
- Crucial point about variables in Python: *variables* are just *names*.
- If you want to know the type of anything (a variable or literal value), you can use type(thing)
- A *class* is the definition of an object.
- In Python, *class* and *type* mean pretty much the same thing.
- Python has a charmingly named *garbage collector* that reuses the memory of things that are no longer needed.
- A *list* is a mutable array of values.