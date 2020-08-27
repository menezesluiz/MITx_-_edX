"""
Exercise 4
Finger Exercises due Aug 5, 2020 20:30 -03
Completed
 Bookmark this page
Exercise 4
5/5 points (graded)
ESTIMATED TIME TO COMPLETE: 8 minutes

Below are some short Python programs. For each program, answer the associated
question.

Try to answer the questions without running the code. Check your answers,
then run the code for the ones you get wrong.

This question is going to ask you what some simple loops print out. If you're
asked what code like this prints:
"""

# Exemplo
num = 5
if num > 2:
    print(num)
    num -= 1
print(num)

# write what it prints out, separating what appears on a new line by a comma
# and a space. So the answer for the above code would be:

# Resposta: 5, 4

"""
If a given loop will not terminate, write the phrase 'infinite loop' 
(no quotes) in the box. Recall that you can stop an infinite loop in your 
program by typing CTRL+c in the console.

Note: What does +=, -=, *=, /= stand for?
a += b is equivalent to a = a + b

a -= b is equivalent to a = a - b

a *= b is equivalent to a = a * b

a /= b is equivalent to a = a / b
"""

# 1
num = 0
while num <= 5:
    print(num)
    num += 1

print("Outside of loop")
print(num)
# Minha resposta:
# 0, 1, 2, 3, 4, 5, Outside of loop, 5 ou 6

# 2
numberOfLoops = 0
numberOfApples = 2
while numberOfLoops < 10:
    numberOfApples *= 2
    numberOfApples += numberOfLoops
    numberOfLoops -= 1
print("Number of apples: " + str(numberOfApples))
# Minha resposta:
# Infinite Loop


# 3
num = 10
while True:
    if num < 7:
        print("Breaking out of loop")
        break
    print(num)
    num -= 1
print("Outside of loop")
"""
Note: If the command break is executed within a loop, it halts evaluation of 
the loop at that point and passes control to the next expression. 
Test some break statements inside different loops if you don't understand this 
concept!
"""
# Minha resposta:
# Breaking out of loop, 10, 9, Outside Of loop

# 5
num = 100
while not False:
    if num < 0:
        break
print('num is: ' + str(num))
# Minha resposta:
# Infinit loop
