from sharedALL import *

mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_pose = mp.solutions.pose


def getPosePositions(video):
    pose = mp_pose.Pose(
        min_detection_confidence=0.5,
        min_tracking_confidence=0.5)

    results_pose_landmarks = []

    cap = cv2.VideoCapture(video)

    while cap.isOpened() & cap.isOpened() != None:

        # read frame from capture object
        _, frame = cap.read()

        try:
            if frame is not None:
            # convert the frame to RGB format
                results = pose.process(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
                    
                image_height, image_width, _ = frame.shape         

                mp_drawing.draw_landmarks(
                        frame, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)

                results_pose_landmarks.append(results.pose_landmarks)
            else:
                break

        except:
                # show the final output
            print("ERROR, CONTINUEING")
    
    return results_pose_landmarks

positions = getPosePositions(thevideo)


def values(frame):
    return positions[frame].landmark



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

