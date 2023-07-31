import cv2
import numpy as np

def get_hsv_value(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        pixel_value = hsv[y, x]
        print("HSV Value: ", pixel_value)
        
        # Calculate the lower and upper HSV values by subtracting/adding a range from the clicked pixel value
        lower_hsv = np.array([max(pixel_value[0] - 10, 0), max(pixel_value[1] - 10, 0), max(pixel_value[2] - 10, 0)])
        upper_hsv = np.array([min(pixel_value[0] + 10, 180), min(pixel_value[1] + 10, 255), min(pixel_value[2] + 10, 255)])
        print("Lower HSV: ", lower_hsv)
        print("Upper HSV: ", upper_hsv)

# Create a VideoCapture object to capture video from the camera
cap = cv2.VideoCapture(0)

# Create a window and set the callback function
cv2.namedWindow('Camera')
cv2.setMouseCallback('Camera', get_hsv_value)

while True:
    # Read the video frame
    ret, frame = cap.read()
    
    # Display the frame
    cv2.imshow('Camera', frame)
    
    # Break the loop when the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the VideoCapture object and close the windows
cap.release()
cv2.destroyAllWindows()
