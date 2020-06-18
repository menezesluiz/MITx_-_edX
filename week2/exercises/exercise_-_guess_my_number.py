# -*- coding: utf-8 -*-
"""
Created on Sun Jun 14 12:04:09 2020

@author: Luiz Eduardo
"""

"""
In this problem, you'll create a program that guesses a secret number!

The program works as follows: you (the user) thinks of an integer between 0
(inclusive) and 100 (not inclusive). The computer makes guesses,
and you give it input - is its guess too high or too low?
Using bisection search, the computer will guess the user's secret number!

Here is a transcript of an example session:
"""

#  declarar frase inicial
print("Please think of a number between 0 and 100!")

#  declarar as variáveis máxima e mínima (limites)
low = 0
high = 100

while True:
    correct = (low + high) // 2
    print("Is your secret number " + str(correct) + "?")
    x = input("Enter 'h' to indicate the guess is too high." +
              " Enter 'l' to indicate the guess is too low." +
              " Enter 'c' to indicate I guessed correctly. ")
    if x == 'c':
        print("Game over. Your secret number was: ", str(correct))
        break
    elif x == "l":
        low = correct
    elif x == "h":
        high = correct
    else:
        print("Sorry, I did not understand your input.")
