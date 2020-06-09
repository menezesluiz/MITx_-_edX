"""
English
Assume s is a string of lower case characters.

Write a program that prints the longest substring of s in which the letters
occur in alphabetical order. For example, if s = 'azcbobobegghakl',
then your program should print:
Longest substring in alphabetical order is: beggh

In the case of ties, print the first substring. For example, if s = 'abcbcd',
then your program should print:
Longest substring in alphabetical order is: abc

Note: This problem may be challenging. We encourage you to work smart. If
you've spent more than a few hours on this problem, we suggest that you move
on to a different part of the course. If you have time, come back to this
problem after you've had a break and cleared your head.

-------------------------------------------------------------------------------
Brazilian Portueguese
Suponha que s é uma sequência de caracteres em minúsculas.

Escreva um programa que imprima a subsequência mais longa de s na qual as
letras ocorrem em ordem alfabética. Por exemplo, se s = 'azcbobobegghakl',
seu programa deverá imprimir:
A substring mais longa em ordem alfabética é: beggh

No caso de gravatas, imprima a primeira substring. Por exemplo,
se s = 'abcbcd', seu programa deve imprimir:
A subsequência mais longa em ordem alfabética é: abc

Nota: Esse problema pode ser desafiador. Nós encorajamos você a trabalhar
de forma inteligente. Se você passou mais de algumas horas com esse problema,
sugerimos que você passe para uma parte diferente do curso.
Se você tiver tempo, volte a esse problema depois de fazer uma pausa
e limpar a cabeça.
"""

s = 'azcbobobegghakl'
indice = 0
palavra = ""
maior_palavra = ""

while indice < len(s) - 1:
    if palavra == "":
        palavra = s[indice]
        if len(palavra) > len(maior_palavra):
            maior_palavra = palavra

    if s[indice] <= s[indice + 1]:
        palavra += s[indice + 1]
        if len(palavra) > len(maior_palavra):
            maior_palavra = palavra

    else:
        palavra = ""

    indice += 1

print(maior_palavra)