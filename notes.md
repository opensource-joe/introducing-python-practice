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

## Chapter 13: Calendars and Clocks

- Python’s standard library has many date and time modules, including: datetime, time, calendar, dateutil, and others.
- The standard datetime module handles (which should not be a surprise) dates and times. It defines four main object classes, each with many methods:
    - date for years, months, and days
    - time for hours, minutes, seconds, and fractions
    - datetime for dates and times together
    - timedelta for date and/or time intervals
- One way to represent an absolute time is to count the number of seconds since some starting point. Unix time uses the number of seconds since midnight on January 1, 1970.1 This value is often called the epoch, and it is often the simplest way to exchange dates and times among systems.
- Epoch values are a useful least-common denominator for date and time exchange with different systems, such as JavaScript. Sometimes, though, you need actual days, hours, and so forth, which time provides as struct_time objects. localtime() provides the time in your system’s time zone, and gmtime() provides it in UTC.
- Wherever possible, use UTC instead of time zones. UTC is an absolute time, independent of time zones. If you have a server, set its time to UTC; do not use local time.
- Never use daylight savings time if you can avoid it.

## Chapter 14: Files and Directories

- A file is a sequence of bytes, stored in some filesystem, and accessed by a filename. A directory is a collection of files, and possibly other directories. The term folder is a synonym for directory.
- Many filesystems are hierarchical, and often referred to as being like a tree.
- The simplest kind of persistence is a plain old file, sometimes called a flat file. You read from a file into memory and write from memory to a file.
- You need to call the open function before you do the following:
    - Read an existing file
    - Write to a new file
    - Append to an existing file
    - Overwrite an existing file
- fileobj = open( filename, mode )
- An alternative to reading and writing a file is to memory-map it with the standard mmap module. This makes the contents of a file look like a bytearray in memory.
- In most operating systems, files exist in a hierarchy of directories (often called folders). The container of all of these files and directories is a filesystem (sometimes called a volume). The standard os module deals with operating specifics such as these and provides the following functions with which you can manipulate them.
- When you want to refer to a specific file or directory, you need its pathname: the sequence of directories needed to get there, either absolute from the top (the root), or relative to your current directory.

## Chapter 15: Data in Time - Processes and Concurrency

- When you run an individual program, your operating system creates a single process. It uses system resources (CPU, memory, disk space) and data structures in the operating system’s kernel (file and network connections, usage statistics, and so on). A process is isolated from other processes.
- The multiprocessing module has more bells and whistles than a clown on a calliope. It’s really intended for those times when you need to farm out some task to multiple processes to save overall time; for example, downloading web pages for scraping, resizing images, and so on. It includes ways to queue tasks, enable intercommunication among processes, and wait for all the processes to finish.
- A queue is like a list: things are added at one end and taken away from the other. The most common is referred to as FIFO (first in, first out).
- In general, queues transport messages, which can be any kind of information.
- You can implement queues in many ways. For a single machine, the standard library’s multiprocessing module (which you saw earlier) contains a Queue function.
- There are other queue types in the multiprocessing module, and you can read the documentation for more examples.
- A thread runs within a process with access to everything in the process.
- One difference between multiprocessing and threading is that threading does not have a terminate() function. There’s no easy way to terminate a running thread, because it can cause all sorts of problems in your code, and possibly in the space-time continuum itself.
- So for Python, the recommendations are as follows:
    - Use threads for I/O-bound problems
    - Use processes, networking, or events (discussed in the next section) for CPU-bound problems
- You can use concurrent.futures any time you want to launch a bunch of concurrent tasks, such as the following:
    - Crawling URLs on the web
    - Processing files, such as resizing images
    - Calling service APIs
    - As usual, the docs provide additional details, but are much more technical.

## Chapter 16: Data in a Box - Persistent Storage

- An active program accesses data stored in Random Access Memory, or RAM.
- As programmers, we need persistence: storing and retrieving data using nonvolatile media such as disks.
- A record is a term for one chunk of related data, consisting of individual fields.
- The simplest persistence is a plain old flat file. This works well if your data has a very simple structure and you exchange all of it between disk and memory. Plain text data might be suitable for this treatment.
- If you want to exchange data structures among programs, you need a way to encode hierarchies, sequences, sets, and other structures as text. XML is a prominent markup format that does this.
- JavaScript Object Notation (JSON) has become a very popular data interchange format, beyond its JavaScript origins. The JSON format is a subset of JavaScript, and often legal Python syntax, as well. Its close fit to Python makes it a good choice for data interchange among programs.
- Similar to JSON, YAML has keys and values, but handles more data types such as dates and times. The standard Python library does not yet include YAML handling, so you need to install a third-party library named yaml to manipulate it.
- This is as good place as any to introduce pandas—a Python library for structured data.
- It’s especially useful for heavy numeric work with NumPy, and data preparation for machine learning.
- Relational databases are only about 40 years old but are ubiquitous in the computing world.
- These are called relational because they show relationships among different kinds of data in the form of rectangular tables.
- A table is a rectangular grid of columns (data fields) and rows (individual data records), similar to a spreadsheet. The intersection of a row and column is a table cell.
- A column or group of columns is usually the table’s primary key; its values must be unique in the table. This prevents adding the same data to the table more than once. This key is indexed for fast lookups during queries.
- Each table lives within a parent database, like a file within a directory.
- The word database is used in multiple ways: as the server, the table container, and the data stored therein. If you’ll be referring to all of them at the same time, it might help to call them database server, database, and data.
- SQL is not an API or a protocol, but a declarative language: you say what you want rather than how to do it. It’s the universal language of relational databases. SQL queries are text strings sent by a client to the database server, which in turn figures out what to do with them.
- There are two main categories of SQL statements:
    - DDL (data definition language) - Handles creation, deletion, constraints, and permissions for tables, databases, and users.
    - DML (data manipulation language) - Handles data insertions, selects, updates, and deletions.
- An application programming interface (API) is a set of functions that you can call to get access to some service. DB-API is Python’s standard API for accessing relational databases.
- SQLite is a good, light, open source relational database. It’s implemented as a standard Python library, and stores databases in normal files.
- MySQL is a very popular open source relational database. Unlike SQLite, it’s an actual server, so clients can access it from different devices across the network.
- PostgreSQL is a full-featured open source relational database. Indeed in many ways, it’s more advanced than MySQL.
- Some nonrelational databases have been written to allow more flexible data definitions as well as to process very large data sets or support custom data operations.
- The simplest type of NoSQL databases are key-value stores.
- Redis is a data structure server. It handles keys and their values, but the values are richer than those in other key-value stores.
- A document database is a NoSQL database that stores data with varying fields.
- You could handle data like this in memory with Python dictionaries and lists, or store it as JSON files.
- Time series data may be collected at fixed intervals (such as computer performance metrics) or at random times, which has led to many storage methods.
- For our last case of data that need its own database category, we have graphs: nodes (data) connected by edges or vertices (relationships).

## Chapter 17: Data in Space - Networks

- Concurrency: how to do more than one thing at a time.
- Trying to do things in more than one place: distributed computing or networking.
- The internet is based on rules about how to make connections, exchange data, terminate connections, handle timeouts, and so on. These are called protocols, and they are arranged in layers.
- TCP sets up a secret handshake between sender and receiver to ensure a good connection.
- The lowest level of network programming uses a socket, borrowed from the C language and the Unix operating system.
- You can build networking applications from some basic patterns:
    - The most common pattern is request-reply, also known as request-response or client-server. This pattern is synchronous: the client waits until the server responds.
    - Another common pattern is push, or fanout: you send data to any available worker in a pool of processes.
    - Another common pattern is push, or fanout: you send data to any available worker in a pool of processes.
    - One pattern is similar to radio or television broadcasting: publish-subscribe, or pub-sub. With this pattern, a publisher sends out data. In a simple pub-sub system, all subscribers would receive a copy.
- The Domain Name System (DNS) is a critical internet service that converts IP addresses to and from names via a distributed database.
- If data is published only on a website, anyone who wants to access and structure the data needs to write scrapers (as shown in “Crawl and Scrape”), and rewrite them each time a page format changes.
- In contrast, if a website offers an API to its data, the data becomes directly available to client programs.
- The easiest API is a web interface, but one that provides data in a structured format such as JSON or XML rather than plain text or HTML. The API might be minimal or a full-fledged RESTful API (defined in “Web APIs and REST”), but it provides another outlet for those restless bytes.
- JSON is a popular serialization format, especially with web RESTful systems, but it can’t express all Python data types directly. Also, as a text format it tends to be more verbose than some binary serialization methods.
- Python provides the pickle module to save and restore any object in a special binary format.
- Remote Procedure Calls (RPCs) look like normal functions but execute on remote machines across a network. Instead of calling a RESTful API with arguments encoded in the URL or request body, you call an RPC function on your own machine.
- As Google and other internet companies grew, they found that traditional computing solutions didn’t scale. Software that worked for single machines, or even a few dozen, could not keep up with thousands.
- Disk storage for databases and files involved too much seeking, which requires mechanical movement of disk heads.
- Developers found that it was faster to distribute and analyze data on many networked machines than on individual ones. They could use algorithms that sounded simplistic but actually worked better overall with massively distributed data.
- After Google published its MapReduce results in a paper, Yahoo followed with an open source Java-based package named Hadoop.
- The phrase big data applies here. Often it just means “data too big to fit on my machine”: data that exceeds the disk, memory, CPU time, or all of the above. To some organizations, if big data is mentioned somewhere in a question, the answer is always Hadoop. Hadoop copies data among machines, running them through map (scatter) and reduce (gather) programs, and saving the results on disk at each step.
- A quicker method called Hadoop streaming works like Unix pipes, streaming the data through programs without requiring disk writes at each step. You can write Hadoop streaming programs in any language, including Python.
- Many Python modules have been written for Hadoop, and some are discussed in the blog post “A Guide to Python Frameworks for Hadoop”.
- A rival named Spark was designed to run 10 to 100 times faster than Hadoop. It can read and process any Hadoop data source and format. Spark includes APIs for Python and other languages. You can find the installation documents online.
The eight fallacies of distributed computing, according to Peter Deutsch, are as follows:
    - The network is reliable.
    - Latency is zero.
    - Bandwidth is infinite.
    - The network is secure.
    - Topology doesn’t change.
    - There is one administrator.
    - Transport cost is zero.
    - The network is homogeneous.
- OpenStack is an open source framework of Python services and REST APIs.

## Chapter 18: The Web, Untangled

- Python is a particularly good language for web work at every level:
    - Clients, to access remote sites
    - Servers, to provide data for websites and web APIs
    - Web APIs and services, to interchange data in other ways than viewable web pages
- The curl program is probably the most popular command-line web client. Documentation includes the book Everything Curl.
- In Python 2, web client and server modules were a bit scattered. One of the Python 3 goals was to bundle these modules into two packages: 1) http, 2)urllib.
- I think web client development with requests is easier. You can browse the documentation (which is pretty good) for full details.
- Web developers have found Python to be an excellent language for writing web servers and server-side programs. This has led to such a variety of Python-based web frameworks.
- A web framework provides features with which you can build websites.
- Web servers handle the HTTP and WSGI details, but you use web frameworks to actually write the Python code that powers the site.
- The web and databases are the peanut butter and jelly of computing: where you find one, you’ll eventually find the other. In real-life Python applications, at some point you’ll probably need to provide a web interface (site and/or API) to a relational database.
- Often, data is available only within web pages. If you want to access it, you need to access the pages through a web browser and read it.
- Representational State Transfer (REST) was defined by Roy Fielding in his doctoral thesis. Many products claim to have a REST interface or a RESTful interface. In practice, this often only means that they have a web interface—definitions of URLs to access a web service.
- A RESTful service uses the HTTP verbs in specific ways:
    - HEAD gets information about the resource, but not its data.
    - GET retrieves the resource’s data from the server. This is the standard method used by your browser. GET should not be used to create, change, or delete data.
    - POST creates a new resource.
    - PUT replaces an existing resource, creating it if it doesn’t exist.
    - PATCH partially updates a resource.
    - DELETE deletes. Truth in advertising!
- Sometimes, you might want a little bit of information—a movie rating, stock price, or product availability—but what you need is available only in HTML pages.
- An automated web fetcher is called a crawler or spider.4 After the contents have been retrieved from the remote web servers, a scraper parses it to find the needle in the haystack.
- If you need an industrial-strength combined crawler and scraper, Scrapy is worth downloading.
- Scrapy is a framework, not just a module such as BeautifulSoup. It does more, but it’s more complex to set up. To learn more about Scrapy, read “Scrapy at a Glance” and the tutorial.
- If you already have the HTML data from a website and just want to extract data from it, BeautifulSoup is a good choice. HTML parsing is harder than it sounds. This is because much of the HTML on public web pages is technically invalid: unclosed tags, incorrect nesting, and other complications. If you try to write your own HTML parser by using regular expressions (discussed in “Text Strings: Regular Expressions”) you’ll soon encounter these messes.
- Kenneth Reitz, the author of the popular web client package requests, has written a new scraping library called requests-html.

## Chapter 19: Be a Pythonista

- When you need to develop some code, the fastest solution is to steal it…from a source that allows it.
- The Python standard library is wide, deep, and mostly clear. Dive in and look for those pearls.
- The first place to look is the Python Package Index (PyPI).
- Another popular repository is GitHub. See what Python packages are currently trending.
- Popular Python recipes has more than four thousand short Python programs, on every subject.
- Jupyter is an evolution of IPython. The name combines the languages Julia, Python, and R—all of which are popular in data science and scientific computing. Jupyter Notebooks are a modern way to develop and publish your code with documentation for any of these languages.
- JupyterLab is the next generation of Jupyter Notebook and will eventually replace it.
- Static languages require you to define the types of your variables, and they can catch some errors at compile time. As you know, Python doesn’t do this, and you can encounter bugs only when the code is run.
- The very simplest way to test Python programs is to add print() statements.
- The next step, before creating actual test programs, is to run a Python code checker. The most popular are pylint and pyflakes.
- Move on to actual tests of the logic in your program.
- It’s a good practice to write independent test programs first, to ensure that they all pass before you commit your code to any source control system.
- The standard library contains not one, but two test packages. Let’s start with unittest.
- The second test package in the standard library is doctest. With this package, you can write tests within the docstring itself, also serving as documentation.
- Test first. The better your tests are, the less you’ll have to fix later. Yet, bugs happen and need to be fixed when they’re found later.
- When code breaks, it’s usually because of something you just did. So you typically debug “from the bottom up,” starting with your most recent changes.
- The simplest way to debug in Python is to print out strings. Some useful things to print include vars(), which extracts the values of your local variables, including function arguments.
- If your code also includes normal prints to standard output, you can write your debugging messages to standard error output with print(stuff, file=sys.stderr).
- As you read in “Decorators”, a decorator can call code before or after a function without modifying the code within the function itself. This means that you can use a decorator to do something before or after any Python function, not just ones that you wrote.
- Use of the standard Python debugger, pdb.
- There’s a new built-in function called breakpoint(). If you add it to your code, a debugger will automatically start up and pause at each location.
- The standard Python library module is logging.
- A quick way of timing something is to get the current time, do something, get the new time, and then subtract the original time from the new time.

## Three Remaining Chapters (domain specific)
- Chapter 20: Py Art
- Chapter 21: Py at Work
- Chapter 22: Py Sci