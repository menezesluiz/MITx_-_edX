"""
Exercise: odd tuples
0.0/5.0 points (graded)
ESTIMATED TIME TO COMPLETE: 5 minutes

Write a procedure called , which takes a tuple as input, and returns a new
tuple as output, where every other element of the input tuple is copied,
starting with the first one. So if test is the tuple , then evaluating on
this input would return the tuple . oddTuples('I', 'am', 'a', 'test', 'tuple')
oddTuples('I', 'a', 'tuple')
"""

def oddTuples(aTup):
    '''
    aTup: a tuple

    returns: tuple, every other element of aTup.
    '''
    # Your Code Here

    return aTup[::2]

