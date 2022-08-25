# https://learning.oreilly.com/library/view/introducing-python-2nd/9781492051374/ch16.html#:-:text=Things%20to%20Do

# 16.1 Save the following text lines to a file called books.csv (notice that if the fields are separated by commas, you need to surround a field with quotes if it contains a comma):

# text = '''
# author,book
# J R R Tolkien,The Hobbit
# Lynne Truss,"Eats, Shoots & Leaves
# '''

# creates test.csv and writes to it
# with open ('test.csv', 'wt') as outfile:
#     outfile.write(text)

# 16.2 Use the csv module and its DictReader method to read books.csv to the variable books. Print the values in books. Did DictReader handle the quotes and commas in the second book’s title?

# import csv

# pulls data from books.csv file
# with open('books.csv', 'rt') as infile:
#     books = csv.DictReader(infile)
#     for book in books:
#         print(book)

# 16.3 Create a CSV file called books2.csv by using these lines:

# text = '''
# title,author,year
# The Weirdstone of Brisingamen,Alan Garner,1960
# Perdido Street Station,China Miéville,2000
# Thud!,Terry Pratchett,2005
# The Spellman Files,Lisa Lutz,2007
# Small Gods,Terry Pratchett,1992
# '''
# with open('books2.csv', 'wt') as outfile:
#     outfile.write(text)

# 16.4 Use the sqlite3 module to create a SQLite database called books.db and a table called books with these fields: title (text), author (text), and year (integer).

# import sqlite3
# db = sqlite3.connect('books.db')
# curs = db.cursor()
# curs.execute('''create table book (title text, author text, year int)''')
# db.commit()

# Skipped the remainder since they are specific to databases with imports and exports

# 16.5 Read books2.csv and insert its data into the book table.

# 16.6 Select and print the title column from the book table in alphabetical order.

# 16.7 Select and print all columns from the book table in order of publication.

# 16.8 Use the sqlalchemy module to connect to the sqlite3 database books.db that you just made in exercise 16.4. As in 16.6, select and print the title column from the book table in alphabetical order.

# 16.9 Install the Redis server and the Python redis library (pip install redis) on your computer. Create a Redis hash called test with the fields count (1) and name ('Fester Bestertester'). Print all the fields for test.

# 16.10 Increment the count field of test and print it