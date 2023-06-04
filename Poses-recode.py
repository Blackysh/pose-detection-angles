import cv2
import mediapipe as mp
import math
import re

mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose



thevideo = 'a.mp4'
removeMinus = False


def getPosePositions(video):
    pose = mp_pose.Pose(
        min_detection_confidence=0.5,
        min_tracking_confidence=0.5)

    results_pose_landmarks = []

    cap = cv2.VideoCapture(video)

    while cap.isOpened():
        # read frame from capture object
        _, frame = cap.read()
        try:
            # convert the frame to RGB format
            results = pose.process(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
                
            image_height, image_width, _ = frame.shape         

            mp_drawing.draw_landmarks(
                    frame, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)

            results_pose_landmarks.append(results.pose_landmarks)

                # show the final output
            cv2.imshow('Output', frame)
        except:
            break
        if cv2.waitKey(1) == ord('q'):
                break


    
    return results_pose_landmarks




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


def angleXIs(frame, Joint1, Joint2, Joint3 = None):
    positions = getPosePositions(video=thevideo)
    value = positions[frame].landmark


    a = [value[Joint2].x, value[Joint2].y]
    b = [value[Joint1].x, value[Joint1].y]

    if Joint3 == None:
        c = [value[Joint1].x , value[Joint2].y]
    else:
        c = [value[Joint3].x, value[Joint3].y]

    pointsList = [a,b,c]
    getAngle(pointsList)

    return angle


def angleZIs(frame, Joint1, Joint2, Joint3 = None):
    positions = getPosePositions(video=thevideo)
    value = positions[frame].landmark

    a = [value[Joint2].y, value[Joint2].z]
    b = [value[Joint1].y, value[Joint1].z]

    if Joint3 == None:
        c = []
    else:
        c = [value[Joint3].y, value[Joint3].z]

    pointsList = [a,b,c]
    getAngle(pointsList)

    return angle




















positions = getPosePositions(video=thevideo)
