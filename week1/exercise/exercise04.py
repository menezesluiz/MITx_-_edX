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

num = 0
while num <= 5:
    print(num)
    num += 1

print("Outside of loop")
print(num)