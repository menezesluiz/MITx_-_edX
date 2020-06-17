"""
As we'll see in subsequent lectures, everything in Python is an object.
Objects are special because we can associate special functions, referred to as
object methods, with the object. In this problem you'll be working with string
objects, and their built-in methods.

As we'll see in subsequent lectures, everything in Python is an object.
Objects are special because we can associate special functions, referred to as
object methods, with the object. In this problem you'll be working with string
objects, and their built-in methods.
>>> s = 'abc'
>>> s.capitalize
<built-in method capitalize of str object at 0x104c35878>
>>> s.capitalize()
'Abc'

"""

str1 = 'exterminate!'
str2 = 'number one - the larch'

"""
str1.upper

str1.upper()

str1

str1.isupper()

str1.islower()

str2 = str2.capitalize()
str2

str2.swapcase()

str1.index('e')

str2.index('n')

str2.find('n')

str2.index('!')

str2.find('!')
"""
Note: Be sure to make note of the difference between the find and index
string methods...
"""
str1.count('e')

str1 = str1.replace('e', '*')
str1

str2.replace('one', 'seven')
"""