# https://learning.oreilly.com/library/view/introducing-python-2nd/9781492051374/ch05.html#:-:text=Things%20to%20Do

# Exercise 5.1
# Capitalize the word starting with m
# song = "When an eel grabs your arm, And it causes great harm, That's a moray!"
# print(song.replace('moray', 'Moray'))

# Exercise 5.2
# questions = [
#     "We don't serve strings around here. Are you a string?",
#     "What is said on Father's Day in the forest?",
#     "What makes the sound 'Sis! Boom! Bah!'?"
# ]
# answers = [
#     "An exploding sheep.",
#     "No, I'm a frayed knot.",
#     "'Pop!' goes the weasel."
# ]
# for (a, b) in zip(questions, answers):
#     print(a, b)

# Exercise 5.3
# Write the following poem by using old-style formatting. Substitute the strings: 'roast beef', 'ham', 'head' and 'clam' in this string.
# red_meat = 'roast beef'
# pork = 'ham'
# body_top = 'head'
# seafood = 'clam'

# print('My kitty cat likes %s,' % red_meat + '\n'
# 'My kitty cat likes %s,' % pork + '\n'
# 'My kitty cat likes %s,' % body_top + '\n'
# 'And now thinks he\'s a %s' % seafood + '.'
# )

# Exercise 5.4
# Write a form letter by using new-style formatting. Save the following string as **letter**
# salutation = 'Doctor'
# name = 'Joseph Castle'
# product = 'electric heater'
# verbed = 'exploded'
# room = 'living room'
# animals = 'cats'
# amount = '$1,000'
# percent = 90
# spokesman = 'Thomas Shelby'
# job_title = 'Shelby Clan Leader'

# letter = f"""

# Dear {salutation} {name},

# Thank you for your letter. We are sorry that our {product}
# {verbed} in your {room}. Please note that it should never
# be used in a {room}, especially near any {animals}.

# Send us your receipt and {amount} for shipping and handling.
# We will send you another {product} that, in our tests,
# is {percent}% less likely to have {verbed}.

# Thank you for your support.

# Sincerely,
# {spokesman}
# {job_title}

# """
# print(letter)

# Exercise 5.5
# Assign values to variable strings named 'salutation', 'name', 'product', 'verbed' (past tense verb), 'room', 'animals', 'percent', 'spokesman', and 'job_title'. Print **letter** with these values using letter.format().

# letter = """

# Dear {salutation} {name},

# Thank you for your letter. We are sorry that our {product}
# {verbed} in your {room}. Please note that it should never
# be used in a {room}, especially near any {animals}.

# Send us your receipt and {amount} for shipping and handling.
# We will send you another {product} that, in our tests,
# is {percent}% less likely to have {verbed}.

# Thank you for your support.

# Sincerely,
# {spokesman}
# {job_title}

# """
# print(letter.format(salutation="Mister", name="Dave Smith", product="radiator", verbed='died', room='bedroom', animals='fish', amount='$90', percent=20, spokesman="Aubrey Hunt", job_title="Grand Inquisitor"))

# Exercise 5.6
# After public polls to name things, a pattern emerged: an English submarine (Boaty McBoatface), an Australian racehorse (Horsey McHorseface), and a Swedish train (Trainy McTrainface). Use % formatting to print the winning name at the state fair for a prize duck, gourd, and spitz.
# duck = 'Boaty McBoatface'
# gourd = 'Horsey McHorseface'
# spitz = 'Trainy McTrainface'

# print(f'The winning horse for a duck is {duck}.')
# print(f'The winning horse for a gourd is {gourd}.')
# print(f'The winning horse for a spitz is {spitz}.')

# Exercise 5.7
# Do the same as 5.6 with format() formatting.

# print('A winning horse for a duck is {duck}.'.format(duck='Boaty McBoatface') + '\n'
# 'A winning horse for a gourd is {gourd}.'.format(gourd='Horsy McHorseface') + '\n'
# 'A winning horse for a spitz is {spitz}.'.format(spitz='Trainy McTrainface')
# )

# Exercise 5.8
# Once more, with feeling, and f strings

# duck = 'Boaty McBoatface'
# gourd = 'Horsey McHorseface'
# spitz = 'Trainy McTrainface'
# feeling = 'excited'

# print(f'The winning horse for a duck is an {feeling} {duck}.')
# print(f'The winning horse for a gourd is an {feeling} {gourd}.')
# print(f'The winning horse for a spitz is an {feeling} {spitz}.')