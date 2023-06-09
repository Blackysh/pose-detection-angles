from sharedALL import *
from sharedBody import *

def manualAngleYIs(frame, Points1, Joint2, Joint3):
    value = values(frame)
    a = [value[Joint2].x, value[Joint2].y]
    b = [value[Joint3].x, value[Joint3].y]
    c = Points1

    pointsList = [b,a,c]
    angle = getAngle(pointsList)

    return angle


def manualAngleZIs(frame, Points1, Joint2, Joint3):
    value = values(frame)
    a = [value[Joint2].x, value[Joint2].z]
    b = [value[Joint3].x, value[Joint3].z]
    c = Points1

    pointsList = [b,a,c]
    angle = getAngle(pointsList)

    return angle

def neckAngleZ(frame):
    value = values(frame)
    diffX = value[12].x - value[11].x
    diffZ = value[12].z - value[11].z

    midPointX = diffX/2 + value[11].x
    midPointZ = diffZ/2 + value[11].z

    return manualAngleZIs(frame, [midPointX, midPointZ], 7, 0)

    
def neckAngleY(frame):
    value = values(frame)
    diffX = value[12].x - value[11].x
    diffY = value[12].y - value[11].y

    midPointX = diffX/2 + value[11].x
    midPointY = diffY/2 + value[11].y
    return manualAngleXIs(frame, [midPointX, midPointY], 7, 0)


def neck_angles():
    anglesY = []
    anglesZ = []
    i = 0

    for position in positions:
        try:
            angleY = neckAngleY(i)
            angleZ = neckAngleZ(i)
        except:
            angleY = None
            angleZ = None
        anglesX.append(anglesX)
        anglesZ.append(angleZ)
        i+=1
        


    return [anglesX, anglesZ]


neckAngles = neck_angles()