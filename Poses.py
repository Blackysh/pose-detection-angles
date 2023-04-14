import cv2
import mediapipe as mp





def getPosePositions(video):

    mp_drawing = mp.solutions.drawing_utils
    mp_pose = mp.solutions.pose

    pose = mp_pose.Pose(
        min_detection_confidence=0.5,
        min_tracking_confidence=0.5)



    cap = cv2.VideoCapture(video)

    while cap.isOpened():
        # read frame from capture object
        _, frame = cap.read()
        current_frame = cap.get(CV_CAP_PROP_POS_FRAMES)
        try:
            # convert the frame to RGB format
            results = pose.process(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
            print(results.pose_landmarks)
            
            image_height, image_width, _ = image.shape
            
            nose = [ current_frame, results.pose_landmarks.landmark[mp_pose.PoseLandmark.NOSE].x * image_width, results.pose_landmarks.landmark[mp_pose.PoseLandmark.NOSE].y * image_height, results.pose_landmarks.landmark[mp_pose.PoseLandmark.NOSE].z , results.pose_landmarks.landmark[mp_pose.PoseLandmark.NOSE].visibility ]


            mp_drawing.draw_landmarks(
                frame, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)



            # show the final output
            cv2.imshow('Output', frame)
        except:
            pass
        if cv2.waitKey(1) == ord('q'):
                break

    cap.release()
    cv2.destroyAllWindows()


    return pos_list
    