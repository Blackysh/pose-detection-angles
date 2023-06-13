from sharedALL import *

def getPosePositions(video):
    results_hand_landmarks = []

    mpHands = mp.solutions.hands
    hands = mpHands.Hands()

    cap = cv2.VideoCapture(video)
    print(thevideo)

    while cap.isOpened() and cap.isOpened() != None:
        try:
            _, frame = cap.read()

            if frame is not None:

                image_height, image_width, _ = frame.shape         

                results = hands.process(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))


                rsults_stuff = results.multi_hand_landmarks

                results_hand_landmarks.append(rsults_stuff)

            else:
                break

        except Exception as E: 
            print('error: ' + str(E))

    return results_hand_landmarks

hand_positions = getPosePositions(thevideo)

def values(frame, hand):
    return hand_positions[frame][hand].landmark


def angleXIs(frame, hand, Joint1, Joint2, Joint3):
    value = values(frame, hand)
    a = [value[Joint2].x, value[Joint2].y]
    b = [value[Joint1].x, value[Joint1].y]
    c = [value[Joint3].x, value[Joint3].y]

    pointsList = [b,a,c]
    angle = getAngle(pointsList)

    return angle


def angleZIs(frame, hand, Joint1, Joint2, Joint3):
    value = values(frame, hand)
    a = [value[Joint2].y, value[Joint2].z]
    b = [value[Joint1].y, value[Joint1].z]
    c = [value[Joint3].y, value[Joint3].z]

    pointsList = [b,a,c]
    angle = getAngle(pointsList)

    return angle


