# Exercise 4.1
# secret = 4
# guess = 2
# if guess < secret:
#     print('too low')
# elif guess > secret:
#     print('too high')
# else:
#     print('just right')

# Exercise 4.2
# Assign true or false variables to small and green. Write some if/else statements to print which of these matches those: cherry, pea, watermelon, pumpkin.
# cherry: False, False
# pea: True, True
# watermelon: False, True
# pumpkin: False, False

small = True
green = True

if small & green:
    print('you are a pea')
elif green:
    print('you are a watermelon')
else:
    print('you are a cherry or pumpkin')
