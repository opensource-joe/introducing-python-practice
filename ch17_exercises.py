# https://learning.oreilly.com/library/view/introducing-python-2nd/9781492051374/ch17.html#:-:text=Things%20to%20Do

# Skipped b/c more advanced and not presently needed.

# 17.1 Use a plain socket to implement a current-time-service. When a client sends the string time to the server, return the current date and time as an ISO string.

# 17.2 Use ZeroMQ REQ and REP sockets to do the same thing.

# 17.3 Try the same with XMLRPC.

# 17.4 You may have seen the classic I Love Lucy television episode in which Lucy and Ethel worked in a chocolate factory. The duo fell behind as the conveyor belt that supplied the confections for them to process began operating at an ever-faster rate. Write a simulation that pushes different types of chocolates to a Redis list, and Lucy is a client doing blocking pops of this list. She needs 0.5 seconds to handle a piece of chocolate. Print the time and type of each chocolate as Lucy gets it, and how many remain to be handled.

# 17.5 Use ZeroMQ to publish the poem from exercise 12.4 (from Example 12-1), one word at a time. Write a ZeroMQ consumer that prints every word that starts with a vowel, and another that prints every word that contains five letters. Ignore punctuation characters.