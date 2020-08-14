"""
Exercise 2 part 3
0 points possible (ungraded)
ESTIMATED TIME TO COMPLETE: 7 minutes
Note that you will have to answer all questions before you can click the Check
button.

For each of the expressions below, specify its type and value. If it generates
an error, select type 'NoneType' and write the word 'error' (note this is a
word, not a string, no quotes) in the box for the value. While you could simply
type these expressions into your IDE, we encourage you to answer them directly
since this will help reinforce your understand of basic Python expressions.

Assume we've made the following assignments:

"""

str1 = 'hello'
str2 = ','
str3 = 'world'

print(type('HELLO' == str1))
print('HELLO' == str1)

print(type('a' in str3))
print('a' in str3)

str4 = str1 + str3 # definida uma nova variável
'low' in str4
print(type('low' in str4))
print('low' in str4)

print(type(str3[1:3]))
print(str3[1:3])

print(type(str3[:3]))
print(str3[:3])