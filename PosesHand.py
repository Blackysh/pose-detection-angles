from sharedHand import *
from PosesBody import wrist_left, wrist_right
from PosesHandFingers import *


def anglesHandX(frame, hand):
    t1 = thumbAnglesX(frame,hand)[0]
    t2 = thumbAnglesX(frame,hand)[1]
    t3 = thumbAnglesX(frame,hand)[2]

    i1 = indexAnglesX(frame,hand)[0]
    i2 = indexAnglesX(frame,hand)[1]
    i3 = indexAnglesX(frame,hand)[2]

    m1 = midAnglesX(frame,hand)[0]
    m2 = midAnglesX(frame,hand)[1]
    m3 = midAnglesX(frame,hand)[2]

    r1 = ringAnglesX(frame,hand)[0]
    r2 = ringAnglesX(frame,hand)[1]
    r3 = ringAnglesX(frame,hand)[2]

    p1 = pinktyAnglesX(frame,hand)[0]
    p2 = pinktyAnglesX(frame,hand)[1]
    p3 = pinktyAnglesX(frame,hand)[2]
    
    return [t1, t2, t3, i1, i2, i3, m1, m2, m3, r1, r2, r3, p1, p2, p3]


def anglesHandZ(frame, hand):
    t1 = thumbAnglesZ(frame,hand)[0]
    t2 = thumbAnglesZ(frame,hand)[1]
    t3 = thumbAnglesZ(frame,hand)[2]

    i1 = indexAnglesZ(frame,hand)[0]
    i2 = indexAnglesZ(frame,hand)[1]
    i3 = indexAnglesZ(frame,hand)[2]

    m1 = midAnglesZ(frame,hand)[0]
    m2 = midAnglesZ(frame,hand)[1]
    m3 = midAnglesZ(frame,hand)[2]

    r1 = ringAnglesZ(frame,hand)[0]
    r2 = ringAnglesZ(frame,hand)[1]
    r3 = ringAnglesZ(frame,hand)[2]

    p1 = pinktyAnglesZ(frame,hand)[0]
    p2 = pinktyAnglesZ(frame,hand)[1]
    p3 = pinktyAnglesZ(frame,hand)[2]
    
    return [t1, t2, t3, i1, i2, i3, m1, m2, m3, r1, r2, r3, p1, p2, p3]



