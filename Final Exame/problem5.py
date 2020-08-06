# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 11:08:38 2020

@author: engineering_LuizEdua
"""


def uniqueValues(aDict):
    '''
    aDict: a dictionary
    returns: a sorted list of keys that map to unique aDict values,
    empty list if none
    '''
    # Your code here
    temporario = {}
    resultado = []
    for value in aDict.values():
        if(value in temporario.keys()):
            temporario[value] += 1
        else:
            temporario[value] = 1
    for key in aDict.keys():
        if(temporario[aDict[key]] == 1):
            resultado.append(key)

    return sorted(resultado)
