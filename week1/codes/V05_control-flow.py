"""
Vídeo explicando o controle de fluxo em programas
"""


# um exemplo de loop. Fica preso enquanto repete a palavra "right"
n = input("You are in the Lost Forest. Go left or right? ")
while n == "right":
    n = input("You are in the Lost Forest. Go left or right? ")
print("You got out of the Lost Forest")

# more complicated with while loop
n = 0
while n < 5:
    print(n)
    n = n + 1

# shortcut with for loop
for n in range(5):
    print(n)


# range(start, stop, step)
mysum = 0
for i in range(7, 10):
    mysum += i
print(mysum)


mysum = 0
for i in range(5, 11, 2):
    mysum += i
print(mysum)

# incluindo o comando break
mysum = 0
for i in range(5, 11, 2):
    mysum += i
    if mysum == 5:
        break
print(mysum)
