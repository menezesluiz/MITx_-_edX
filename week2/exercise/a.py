import math


def cy_vol(r, h):
    vol = ((math.pi * (r ** 2) * h))
    Ab = 10
    h = (Ab / 2)
    total = round(vol, 2)
    return total
cy_vol(3.1, 10)
