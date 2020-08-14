"""
Vídeo sobre entrada e saída de dados em Python (Input/Output)
"""

# print

x = 1
print(x)
x_str = str(x)
print("my fav num is", x, ".", "x =", x)
print("my fav num is " + x_str + ". " + "x = " + x_str)

# utilizando o comando "input"

text = input("Type anything... ") # aguarda a entrada de dados após o comando
print(5 * text)

"""
num = int(input("Type a number... "))
print(5 * num)
"""