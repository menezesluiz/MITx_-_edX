"""
Assume s is a string of lower case characters.
Write a program that counts up the number of vowels contained in the string s.
Valid vowels are: 'a', 'e', 'i', 'o', and 'u'.
For example, if s = 'azcbobobegghakl', your program should print:
Number of vowels: 5

------------------------------------------------------------------------------
Brazilian Portuguese
Suponha que s é uma sequência de caracteres em minúsculas.
Escreva um programa que conte o número de vogais contidas na string s.
As vogais válidas são: 'a', 'e', 'i', 'o' e 'u'.
Por exemplo, se s = 'azcbobobegghakl', seu programa deve imprimir:
Número de vogais: 5
"""

s = 'azcbobobegghakl'
numVowels = 0

for char in s:
    if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u':
        numVowels += 1

print("Number of vowels: " + str(numVowels))