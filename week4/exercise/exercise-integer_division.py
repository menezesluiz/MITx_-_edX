def integerDivision(x, a):
    """
    x: a non-negative integer argument
    a: a positive integer argument

    returns: integer, the integer division of x divided by a.
    """

    # o exercício pede para debugar o código e encontrar o erro, deve-se add
    # o count = 0

    # count = 0
    while x >= a:
        count += 1
        x = x - a
    return count

print(integerDivision(5, 3))

print("MITx-edX")