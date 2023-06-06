import cv2
import mediapipe as mp
import math
import re


thevideo = 's.mp4'
removeMinus = False


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