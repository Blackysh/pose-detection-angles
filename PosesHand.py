from sharedHand import *
from PosesBody import wrist_left, wrist_right
from PosesHandFingers import *
import sharedBody

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


def is0Left(frame):
    wristX = values(frame, 0)[0].x
    wristY = values(frame, 0)[0].y

    left_wristX = sharedBody.values(frame)[15].x
    left_wristY = sharedBody.values(frame)[15].y

    right_wristX = sharedBody.values(frame)[16].x
    right_wristY= sharedBody.values(frame)[16].y

    distance_rightX = wristX - right_wristX
    distance_leftX = wristX - left_wristX

    distance_rightY = wristY - right_wristY
    distance_leftY = wristY - right_wristY

    if distance_rightX > distance_leftX or distance_rightY > distance_leftY:
        return True
    
    else:
        return False

    


def left_hand_positions():
    i = 0

    left_handx = []
    left_handz = []
    for position in hand_positions:
        if is0Left(i):
            leftX = anglesHandX(i, 0)
            leftZ = anglesHandZ(i, 0)
        else:
            try:
                leftX = anglesHandX(i,1)
                leftZ = anglesHandZ(i,1)
            except:
                print('ERROR: Second Hand Not Found')
        left_handx.append(leftX)
        left_handz.append(leftZ)
        i +=1


    return [left_handx,left_handz]



def right_hand_positions():
    i = 0 
    right_handx = []
    right_handz = []

    for position in hand_positions:
        if not is0Left(i):
            rightX = anglesHandX(i, 0)
            rightZ = anglesHandZ(i, 0)
        else:
            try:
                rightX = anglesHandX(i, 1)
                rightZ = anglesHandZ(i,1)
            except:
                print('ERROR: Second Hand Not Found') 
        i +=1
        right_handx.append(rightX)
        right_handz.append(rightZ)


        return [right_handx, right_handz]


leftHand = left_hand_positions()
rightHand = right_hand_positions()