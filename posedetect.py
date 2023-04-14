import cv2
import mediapipe as mp


mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose

pose = mp_pose.Pose(
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5)



cap = cv2.VideoCapture('vid4detection.mp4')

while cap.isOpened():
    # read frame from capture object
    _, frame = cap.read()

    try:
    	# convert the frame to RGB format
        results = pose.process(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
        print(results.pose_landmarks)
        mp_drawing.draw_landmarks(
            frame, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)

        pose_landmarks = results.pose.landmarks

        # show the final output
        cv2.imshow('Output', frame)
    except:
    	pass
    if cv2.waitKey(1) == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
    