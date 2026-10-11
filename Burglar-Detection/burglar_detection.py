# Importing opencv
import cv2

# Reading the video file
cap = cv2.VideoCapture("input_video.mp4")

# Array for storing the frames
frames = []

# Gap between the frames we compare
gap = 5

# Frame counter
count = 0

# Minimum contour area to count as motion
min_area = 300

while True:
    # Reading the captured frame
    ret, frame = cap.read()

    # Stop if nothing is being read
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    frames.append(gray)

    if len(frames) > gap + 1:
        frames.pop(0)

    cv2.putText(frame, f"Frame Count:{count}", (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    if len(frames) > gap:
        # Difference between oldest and newest frame
        diff = cv2.absdiff(frames[0], frames[-1])

        # Keeping pixel values from 30 to 255
        _, thresh = cv2.threshold(diff, 30, 255, cv2.THRESH_BINARY)

        contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL,
                                       cv2.CHAIN_APPROX_SIMPLE)

        motion = False
        for c in contours:
            if cv2.contourArea(c) < min_area:
                continue
            motion = True
            x, y, w, h = cv2.boundingRect(c)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        if motion:
            cv2.putText(frame, "Motion Detected!", (10, 60),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
            cv2.imwrite(f'motion_frame_{count}.jpg', frame)
            print(f'Saved:motion_frame_{count}.jpg')

    
    cv2.imshow('Motion Detection', frame)
    count += 1

    # Exit if ESC is pressed or the window is closed
    key = cv2.waitKey(1) & 0xFF

    if key == 27:
        break

    if cv2.getWindowProperty('Motion Detection',
                         cv2.WND_PROP_VISIBLE) < 1:
        break


# Releasing the camera and closing windows after the loop
cap.release()
cv2.destroyAllWindows()