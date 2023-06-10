from sharedALL import *
from sharedBody import *


def anglesXbody(frame):
    # Upper
    left_shoulder = angleXIs(frame,11,13,23) #11
    right_shoulder = angleXIs(frame,12,24,14) #12
    left_elbow = angleXIs(frame,13,15,11) #13
    right_elbow = angleXIs(frame,14,12,16) #14
    # Lower
    left_leg = angleXIs(frame,23,25,24) #23
    right_leg = angleXIs(frame,24,23,26) #24
    left_knee = angleXIs(frame,25,27,23) #25
    right_knee = angleXIs(frame,26,24,28) #26
    left_foot = angleXIs(frame,27,25,31) #27
    right_foot = angleXIs(frame,28,32,26) #28
    wrist_left = angleXIs(frame, 15, 13, 19)
    wrist_right = angleXIs(frame, 16, 14, 20)

    return [ 
        left_shoulder, right_shoulder, left_elbow, right_elbow,left_leg, right_leg, left_knee, right_knee, left_foot, right_foot, #10
        left_shoulder, right_shoulder, left_elbow, right_elbow, #14
        wrist_left, wrist_right, None, None, None, None, None, None,
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

    wrist_left = angleZIs(frame, 15, 13, 19)
    wrist_right = angleZIs(frame, 16, 14, 20)

    return [ 
        left_shoulder, right_shoulder, left_elbow, right_elbow,left_leg, right_leg, left_knee, right_knee, left_foot, right_foot, #10
        left_shoulder, right_shoulder, left_elbow, right_elbow, #14
        wrist_left, wrist_right, None, None, None, None, None, None,
        left_leg, right_leg, left_knee, right_knee, left_foot, right_foot
]




def all_body_angles():
    anglesX = []
    anglesZ = []
    i = 0

    wrists_leftX = []
    wrists_leftZ = []
    wrists_RightX = []
    wrists_RightZ = []

    for position in positions:
        try:
            angleX = anglesXbody(i)
            angleZ = anglesZbody(i)

            wrist_leftX = anglesXbody(i)[15]
            wrist_rightX = anglesXbody(i)[16]
            wrist_leftZ = anglesZbody(i)[15]
            wrist_rightZ = anglesZbody(i)[16]


        except:
            angleX = None
            angleZ = None
            wrist_leftX = None
            wrist_rightX = None
            wrist_leftZ = None
            wrist_rightZ = None

        anglesX.append(angleX)
        anglesZ.append(angleZ)
        wrists_leftX.append(wrist_leftX)
        wrists_leftZ.append(wrist_leftZ)
        wrists_RightX.append(wrist_rightX)
        wrists_RightZ.append(wrist_rightZ)
        i+=1
        
        wrists_left = [wrists_leftX, wrists_leftZ]
        wrists_right = [wrists_RightX, wrists_RightZ]


    return [anglesX, anglesZ, wrists_left, wrists_right]


bodyAnglesP = all_body_angles()


# Use bodyAngles [0 and 1] for Angles X and Z respectively. 
# After choosing if you want angle X or Angle Z, choose the frame you want the angle for
# After choosing the angle, choose the body part that you want the angle for.
bodyAngles = [bodyAnglesP[0], bodyAnglesP[1]]


wrists_left = bodyAnglesP[2]
wrists_right = bodyAnglesP[3]

