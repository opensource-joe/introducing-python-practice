# https://learning.oreilly.com/library/view/introducing-python-2nd/9781492051374/ch12.html#:-:text=Things%20to%20Do

# 12.1 Create a Unicode string called mystery and assign it the value '\U0001f984'. Print mystery and its Unicode name.

# import unicodedata
# mystery = '\U0001f984'
# print(mystery)
# print(unicodedata.name(mystery))

# 12.2 Encode mystery, this time using UTF-8, into the bytes variable pop_bytes. Print pop_bytes.

# pop_bytes = mystery.encode('utf-8')
# print(pop_bytes)

# 12.3 Using UTF-8, decode pop_bytes into the string variable pop_string. Print pop_string. Is pop_string equal to mystery?

# pop_string = pop_bytes.decode('utf-8')
# print(pop_string)

# 12.4 When you’re working with text, regular expressions come in very handy. We’ll apply them in a number of ways to our featured text sample. It’s a poem titled “Ode on the Mammoth Cheese,” written by James McIntyre in 1866 in homage to a seven-thousand-pound cheese that was crafted in Ontario and sent on an international tour. If you’d rather not type all of it, use your favorite search engine and cut and paste the words into your Python program, or just grab it from Project Gutenberg. Call the text string mammoth. - located in mammoth.txt

# import mammoth
# file name.variable name
# mammoth_text = mammoth.mammoth 
# print(mammoth_text)

# 12.5 Import the re module to use Python’s regular expression functions. Use the re.findall() to print all the words that begin with c.

# import re
# # variable source from answer 12.4
# source = mammoth_text
# out = re.findall('[c]\w+', source)
# print(out)

# 12.6 Find all four-letter words that begin with c.

# import re
# # variable source from answer 12.4
# source = mammoth_text
# out = re.findall(r'\bc\w{3}\b', source)
# print(out)

# 12.7 Find all the words that end with r.

# import re
# # variable source from answer 12.4
# source = mammoth_text
# out = re.findall(r'\b\w*r\b', source)
# print(out)

# 12.8 Find all words that contain exactly three vowels in a row.

# import re
# # variable source from answer 12.4
# source = mammoth_text
# out = re.findall(r'\b\w*[aeiou]{3}[^aeiou\s]*\w*\b', source)
# print(out)

# 12.9 Use unhexlify to convert this hex string (combined from two strings to fit on a page) to a bytes variable called gif:

# '47494638396101000100800000000000ffffff21f9' +
# '0401000000002c000000000100010000020144003b'

# import binascii
# hex_str = '47494638396101000100800000000000ffffff21f9' + '0401000000002c000000000100010000020144003b'
# gif = binascii.unhexlify(hex_str)
# print(len(gif))

# 12.10 The bytes in gif define a one-pixel transparent GIF file, one of the most common graphics file formats. A legal GIF starts with the ASCII characters GIF89a. Does gif match this?

# print(gif[:6] == b'GIF89a')

# 12.11 The pixel width of a GIF is a 16-bit little-endian integer beginning at byte offset 6, and the height is the same size, starting at offset 8. Extract and print these values for gif. Are they both 1?

# import struct
# width, height = struct.unpack('<HH', gif[6:10])
# print(width, height)

# This wine has an umlaut in Germany, but loses it in Alsace on the way to France.

# Base 16, specified with characters 0-9 and A-F.

# See the HTML5 named-character reference chart.