"""
Consider the following function definition:
"""

def union(set1, set2):
   """
   set1 and set2 are collections of objects, each of which might be empty.
   Each set has no duplicates within itself, but there may be objects that
   are in both sets. Objects are assumed to be of the same type.

   This function returns one set containing all elements from
   both input sets, but with no duplicates.
   """
   if len(set1) == 0:
      return set2
   elif set1[0] in set2:
      return union(set1[1:], set2)
   else:
      return set1[0] + union(set1[1:], set2)

"""
Assume that union is called with strings as arguments.

Please select the best glass box test suite for the function union from the 
following options:
"""

#  Test Suite A: union('',''), union('','a'), union('','ab'), union('a',''),
#  union('a','b'), union('c','ab'), union('de',''), union('ab','c'),
#  union('cd','ab')

# Test Suite B: union('abc',''), union('abc','a'), union('abc','ab'),
# union('abc','d'), union('abc', 'abcd')

# Test Suite C: union('','abc'), union('a','abc'), union('ab','abc'),
# union('abc','abc')

# Test Suite D: union('','abc'), union('a','abc'), union('ab','abc'),
# union('d','abc')