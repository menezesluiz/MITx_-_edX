import math


def polysum(n, s):
    area = ((0.25 * n * (s ** 2)) / (math.tan(math.pi / n)))
    perimetro = n * s
    sum = area + (perimetro ** 2)
    sum = round(sum, 4)
    return sum
polysum(71, 40)