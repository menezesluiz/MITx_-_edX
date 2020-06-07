"""
varA = input()
varB = input()

if (type(varA) == str) or (type(varB) == str):
    print("string involved")
elif varA > varB:
    print("bigger")
elif varA == varB:
    print("equal")
elif varA < varB:
    print("smaller")

"""

"""
num = 0
while num <= 10:
    num += 1
    if num % 2 == 0:
        print(num)
print("Good Bye")
"""

"""
print("Hello")
num = 12
while num > 1:
    num -= 1
    if num % 2 == 0:
        print(num)
"""

"""
end = 6
n = 1
soma = 0
while n <= end:
    soma = soma + n
    n += 1
print(soma)
"""

"""
for i in range(2, 12, 2):
    print(i)
print("Goodbye!")
"""


"""
print("Hello!")
for i in range(10, 1, -2):
    print(i)
"""

"""
end = 20
n = 1
z = 0
for i in range(0, end):
    z = z + n
    n += 1
print(z)
"""


"""
x = int(input())
ans = 0
while ans ** 3 < x:
    ans = ans + 1
if ans ** 3 != x:
    print(str(x) + " não é um cubo perfeito!")
else:
    print("A raiz cubica é " + str(x) + " is " + str(ans))

'''
cubo perfeito é quando a raiz cubica da um número tem-se como resultado
um número inteiro. 
2³ = 8,  4³ = 64, 5³ = 125
'''
"""
"""
iteration = 0
count = 0
while iteration < 5:
    for letter in "hello, world":
        count += 1
    print("Iteration " + str(iteration) + "; count is: " + str(count))
    iteration += 1
"""
"""
count = 0
phrase = "hello, world"
for iteration in range(5):
    while True:
        count += len(phrase)
        break
    print("Iteration " + str(iteration) + "; count is: " + str(iteration))
"""