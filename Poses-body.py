import cv2
import mediapipe as mp
import math
import re

mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose
thevideo = 's.mp4'
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


def angleXIs(frame, Joint1, Joint2, Joint3):
    #positions = getPosePositions(video=thevideo)
    #value = positions[frame].landmark


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




def all_angles():
    anglesX = []
    anglesZ = []
    i = 0
    for position in positions:
        angleX = anglesXbody(i)
        angleZ = anglesZbody(i)
        anglesX.append(anglesX)
        anglesZ.append(angleZ)
        i+=1

        

















positions = getPosePositions(video=thevideo)
