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
    pointsList = []
    anglesList = []
    angleListz = []
    for position in positions:
        if str(position) != "None":
            # Left Shoulder
            Left_Elbow_xy = [ position.landmark[mp_pose.PoseLandmark.LEFT_ELBOW].x, position.landmark[mp_pose.PoseLandmark.LEFT_ELBOW].y]
            Left_Shoulder_xy = [ position.landmark[mp_pose.PoseLandmark.LEFT_SHOULDER].x, position.landmark[mp_pose.PoseLandmark.LEFT_SHOULDER].y ]
            Left_Shoulder_y3 = [ position.landmark[mp_pose.PoseLandmark.LEFT_SHOULDER].x + 0.1, position.landmark[mp_pose.PoseLandmark.LEFT_SHOULDER].y]
            pointsList.extend([Left_Elbow_xy , Left_Shoulder_xy, Left_Shoulder_y3])
            angleLeft_Shoulder = getAngle(pointsList=pointsList)
            anglesList.append(angleLeft_Shoulder)

            # Left Elbow
            Left_Wrist_xy = [ position.landmark[mp_pose.PoseLandmark.LEFT_WRIST].x, position.landmark[mp_pose.PoseLandmark.LEFT_WRIST].y]
            Left_Elbow_xy = [ position.landmark[mp_pose.PoseLandmark.LEFT_ELBOW].x, position.landmark[mp_pose.PoseLandmark.LEFT_ELBOW].y ]
            Left_Elbow_y3 = [ position.landmark[mp_pose.PoseLandmark.LEFT_ELBOW].x + 0.1, position.landmark[mp_pose.PoseLandmark.LEFT_ELBOW].y]
            pointsList.extend([Left_Wrist_xy , Left_Elbow_xy, Left_Elbow_y3])
            angleLeft_Elbow = getAngle(pointsList=pointsList)
            anglesList.append(angleLeft_Elbow)

            # Right Shoulder
            Right_Elbow_xy = [ position.landmark[mp_pose.PoseLandmark.RIGHT_ELBOW].x, position.landmark[mp_pose.PoseLandmark.RIGHT_ELBOW].y]
            Right_Shoulder_xy = [ position.landmark[mp_pose.PoseLandmark.RIGHT_SHOULDER].x, position.landmark[mp_pose.PoseLandmark.RIGHT_SHOULDER].y ]
            Right_Shoulder_y3 = [ position.landmark[mp_pose.PoseLandmark.RIGHT_SHOULDER].x + 0.1, position.landmark[mp_pose.PoseLandmark.RIGHT_SHOULDER].y]
            pointsList.extend([Right_Elbow_xy , Right_Shoulder_xy, Right_Shoulder_y3])
            angleRight_Shoulder = getAngle(pointsList=pointsList)
            anglesList.append(angleRight_Shoulder)

            # Right Elbow
            Right_Wrist_xy = [ position.landmark[mp_pose.PoseLandmark.RIGHT_WRIST].x, position.landmark[mp_pose.PoseLandmark.RIGHT_WRIST].y]
            Right_Elbow_xy = [ position.landmark[mp_pose.PoseLandmark.RIGHT_ELBOW].x, position.landmark[mp_pose.PoseLandmark.RIGHT_ELBOW].y ]
            Right_Elbow_y3 = [ position.landmark[mp_pose.PoseLandmark.RIGHT_ELBOW].x + 0.1, position.landmark[mp_pose.PoseLandmark.RIGHT_ELBOW].y]
            pointsList.extend([Right_Wrist_xy , Right_Elbow_xy, Right_Elbow_y3])
            angleRight_Elbow = getAngle(pointsList=pointsList)
            angleList.append(angleRight_Elbow)

            # Right Leg
            Right_KNEE_xy = [ position.landmark[mp_pose.PoseLandmark.RIGHT_KNEE].x, position.landmark[mp_pose.PoseLandmark.RIGHT_KNEE].y]
            Right_HIP_xy = [ position.landmark[mp_pose.PoseLandmark.RIGHT_HIP].x, position.landmark[mp_pose.PoseLandmark.RIGHT_HIP].y ]
            Right_HIP_y3 = [ position.landmark[mp_pose.PoseLandmark.RIGHT_HIP].x + 0.1, position.landmark[mp_pose.PoseLandmark.RIGHT_HIP].y]
            pointsList.extend([Right_KNEE_xy , Right_HIP_xy, Right_HIP_y3])
            angleRight_HIP = getAngle(pointsList=pointsList)
            anglesList.append(angleRight_HIP)

            # Right KNEE
            Right_ANKLE_xy = [ position.landmark[mp_pose.PoseLandmark.RIGHT_ANKLE].x, position.landmark[mp_pose.PoseLandmark.RIGHT_ANKLE].y]
            Right_KNEE_xy = [ position.landmark[mp_pose.PoseLandmark.RIGHT_KNEE].x, position.landmark[mp_pose.PoseLandmark.RIGHT_KNEE].y ]
            Right_KNEE_y3 = [ position.landmark[mp_pose.PoseLandmark.RIGHT_KNEE].x + 0.1, position.landmark[mp_pose.PoseLandmark.RIGHT_KNEE].y]
            pointsList.extend([Right_ANKLE_xy , Right_KNEE_xy, Right_KNEE_y3])
            angleRight_KNEE = getAngle(pointsList=pointsList)
            angleList.append(angleRight_KNEE)


            # Right Leg
            Right_KNEE_xy = [ position.landmark[mp_pose.PoseLandmark.RIGHT_KNEE].x, position.landmark[mp_pose.PoseLandmark.RIGHT_KNEE].y]
            Right_HIP_xy = [ position.landmark[mp_pose.PoseLandmark.RIGHT_HIP].x, position.landmark[mp_pose.PoseLandmark.RIGHT_HIP].y ]
            Right_HIP_y3 = [ position.landmark[mp_pose.PoseLandmark.RIGHT_HIP].x + 0.1, position.landmark[mp_pose.PoseLandmark.RIGHT_HIP].y]
            pointsList.extend([Right_KNEE_xy , Right_HIP_xy, Right_HIP_y3])
            angleRight_HIP = getAngle(pointsList=pointsList)
            anglesList.append(angleRight_HIP)

            # Right KNEE
            Right_ANKLE_xy = [ position.landmark[mp_pose.PoseLandmark.RIGHT_ANKLE].x, position.landmark[mp_pose.PoseLandmark.RIGHT_ANKLE].y]
            Right_KNEE_xy = [ position.landmark[mp_pose.PoseLandmark.RIGHT_KNEE].x, position.landmark[mp_pose.PoseLandmark.RIGHT_KNEE].y ]
            Right_KNEE_y3 = [ position.landmark[mp_pose.PoseLandmark.RIGHT_KNEE].x + 0.1, position.landmark[mp_pose.PoseLandmark.RIGHT_KNEE].y]
            pointsList.extend([Right_ANKLE_xy , Right_KNEE_xy, Right_KNEE_y3])
            angleRight_KNEE = getAngle(pointsList=pointsList)
            angleList.append(angleRight_KNEE)

            # LEFT Leg
            LEFT_KNEE_xy = [ position.landmark[mp_pose.PoseLandmark.LEFT_KNEE].x, position.landmark[mp_pose.PoseLandmark.LEFT_KNEE].y]
            LEFT_HIP_xy = [ position.landmark[mp_pose.PoseLandmark.LEFT_HIP].x, position.landmark[mp_pose.PoseLandmark.LEFT_HIP].y ]
            LEFT_HIP_y3 = [ position.landmark[mp_pose.PoseLandmark.LEFT_HIP].x + 0.1, position.landmark[mp_pose.PoseLandmark.LEFT_HIP].y]
            pointsList.extend([LEFT_KNEE_xy , LEFT_HIP_xy, LEFT_HIP_y3])
            angleLEFT_HIP = getAngle(pointsList=pointsList)
            anglesList.append(angleLEFT_HIP)

            # LEFT KNEE
            LEFT_ANKLE_xy = [ position.landmark[mp_pose.PoseLandmark.LEFT_ANKLE].x, position.landmark[mp_pose.PoseLandmark.LEFT_ANKLE].y]
            LEFT_KNEE_xy = [ position.landmark[mp_pose.PoseLandmark.LEFT_KNEE].x, position.landmark[mp_pose.PoseLandmark.LEFT_KNEE].y ]
            LEFT_KNEE_y3 = [ position.landmark[mp_pose.PoseLandmark.LEFT_KNEE].x + 0.1, position.landmark[mp_pose.PoseLandmark.LEFT_KNEE].y]
            pointsList.extend([LEFT_ANKLE_xy , LEFT_KNEE_xy, LEFT_KNEE_y3])
            angleLEFT_KNEE = getAngle(pointsList=pointsList)
            angleList.append(angleLEFT_KNEE)




            # At Last (Changing to new frame)
            anglesList.append(":")
            angleListz.append(":")
    return [ angleList , angleListz ] 



positions = getPosePositions(video="a.mp4")
angles = getAngles(positions)
""" 

    positions[1] <-- is the number of frame
    .landmark[  mp_pose.PoseLandmark.NOSE <-- Landmark Name     ]
    .x <-- x axis, y axis, z axis, visibility . 

print(positions[1].landmark[mp_pose.PoseLandmark.NOSE].x)
"""
