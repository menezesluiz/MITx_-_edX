"""
Exercise: while
Finger Exercises due Aug 5, 2020 20:30 -03
Completed
 Bookmark this page
Exercise: while exercise 1
5.0/5.0 points (graded)
ESTIMATED TIME TO COMPLETE: 5 minutes

In this problem you'll be given a chance to practice writing some while loops.

1. Convert the following into code that uses a while loop.

print 2
prints 4
prints 6
prints 8
prints 10
prints Goodbye!
"""
num = 0
while num <= 10:
    num += 1
    if num % 2 == 0:
        print(num)
print("Goodbye!")