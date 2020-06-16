# -*- coding: utf-8 -*-
"""
Created on Fri Jun 12 14:02:05 2020

@author: Luiz Eduardo
"""

"""
iteration = 0
count = 0
while iteration < 5:
    # the variable 'letter' in the loop stands for every
    # character, including spaces and commas!
    for letter in 'hello, world':
        count += 1
    print("Iteration " + str(iteration) + "; count is: " + str(count))
    iteration += 1
"""

"""
iteration = 0
while iteration < 5:
    count = 0
    for letter in "hello, world":
        count += 1
        if iteration % 2 == 0:
            break
    print("Iteration " + str(iteration) + "; count is: " + str(count))
    iteration += 1
"""


"""
x = 25
epsilon = 0.01
step = 0.1
guess = 0.0

while guess <= x:
    if abs(guess**2 - x) < epsilon:
        break
    else:
        guess += step

if abs(guess**2 - x) >= epsilon:
    print('failed')
else:
    print('succeeded: ' + str(guess))
"""


"""
x = 25
epsilon = 0.01
step = 0.1
guess = 0.0

while guess <= x:
    if abs(guess ** 2 - x) >= epsilon:
        guess += step

if abs(guess ** 2 - x) >= epsilon:
    print("Failed")
else:
    print("Succeeded: " + str(guess))
"""

"""
x = 25
epsilon = 0.01
step = 0.1
guess = 0.0

while abs(guess ** 2 - x) >= epsilon:
    if guess <= x:
        guess += step
    else:
        break

if abs(guess ** 2 - x) >= epsilon:
    print("failed")
else:
    print('suceceeded: ' + str(guess))
"""

"""
def square(x):
    return(x )
"""


"""
a = int(input())
b = int(input())
c = int(input())
x = int(input())

def evalQuadratic(a, b, c, x):
    return(a * (x ** 2) + (b * x) + c)
print(evalQuadratic(a, b, c, x))
"""


"""
x = input()
y = input()
z = input()


def a(x):
    '''
    x: int or float.
    '''
    return x + 1
print(a(a(a(6))))



def b(x):
    '''
    x: int or float.
    '''
    return x + 1.0


def c(x, y):
    '''
    x: int or float.
    y: int or float.
    '''
    return x + y


def d(x, y):
    '''
    x: Can be of any type.
    y: Can be of any type.
    '''
    return x > y


def e(x, y, z):
    '''
    x: Can be of any type.
    y: Can be of any type.
    z: Can be of any type.
    '''
    return x >= y and x <= z


def f(x, y):
    '''
    x: int or float.
    y: int or float
    '''
    x + y - 2
"""