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

- The first step to code reuse is the function: a named piece of code, separate from all others. A function can take any number and type of input parameters and return any number and type of output results.
- You can do two things with a function:
    - Define it, with zero or more parameters
    - Call it, and get zero or more results
- Even for a function with no parameters like this one, you still need the parentheses and the colon in its definition. The next line needs to be indented.
- You call a function just by typing its name and parentheses.
- The values you pass into the function when you call it are known as arguments.
- Arguments outside of the function, but parameters inside.
- If a function doesn’t call return explicitly, the caller gets the result None.
- **None** is a special Python value that holds a place when there is nothing to say.
- This (the difference between None and False) seems like a subtle distinction, but it’s important in Python. You’ll need None to distinguish a missing value from an empty value.
- The most familiar types of arguments are positional arguments, whose values are copied to their corresponding parameters in order.
- Although very common, a downside of positional arguments is that you need to remember the meaning of each position.
- To avoid positional argument confusion, you can specify arguments by the names of their corresponding parameters.
- You can specify default values for parameters.
- When used inside the function with a parameter, an asterisk groups a variable number of positional arguments into a single tuple of parameter values.
- You can use two asterisks (**) to group keyword arguments into a dictionary, where the argument names are the keys, and their values are the corresponding dictionary values.
- You can attach documentation to a function definition by including a string at the beginning of the function body.
- To print a function’s docstring, call the Python help() function.
- Double underscores (aka dunder in Python-speak) are used in many places to name Python internal variables, because programmers are unlikely to use them in their own variable names.
- Functions are first-class citizens in Python. You can assign them to variables, use them as arguments to other functions, and return them from functions.
- An inner function can be useful when performing some complex task more than once within another function, to avoid loops or code duplication.
- An inner function can act as a closure. This is a function that is dynamically generated by another function and can both change and remember the values of variables that were created outside the function.
- A Python **lambda function** is an anonymous function expressed as a single statement. You can use it instead of a normal tiny function.
- A generator is a Python sequence creation object. With it, you can iterate through potentially huge sequences without creating and storing the entire sequence in memory at once. Generators are often the source of data for iterators.
- If you want to create a potentially large sequence, you can write a generator function. It’s a normal function, but it returns its value with a **yield** statement rather than **return**.
- A generator can be run only once. Lists, sets, strings, and dictionaries exist in memory, but a generator creates its values on the fly and hands them out one at a time through an iterator. It doesn’t remember them, so you can’t restart or back up a generator.
- You’ve seen comprehensions for lists, dictionaries, and sets. A generator comprehension looks like those, but is surrounded by parentheses instead of square or curly brackets. It’s like a shorthand version of a generator function.
- A **decorator** is a function that takes one function as input and returns another function.
- A name can refer to different things, depending on where it’s used. Python programs have various **namespaces** — sections within which a particular name is unique and unrelated to the same name in other namespaces.
- Each function defines its own namespace. Consider scope - global vs local variables.
- To access the global variable rather than the local one within a function, you need to be explicit and use the **global** keyword.
- If you don’t say global within a function, Python uses the local namespace and the variable is local. It goes away after the function completes.
- Names that begin and end with two underscores (__) are reserved for use within Python.
- we’ve called functions that do some things directly, and maybe call other functions. But what if a function calls itself?5 This is called recursion. Like an unbroken infinite loop with while or for, you don’t want infinite recursion.
- Recursion is useful when you’re dealing with “uneven” data, like lists of lists of lists.
- Async functions - discussed in Appendix C - use async before def and then an await before function call. The function is asynchronous.
- The main difference between asynchronous and normal functions is that async ones can “give up control” rather than running to completion.
- When things go south,7 Python uses exceptions: code that is executed when an associated error occurs.
- Rather than leaving things to chance, use try to wrap your code, and except to provide the error handling.
- ou can also define your own exception types to handle special situations that might arise in your own programs.

## Chapter 10: Objects and Classes

- An object is a custom data structure containing both data (variables, called attributes) and code (functions, called methods). It represents a unique instance of some concrete thing. Think of objects as nouns and their methods as verbs.
- An attribute is a variable inside a class or object. During and after an object or class is created, you can assign attributes to it. An attribute can be any other object.
- A method is a function in a class or object. A method looks like any other function, but can be used in special ways.
- __init__() is the special Python name for a method that initializes an individual object from its class definition.
- Inheritance: creating a new class from an existing class, but with some additions or changes.
- Inheritance in Python depends on method resolution order.
- Python uses the self argument to find the right object’s attributes and methods.
- Python doesn’t have private attributes, but you can write getters and setters with obfuscated attribute names to get a little privacy. The best solution is to use properties.
- When you see an initial self argument in methods within a class definition, it’s an instance method. These are the types of methods that you would normally write when creating your own classes.
- A class method affects the class as a whole. Any change you make to the class affects all of its objects. Within a class definition, a preceding @classmethod decorator indicates that that following function is a class method.
- A third type of method in a class definition affects neither the class nor its objects; it’s just in there for convenience instead of floating around on its own. It’s a static method, preceded by a @staticmethod decorator, with no initial self or cls parameter.
- Python has a loose implementation of polymorphism; it applies the same operation to different objects, based on the method’s name and arguments, regardless of their class.
- It’s tempting to build elaborate inheritance hierarchies, but sometimes composition or aggregation make more sense.
- A named tuple is a subclass of tuples with which you can access values by name (with .name) as well as by position (with [ offset ]).
- Many people like to create objects mainly to store data (as object attributes), not so much behavior (methods).
- Dataclasses - use from dataclasses import dataclass for additional functionality beyond tuples.

## Chapter 11: Modules, Packages, and Goodies

- Code has a roughly similar bottom-up organization: data types are like words; expressions and statements are like sentences; functions are like paragraphs; and modules are like chapters.
- A module is just a file of any Python code. You don’t need to do anything special—any Python code can be used as a module by others.
- We refer to code of other modules by using the Python import statement. This makes the code and variables in the imported module available to your program.
- The simplest use of the import statement is import module, where module is the name of another Python file, without the .py extension.
- Consider importing from outside the function if the imported code might be used in more than one place, and from inside if you know its use will be limited.
- You can import a whole module or just parts of it.
- To allow Python applications to scale even more, you can organize modules into file and module hierarchies called packages. A package is just a subdirectory that contains .py files. And you can go more than one level deep, with directories inside those.
- Python looks under your current directory for the subdirectory choices and its modules. Actually, it looks in other places, as well, and you can control this.
- You’ve seen that you can package Python modules as:
    - A single module (.py file)
    - A package (directory containing modules, and possibly other packages)
    - You can also split a package across directories with namespace packages.
- When you’re about to write some Python code, it’s often worthwhile to first check whether there’s a standard module that already does what you want. It’s surprising how often you encounter little gems in the standard library.
- Sometimes, the standard library doesn’t have what you need, or doesn’t do it in quite the right way. There’s an entire world of open source, third-party Python software. Good resources include the following:
 - PyPi (also known as the Cheese Shop, after an old Monty Python skit)
    - GitHub
    - readthedocs

## Chapter 12: Wrangle and Mangle Data

- This chapter provides practical techniques for taming data. Sometimes, this is called data munging, or the more businesslike ETL (extract/transform/load) of the database world.
- Data formats fall roughly into two categories: text and binary.
- Unicode is an ongoing international standard to define the characters of all the world’s languages, plus symbols from mathematics and other fields.
- [Unicode Code Charts page](http://www.unicode.org/charts/) has links to all the currently defined character sets with images. The latest version (12.0) defines more than 137,000 characters, each with a unique name and identification number. Python 3.8 handles all of these.
- When you exchange data with the outside world, you need a couple of things:
    - A way to encode character strings to bytes.
    - A way to decode bytes to character strings.
- UTF-8 is the standard text encoding in Python, Linux, and HTML.
- You encode a string to bytes.
- We decode byte strings to Unicode text strings.
- Whenever we get text from some external source (files, databases, websites, network APIs, and so on), it’s encoded as byte strings. The tricky part is knowing which encoding was actually used, so we can run it backward and get Unicode strings.
- Whenever possible, use UTF-8 encoding. It works, is supported everywhere, can express every Unicode character, and is quickly decoded and encoded.
- Python 3.4 added another way to convert to and from Unicode but using HTML character entities.
- Some Unicode characters can be represented by more than one Unicode encoding.
- It’s time to explore more complex pattern matching by using regular expressions. These are provided in the standard module re, which we’ll import. You define a string pattern that you want to match, and the source string to match against.
- Because this is a common Python gotcha, I’ll say it again here: match() only matches a pattern starting at the beginning of the source. search() matches a pattern anywhere in the source.

## Chapter 13 ...