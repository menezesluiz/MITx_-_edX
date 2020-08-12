"""
Vídeo sobre variáveis e as melhores práticas para se trabalhar com elas.
"""

# Vídeo: Bindings

x = 2
x = x * x
y = x + 1
print(y)


# Dessa forma, é mais fácil de se perder
x = 1
y = 2
y = x
x = y
print(x)

# A solução seria criar uma variável temporária

x = 1
y = 2
temp = y
y = x
x = temp
print(x)