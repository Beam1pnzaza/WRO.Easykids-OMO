import cv2
import numpy as np

# Open the default camera (0) or use a specific camera index (e.g., 1 for the second camera)
cam = cv2.VideoCapture(0)

def DetectRed(frame):
    lowerred = np.array([166, 79, 142])
    upperred = np.array([179, 137, 255])
    reddetect = cv2.inRange(hsv, lowerred, upperred)
    red_canny = cv2.Canny(reddetect, 400, 500)
    red_contours, red_hierarchy = cv2.findContours(red_canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
   
    for cnt in red_contours:
        area = cv2.contourArea(cnt)
        print("area =", area)
        if area > 5000:
            cv2.drawContours(frame, [cnt], -1, (0, 0, 255), 3)  # Draw red contours

    if len(red_contours) > 0:
        # Get the bounding rectangle around the first detected contour
        x, y, w, h = cv2.boundingRect(red_contours[0])
        # Calculate the x-coordinate of the center of the rectangle
        center_x = x + w // 2
        return center_x
    else:
        return -1  # Return -1 if no red detected

def DetectGreen(frame):
    lowergreen = np.array([50, 56, 100])
    uppergreen = np.array([70, 172, 255])
    greendetect = cv2.inRange(hsv, lowergreen, uppergreen)
    green_canny = cv2.Canny(greendetect, 400, 500)
    green_contours, green_hierarchy = cv2.findContours(green_canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    
    for cnt in green_contours:
        area = cv2.contourArea(cnt)
        print("area =", area)
        if area > 5000:
            cv2.drawContours(frame, [cnt], -1, (0, 255, 0), 3)  # Draw green contours

    if len(green_contours) > 0:
        # Get the bounding rectangle around the first detected contour
        x, y, w, h = cv2.boundingRect(green_contours[0])
        # Calculate the x-coordinate of the center of the rectangle
        center_x = x + w // 2
        return center_x
    else:
        return -1  # Return -1 if no green detected
    
while True:
    # Capture a frame from the camera
    ret, frame = cam.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Detect and draw red and green contours with area > 100
    red_center_x = DetectRed(frame)
    green_center_x = DetectGreen(frame)

    # Get the height and width of the frame
    height, width = frame.shape[:2]

    # Calculate the x-coordinates to divide the frame into three equal parts
    x1 = width // 3
    x2 = (width // 3) * 2
    center_y = height // 2

    # Drawing the first vertical line
    cv2.line(frame, (x1, 0), (x1, height), (0, 0, 0), 2)

    # Drawing the second vertical line
    cv2.line(frame, (x2, 0), (x2, height), (0, 0, 0), 2)
    
    # Drawing the Y line
    cv2.line(frame, (0, center_y), (width, center_y), (0, 0, 0), 2)

    # Display the appropriate text based on the x-coordinate of the red and green detections
    if red_center_x != -1: 
        if red_center_x < x1:
            cv2.putText(frame, "Zone1 (RED)", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        elif x1 <= red_center_x < x2:
            cv2.putText(frame, "Zone2 (RED)", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        else:
            cv2.putText(frame, "Zone3 (RED)", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    if green_center_x != -1:
        if green_center_x < x1:
            cv2.putText(frame, "Zone1 (GREEN)", (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        elif x1 <= green_center_x < x2:
            cv2.putText(frame, "Zone2 (GREEN)", (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        else:
            cv2.putText(frame, "Zone3 (GREEN)", (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    # Display the frame with the lines and text
    cv2.imshow('Frame', frame)

    # Wait for a key event. If 'q' key is pressed, exit the loop.
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture object
cam.release()

# Destroy all OpenCV windows
cv2.destroyAllWindows()
