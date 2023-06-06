from sharedALL import *
from sharedBody import *

def angleXIs(frame, Joint1, Joint2, Joint3):
    value = values(frame)
    a = [value[Joint2].x, value[Joint2].y]
    b = [value[Joint1].x, value[Joint1].y]
    c = [value[Joint3].x, value[Joint3].y]

    pointsList = [b,a,c]
    angle = getAngle(pointsList)

    return angle


def angleZIs(frame, Joint1, Joint2, Joint3):
    value = values(frame)
    a = [value[Joint2].y, value[Joint2].z]
    b = [value[Joint1].y, value[Joint1].z]
    c = [value[Joint3].y, value[Joint3].z]

    pointsList = [b,a,c]
    angle = getAngle(pointsList)

    return angle


def anglesXbody(frame):
    # Upper
    left_shoulder = angleXIs(frame,11 , 13, 23) #11
    right_shoulder = angleXIs(frame, 12, 24, 14) #12
    left_elbow = angleXIs(frame,13 , 15, 11) #13
    right_elbow = angleXIs(frame, 14, 12, 16) #14
    # Lower
    left_leg = angleXIs(frame,23,25,24) #23
    right_leg = angleXIs(frame,24,23,26) #24
    left_knee = angleXIs(frame,25,27,23) #25
    right_knee = angleXIs(frame,26,24,28) #26
    left_foot = angleXIs(frame,27,25,31) #27
    right_foot = angleXIs(frame,28,32,26) #28

    return [ 
        left_shoulder, right_shoulder, left_elbow, right_elbow,left_leg, right_leg, left_knee, right_knee, left_foot, right_foot, #10
        left_shoulder, right_shoulder, left_elbow, right_elbow, #14
        None, None, None, None, None, None, None, None,
        left_leg, right_leg, left_knee, right_knee, left_foot, right_foot
]


def anglesZbody(frame):
    # Upper
    left_shoulder = angleZIs(frame,11 , 23, 13) #11
    right_shoulder = angleZIs(frame, 12, 24, 14) #12
    left_elbow = angleZIs(frame,13 , 15, 11) #13
    right_elbow = angleZIs(frame, 14, 12, 16) #14
    # Lower
    left_leg = angleZIs(frame,23,25,24) #23
    right_leg = angleZIs(frame,24,23,26) #24
    left_knee = angleZIs(frame,25,27,23) #25
    right_knee = angleZIs(frame,26,24,28) #26
    left_foot = angleZIs(frame,27,25,31) #27
    right_foot = angleZIs(frame,28,32,26) #28

    return [ 
        left_shoulder, right_shoulder, left_elbow, right_elbow,left_leg, right_leg, left_knee, right_knee, left_foot, right_foot, #10
        left_shoulder, right_shoulder, left_elbow, right_elbow, #14
        None, None, None, None, None, None, None, None,
        left_leg, right_leg, left_knee, right_knee, left_foot, right_foot
]




def all_body_angles():
    anglesX = []
    anglesZ = []
    i = 0
    for position in positions:
        angleX = anglesXbody(i)
        angleZ = anglesZbody(i)
        anglesX.append(anglesX)
        anglesZ.append(angleZ)
        i+=1

    return [anglesX, anglesZ]

bodyAngles = all_body_angles()