from sharedHand import *

def indexAnglesX(frame, hand):
    first = angleXIs(frame, hand, 5, 0, 6)
    second = angleXIs(frame, hand, 6,5,7)
    third = angleXIs(frame, hand, 7,6,8)

    return [first,second,third]

def indexAnglesZ(frame, hand):
    first = angleZIs(frame, hand, 5, 0, 6)
    second = angleZIs(frame, hand, 6,5,7)
    third = angleZIs(frame, hand, 7,6,8)

    return [first,second,third]

def midAnglesX(frame, hand):
    first = angleXIs(frame, hand, 9, 0, 10)
    second = angleXIs(frame, hand, 10,9,11)
    third = angleXIs(frame, hand, 11,10,12)

    return [first,second,third]

def midAnglesZ(frame, hand):
    first = angleZIs(frame, hand, 9, 0, 10)
    second = angleZIs(frame, hand, 10,9,11)
    third = angleZIs(frame, hand, 11,10,12)

    return [first,second,third]



def ringAnglesX(frame, hand):
    first = angleXIs(frame, hand, 13, 0, 14)
    second = angleXIs(frame, hand, 14, 13, 15)
    third = angleXIs(frame, hand, 15, 14, 16)

    return [first,second,third]

def ringAnglesZ(frame, hand):
    first = angleZIs(frame, hand, 13, 0, 14)
    second = angleZIs(frame, hand, 14,13,15)
    third = angleZIs(frame, hand, 15,14,16)

    return [first,second,third]


def pinktyAnglesX(frame, hand):
    first = angleXIs(frame, hand, 17, 0, 18)
    second = angleXIs(frame, hand, 18,17,19)
    third = angleXIs(frame, hand, 19,18,20)

    return [first,second,third]

def pinkyAnglesZ(frame, hand):
    first = angleZIs(frame, hand, 17, 0, 18)
    second = angleZIs(frame, hand, 18,17,19)
    third = angleZIs(frame, hand, 19,18,20)

    return [first,second,third]


def thumbAnglesX(frame, hand):
    first = angleXIs(frame, hand, 1, 0, 2)
    second = angleXIs(frame, hand, 2,1,3)
    third = angleXIs(frame, hand, 3,1,4)
    return [first, second, third]


def thumbAnglesZ(frame, hand):
    first = angleZIs(frame, hand, 1, 0, 2)
    second = angleZIs(frame, hand, 2,1,3)
    third = angleZIs(frame, hand, 3,1,4)
    return [first, second, third]