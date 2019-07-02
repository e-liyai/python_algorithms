def getBit(num, i):
    return (num & (1 << i)) != 0


def setBit(num, i):
    return num | (1 << i)


def clearBit(num, i):
    mask = ~(1 << i)
    return num & mask


def clearBitsMostSignificantThroughI(num, i):
    mask = (1 << i) - 1
    return num & mask


def clearBitsithrough0(num, i):
    mask = -1 << (i + 1)
    return num & mask


def updateBitsInRange(outerNum, innerNum, higher, lower):
    counter = lower
    x = None
    while counter <= higher:
        k = (1 << counter)
        x = k if x == None else None
        x |= k
        counter += 1
    outerNum |= x
    innerNum << lower
    return outerNum & innerNum
