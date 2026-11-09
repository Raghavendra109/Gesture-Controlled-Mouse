import cv2
import mediapipe as mp
import pyautogui
import math
# Webcam
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Cannot open camera")
    exit()

# Hand detector
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1)
draw = mp.solutions.drawing_utils

# Screen size
screen_w, screen_h = pyautogui.size()

while True:
    success, frame = cap.read()

    # Flip image
    frame = cv2.flip(frame, 1)

    # Convert BGR to RGB
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Detect hands
    output = hands.process(rgb_frame)

    frame_h, frame_w, _ = frame.shape

    if output.multi_hand_landmarks:
        for hand in output.multi_hand_landmarks:
            draw.draw_landmarks(frame, hand, mp_hands.HAND_CONNECTIONS)

            landmarks = hand.landmark

            # Index finger tip
            index_x = int(landmarks[8].x * frame_w)
            index_y = int(landmarks[8].y * frame_h)

            # Thumb tip
            thumb_x = int(landmarks[4].x * frame_w)
            thumb_y = int(landmarks[4].y * frame_h)

            # Draw circles
            cv2.circle(frame, (index_x, index_y), 10, (0,255,0), -1)
            cv2.circle(frame, (thumb_x, thumb_y), 10, (255,0,0), -1)

            # Convert webcam coordinates to screen coordinates
            screen_x = screen_w / frame_w * index_x
            screen_y = screen_h / frame_h * index_y

            # Move mouse
            pyautogui.moveTo(screen_x, screen_y)

            # Distance between fingers
            distance = math.hypot(index_x - thumb_x, index_y - thumb_y)

            # Click when fingers are close
            if distance < 30:
                pyautogui.click()
                pyautogui.sleep(1)

    cv2.imshow("Gesture Mouse Control", frame)

    # Exit with Q
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows() 