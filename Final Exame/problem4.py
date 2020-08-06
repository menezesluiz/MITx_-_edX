# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 11:07:36 2020

@author: engineering_LuizEdua
"""


def longest_run(L):
    """
    Assumes L is a list of integers containing at least 2 elements.
    Finds the longest run of numbers in L, where the longest run can
    either be monotonically increasing or monotonically decreasing.
    In case of a tie for the longest run, choose the longest run
    that occurs first.
    Does not modify the list.
    Returns the sum of the longest run.
    """
    # Your code here

    decimal_contagem = 0
    inicial_contagem = 0
    maximo = 0
    resultado = 0
    for char in range(len(L) - 1):
        if(L[char] <= L[char + 1]):
            decimal_contagem += 1
            if decimal_contagem > maximo:
                maximo = decimal_contagem
                resultado = char + 1
        else:
            decimal_contagem = 0
        if(L[char] >= L[char + 1]):
            inicial_contagem += 1
            if inicial_contagem > maximo:
                maximo = inicial_contagem
                resultado = char + 1
        else:
            inicial_contagem = 0

    posicao_inicial = resultado - maximo
    return sum(L[posicao_inicial:resultado + 1])
