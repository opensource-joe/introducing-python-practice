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

*Need to do Ch4 exercises - https://learning.oreilly.com/library/view/introducing-python-2nd/9781492051374/ch04.html#:-:text=Things%20to%20Do

## Chapter 5: Text Strings

- Most programmers work with strings of text more often than numbers.Logical (and creative!) thinking is often more important than math skills.
- Strings are our first example of a Python sequence. In this case, they’re a sequence of characters.
- Unlike other languages, strings in Python are immutable. You can’t change a string in place, but you can copy parts of strings to another string to get the same effect.

*Need to do Ch5 exercise - https://learning.oreilly.com/library/view/introducing-python-2nd/9781492051374/ch05.html#:-:text=Things%20to%20Do

## Chapter 6: Loop with While and For

- Sometimes, we need to do something more than once. We need a **loop**, and Python gives us two choices: **while** and **for**.
- If you want to loop until something occurs, but you’re not sure when that might happen, you can use an infinite loop with a **break** statement.
- If the **while** loop ended normally (no break call), control passes to an optional **else**. You use this when you’ve coded a while loop to check for something, and breaking as soon as it’s found.
- This use of else might seem nonintuitive. Consider it a **break checker**.
- **Iterators** make it possible for you to traverse data structures without knowing how large they are or how they are implemented.
- A **break** in a **for** loop breaks out of the loop, as it does for a **while** loop.
- Inserting a **continue** in a **for** loop jumps to the next iteration of the loop, as it does for a **while** loop.
- Similar to **while**, for has an optional **else** that checks whether the for completed normally. If break was **not** called, the **else** statement is run.