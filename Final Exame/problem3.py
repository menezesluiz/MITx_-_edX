# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 12:03:40 2020

@author: engineering_LuizEdua
"""


def print_without_vowels(s):
    '''
    s: the string to convert
    Finds a version of s without vowels and whose characters appear in the
    same order they appear in s. Prints this version of s.
    Does not return anything
    '''
    # Your code here

    vogal = ('A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u')
    for x in s:
        if x in vogal:
            s = s.replace(x, '')
    print(s)

