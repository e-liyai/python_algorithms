def getBit(num, i):
    return (num & (1 << i)) != 0


def setBit(num, i):
    return num | (1 << i)


def clearBit(num, i):
    mask = ~(1 << i)
    return num & mask


def clearBitsMostSignificantThroughI(num, i):
    mask = (1 << i) - 1


def clearBitsithrough0(int num, int i):
    mask = -1 << (i + 1)
    return num & mask
