from sharedALL import *

def getPosePositions(thevideo):
    results_hand_landmarks = []
    mpHands = mp.solutions.hands
    hands = mpHands.Hands()
    mpDraw = mp.solutions.drawing_utils
    cap = cv2.VideoCapture(thevideo)

    while cap.isOpened():
        try:
            _, frame = cap.read()
            results = hands.process(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

            image_height, image_width, _ = frame.shape         

            mp_drawing.draw_landmarks(
                        frame, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)

            ## results_hand_landmarks.append(results.pose_landmarks)
            cv2.imshow('Output', frame)

        except: 
            break

        

getPosePositions(thevideo)