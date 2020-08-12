"""
Video sobre strings e as melhores práticas
"""

# String: uma string é uma sequência de caracteres, letras e caracteres
# especiais

# Pode ser declarada com aspas simples ( ' ' ) ou aspas duplas ( " " )
hi = "Hello there"
greetings = 'hello'

# Podem ser concatenadas
name = 'eric'
greet = hi + name
greetings = hi + " " + name
print(greetings)

# concatenações sucessivas
print(3 * name)

# medir o comprimento da string ou do conjunto de strings
print(len(name))  # posso usar a variável
print(len('eric'))  # também posso usar a string

print(len(hi))
print(len(' hello there')) # constou um caracter a mais devido ao espaço

print(len('hi there'))

'eric'[1] #  indica o indice da respectiva letra = r
# em python, o índice começa por Zero (0)

# índices em python
print('eric'[1:3])  # me da as letras do indice 1 e 2 (até o 3 - excludente)
print('eric'[:3])  # todas as letras até o índice 3 (excluindo o 3)
print('eric'[1:])  # todas as letras a partir do índice 1
print('eric'[:])  # uma cópia do original