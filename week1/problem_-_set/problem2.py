"""
English
Assume s is a string of lower case characters.
Write a program that prints the number of times the string 'bob' occurs in s.
For example, if s = 'azcbobobegghakl', then your program should print:
Number of times bob occurs is: 2

-------------------------------------------------------------------------------
Brazilian Portuguese
Suponha que s é uma sequência de caracteres em minúsculas.
Escreva um programa que imprima o número de vezes que a string
'bob' ocorre em s. Por exemplo, se s = 'azcbobobegghakl',
seu programa deve imprimir:
O número de vezes que bob ocorre é: 2
"""

s = 'azcbobobegghakl'
occurs = 0
for i in range(len(s)):
    if s[i:i+3] == 'bob':
        occurs += 1
print(occurs)
