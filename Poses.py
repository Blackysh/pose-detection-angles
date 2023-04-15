import cv2
import mediapipe as mp
import math
import re

mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose


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
    if re.search('-', str(angD)):
        angfinal = float(str(angD).split('-')[1])
        angfinal = 180 + angfinal
    return angfinal


def getAngles(positions):
    return



positions = getPosePositions(video="a.mp4")
""" 

    positions[1] <-- is the number of frame
    .landmark[  mp_pose.PoseLandmark.NOSE <-- Landmark Name     ]
    .x <-- x axis, y axis, z axis, visibility . 

"""
print(positions[1].landmark[mp_pose.PoseLandmark.NOSE].x)