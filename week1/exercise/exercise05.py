"""
Exercise 5
Finger Exercises due Aug 5, 2020 20:30 -03
Completed
 Bookmark this page
Exercise 5
5/5 points (graded)
ESTIMATED TIME TO COMPLETE: 7 minutes

Below are some short Python programs. For each program, answer the associated question.

Try to answer the questions without running the code. Check your answers, then run the code for the ones you get wrong.

This question is going to ask you what some simple loops print out. If you're asked what code like this prints:
"""
# num = 5
# if num > 2:
#     print(num)
#     num -= 1
# print(num)
"""
write what it prints out, separating what appears on a new line by a comma and a space. So the answer for the above 
code would be:

5, 4
If a given loop will not terminate, write the phrase 'infinite loop' in the box.
"""

"""
Note: Using the 'range' built-in function
The standard way of using the range function is to give it a number to stop at, and range will give a sequence of values
that start at 0 and go through the stop value minus 1. For example, calling range(stop) yields the following:

>>> range(5)
range(0,5)
which is the sequence 0, 1, 2, 3, 4.
However, we can call range with some additional, optional parameters - a value to start at, and a step size. You can
specify a start value by calling range(start, stop), like this:

>>> range(2, 5)
range(2, 5)
which is the sequence of values 2, 3, 4
To specify a step size, you must specify a start value - the call is range(start, stop, stepSize), like this:

>>> range(2, 10, 2)
range(2, 10, 2)
which gives the sequence of values 2, 4, 6, 8
Note that these parameters - start, stop, stepSize - are the same parameters that you can use when slicing a string:

>>> s = "Hello, world!"
>>> s[1:] # s[start:]
ello, world!
>>> s[1:10] # s[start:stop]
ello, wor
>>> s[1:10:3] # s[start:stop:stepSize]
eow
In this problem you'll get more practice on using range. You can also see more examples of 'range' here.
"""

num = 10  # essa variável não interfere em nada o resultado final do código, é uma variável nula
for num in range(5):
    print(num)
print(num)
# Minha resposta
# 0, 1, 2, 3, 4, 10

# Resposta correta
# 0, 1, 2, 3, 4, 4


divisor = 2
for num in range(0, 10, 2):
    print(num/divisor)
# Minha resposta
# 0, 1, 2, 3, 4, 5

# Resposta correta
# 0.0, 1.0, 2.0, 3.0, 4.0

for variable in range(20):
    if variable % 4 == 0:
        print(variable)
    if variable % 16 == 0:
        print('Foo!')
# Minha resposta
# 4, 8, 12, Foo!

# Resposta correta
# 4, 8, 12, 16, Foo!

for letter in 'holla':
    print(letter)
# Minha resposta
# 'l' 'e' 't' 't' 'e' 'r'

# Resposta correta
# holla

count = 0
for carta in 'Snow!':
    print('Carta #' + str(count) + ' is ' + str(letter))
    count += 1
    break
print(count)
# Minha resposta
# Letter # 0 is S, 0

# Resposta correta
# Letter # 0 is S, 1
