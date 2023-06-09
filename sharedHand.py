from sharedALL import *
from sharedALL import thevideo

thevideo = thevideo
def getPosePositions(video):
    results_hand_landmarks = []

    mpHands = mp.solutions.hands
    hands = mpHands.Hands()

    cap = cv2.VideoCapture(video)
    print(thevideo)

    while cap.isOpened() & cap.isOpened() != None:
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