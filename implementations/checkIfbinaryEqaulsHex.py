def compareBinWithHex(binary, hexa):
    value1 = convertFromBase(binary, 2)
    value2 = convertFromBase(hexa, 16)
    if value1 < 0 or value2 < 0:
        return False
    return value1 == value2


def convertFromBase(number, base):
    if base < 2 or (base > 10 and base != 16): return -1
    value = 0
    i = len(number)
    while i:
        digit = digitToValue(number[i])
        if digit < 0 or digit >= base: return -1
        exp = len(number) - 1 - i
        value += digit * pow(base, exp)
        i -=1

    return value


def digitToValue(value):
    pass