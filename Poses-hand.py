import cv2
import mediapipe as mp
import math
import re



def gradient(pt1, pt2):
    #  y2 - y1 / x2 - x1  
    return ( pt2[1]-pt1[1] ) / (pt2[0] - pt1[0] )

def getAngle(pointsList):
    pt1 , pt2, pt3 = pointsList[-3:]
    m1 = gradient(pt1, pt2)
    m2 = gradient(pt1, pt3)
    angR = math.atan( (m2-m1) / (1+(m2*m1)) )
    angD =  math.degrees(angR)
    angfinal = angD
    
    if re.search('-', str(angD)) and removeMinus:
        angfinal = float(str(angD).split('-')[1])
        angfinal = 180 + angfinal
    return angfinal


def angleXIs(frame, Joint1, Joint2, Joint3):
    positions = getPosePositions(video=thevideo)
    value = positions[frame].landmark


    a = [value[Joint2].x, value[Joint2].y]
    b = [value[Joint1].x, value[Joint1].y]
    c = [value[Joint3].x, value[Joint3].y]

    pointsList = [b,a,c]
    angle = getAngle(pointsList)

    return angle


def angleZIs(frame, Joint1, Joint2, Joint3):
    positions = getPosePositions(video=thevideo)
    value = positions[frame].landmark

    a = [value[Joint2].y, value[Joint2].z]
    b = [value[Joint1].y, value[Joint1].z]
    c = [value[Joint3].y, value[Joint3].z]

    pointsList = [b,a,c]
    angle = getAngle(pointsList)

    return angle