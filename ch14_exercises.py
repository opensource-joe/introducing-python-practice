# https://learning.oreilly.com/library/view/introducing-python-2nd/9781492051374/ch14.html#:-:text=Things%20to%20Do

# 14.1 List the files in your current directory.

import os

# path = '/Users/jorcas/Development/introducing-python-practice'
# dir_list = os.listdir(path)
# print(path)
# print(dir_list)

print(os.listdir('.'))

# 14.2 List the files in your parent directory.

# parent_path = '/Users/jorcas/Development'
# dir_list_two = os.listdir(path)
# print(parent_path)
# print(dir_list_two)

os.listdir('..')

# 14.3 Assign the string 'This is a test of the emergency text system' to the variable test1, and write test1 to a file called test.txt.

test1 = 'This is a test of the emergency text system'
# with open('test.txt', 'wt') as output:
#     print(test1, file=output)
outfile = open('test.txt', 'wt')
outfile.write(test1)
outfile.close()

# 14.4 Open the file test.txt and read its contents into the string test2. Are test1 and test2 the same?

with open ('test.txt', 'rt') as infile:
    test2 = infile.read()

print(test2)
