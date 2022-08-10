# https://learning.oreilly.com/library/view/introducing-python-2nd/9781492051374/ch07.html#:-:text=Things%20to%20Do

# 7.1 Create a list called years_list, starting with the year of your birth, and each year thereafter until the year of your fifth birthday. For example, if you were born in 1980, the list would be years_list = [1980, 1981, 1982, 1983, 1984, 1985]. If you’re less than five years old and reading this book, I don’t know what to tell you.

# years_list = [1975, 1976, 1977, 1978, 1979]

# 7.2 In which year in years_list was your third birthday? Remember, you were 0 years of age for your first year.

# print(years_list[3])

# 7.3 In which year in years_list were you the oldest?

# print(years_list[4])

# 7.4 Make a list called things with these three strings as elements: "mozzarella", "cinderella", "salmonella".

# things = ["mozzarella", "cindarella", "salmonella"]

# 7.5 Capitalize the element in things that refers to a person and then print the list. Did it change the element in the list?

# things[1] = things[1].capitalize()

# 7.6 Make the cheesy element of things all uppercase and then print the list.

# things[0] = things[0].upper()
# print(things)

# 7.7 Delete the disease element from things, collect your Nobel Prize, and print the list.

# del things[2]
# print(things)

# 7.8 Create a list called surprise with the elements "Groucho", "Chico", and "Harpo".

# surprise = ['Groucho', 'Chico', 'Harpo']

# 7.9 Lowercase the last element of the surprise list, reverse it, and then capitalize it.

# surprise[-1] = surprise[-1].lower()
# surprise[-1] = surprise[-1][::-1]
# surprise[-1].capitalize()
# print(surprise[-1])

# 7.10 Use a list comprehension to make a list called even of the even numbers in range(10).

even = [number for number in range(2, 11, 2)]
print(even)

# 7.11 Let’s create a jump rope rhyme maker. You’ll print a series of two-line rhymes. Start with this program fragment:

# start1 = ["fee", "fie", "foe"]
# rhymes = [
#     ("flop", "get a mop"),
#     ("fope", "turn the rope"),
#     ("fa", "get your ma"),
#     ("fudge", "call the judge"),
#     ("fat", "pet the cat"),
#     ("fog", "walk the dog"),
#     ("fun", "say we're done"),
#     ]
# start2 = "Someone better"
# For each tuple (first, second) in rhymes:

# For the first line:
# Print each string in start1, capitalized and followed by an exclamation point and a space.
# Print first, also capitalized and followed by an exclamation point.

# For the second line:
# Print start2 and a space.
# Print second and a period.