# Notes file

- Introducing Python, 2nd Ed. by Bill Lubanovic
- Book on O'Reilly: https://learning.oreilly.com/library/view/introducing-python-2nd/9781492051374/
- Code: https://github.com/madscheme/introducing-python

***Zen of Python - import this***

## Python Basics

## Chapter 1: A Taste of Py

- Computer languages are made of *data* (like nouns in spoken languages) and *instructions* or *code* (like verbs).
- Using *for* and *iterators* is a more direct way of making a loop than manually incrementing some counter variable.

## Chapter 2: Data: Types, Values, Variables, and Names

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

## Chapter 3: Numbers

- Python built in data types: 
    - Booleans are true or false
    - Integers are whole numbers
    - Floats are numbers with decimal points

## Chapter 4: Choose with If

- A comment is a piece of text in your program that is ignored by the Python interpreter. The *#* has many names: hash, sharp, pound, and octothorpe.
- If you can’t say everything you want to say in that length, you can use the continuation character: \ (backslash).
- If you’re in the middle of paired parentheses (or square or curly brackets), Python doesn’t squawk about line endings.
- Four spaces to indent each subsection. Don't use tabs or go back and forth between spaces and tabs because it messes up the indent count.
- *Truthiness* refers to Truthy values are values that evaluate to True in a boolean context. Falsy values are values that evaluate to False in a boolean context. Falsy values include empty sequences (lists, tuples, strings, dictionaries, sets), zero in every numeric type, None , and False.
- Whenever you need to make a lot of comparisons like that, separated by *or*, use Python’s membership operator *in*.

## Chapter 5: Text Strings

- Most programmers work with strings of text more often than numbers.Logical (and creative!) thinking is often more important than math skills.
- Strings are our first example of a Python sequence. In this case, they’re a sequence of characters.
- Unlike other languages, strings in Python are immutable. You can’t change a string in place, but you can copy parts of strings to another string to get the same effect.

## Chapter 6: Loop with While and For

- Sometimes, we need to do something more than once. We need a **loop**, and Python gives us two choices: **while** and **for**.
- If you want to loop until something occurs, but you’re not sure when that might happen, you can use an infinite loop with a **break** statement.
- If the **while** loop ended normally (no break call), control passes to an optional **else**. You use this when you’ve coded a while loop to check for something, and breaking as soon as it’s found.
- This use of else might seem nonintuitive. Consider it a **break checker**.
- **Iterators** make it possible for you to traverse data structures without knowing how large they are or how they are implemented.
- A **break** in a **for** loop breaks out of the loop, as it does for a **while** loop.
- Inserting a **continue** in a **for** loop jumps to the next iteration of the loop, as it does for a **while** loop.
- Similar to **while**, for has an optional **else** that checks whether the for completed normally. If break was **not** called, the **else** statement is run.
- The **range()** function returns a stream of numbers within a specified range. without first having to create and store a large data structure such as a list or tuple.

## Chapter 7: Tuples and Lists

- Most computer languages can represent a sequence of items indexed by their integer position: first, second, and so on down to the last.
- **Tuples** are immutable; when you assign elements (only once) to a tuple, they’re baked in the cake and can’t be changed. **Lists** are mutable, meaning you can insert and delete elements with great enthusiasm.
- **Tuple unpacking** lets you assign multiple variables at once.
- **Lists** are good for keeping track of things by their order, especially when the order and contents might change. Unlike strings, lists are mutable. You can change a list in place, add new elements, and delete or replace existing elements. The same value can occur more than once in a list.
- Python’s list() function also converts other **iterable** data types (such as tuples, strings, sets, and dictionaries) to lists.
-  You can extract a subsequence of a list by using a **slice**.
- The traditional way of adding items to a list is to **append()** them one by one to the end.
- When you want to add an item before any offset in the list, use **insert()**.
- Duplicate a string’s characters with * (e.g., >>> ['blah'] * 3 equals >>> ['blah', 'blah', 'blah']).
- You can merge one list into another by using **extend()**.
- Change items in a list with **offset** and **slice**.
- Delete an item by offset with **del**. **del** is a Python **statement**, not a list method.
- Can remove items in a list with **remove()**.
- You can get an item from a list and delete it from the list at the same time by using **pop()**.
- If you use append() to add new items to the end and pop() to remove them from the same end, you’ve implemented a data structure known as a LIFO (last in, first out) queue. This is more commonly known as a stack. pop(0) would create a FIFO (first in, first out) queue. These are useful when you want to collect data as they arrive and work with either the oldest first (FIFO) or the newest first (LIFO).
- If you want to know the offset of an item in a list by its value, use **index()**.
- The Pythonic way to check for the existence of a value in a list is using **in**.
- To count how many times a particular value occurs in a list, use **count()**.
- Convert a list to a string with **join()**.
- Reorder items in a list with **sort()** or **sorted()**.
- Get length of list with **len()**.
- Copy with **copy()**, **list()**, or a **slice()**. Copy everything in a list with **deepcopy()**.
- Compare lists with operators (e.g., ==, <).
- Iterate through a list with **for** and **in**.
- **break** ends the **for** loop and **continue** steps to the next iteration.
- There’s one more nice iteration trick: iterating over multiple sequences in parallel by using the **zip()** function.
- Create a list with comprehension. List comprehension incorporates the **for**/**in** iteration.
- Lists can contain other lists.

## Chapter 8: Dictionaries and Sets

- A **dictionary** is similar to a list, but the order of items doesn’t matter, and they aren’t selected by an offset such as 0 or 1. Instead, you specify a unique **key** to associate with each **value**.
- Dictionaries are mutable, so you can add, delete, and change their key-value elements.
- In Python, a dictionary is also called a **dict** to save syllables. 
- To create a dictionary, you place curly brackets ({}) around comma-separated **key** : **value** pairs. 
- You can also create a dictionary by passing named arguments and values to the dict() function.
- You can also use the dict() function to convert two-value sequences into a dictionary.
- Adding an item to a dictionary is easy. Just refer to the item by its key and assign a value. If the key was already present in the dictionary, the existing value is replaced by the new one. If the key is new, it’s added to the dictionary with its value.
- Remember that dictionary keys must be unique.
- You can use **keys()** to get all of the keys in a dictionary.
- When you want to get all the key-value pairs from a dictionary, use the **items()** function.
- Starting with Python 3.5, there’s a new way to merge dictionaries, using the ** unicorn glitter.
- You can use the **update()** function to copy the keys and values of one dictionary into another.
- A **set** is like a dictionary with its values thrown away, leaving only the keys. As with a dictionary, each key must be unique. You use a set when you only want to know that something exists, and nothing else about it.

## Chapter 9: Functions