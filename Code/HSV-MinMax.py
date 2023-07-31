import cv2
import numpy as np

def nothing(x):
    pass

# Create a window
cv2.namedWindow('Color Detection')
cv2.resizeWindow('Color Detection', 600, 400)

# Create trackbars for color change
# Hue is from 0-179 for OpenCV
cv2.createTrackbar('HMin', 'Color Detection', 0, 179, nothing)
cv2.createTrackbar('SMin', 'Color Detection', 0, 255, nothing)
cv2.createTrackbar('VMin', 'Color Detection', 0, 255, nothing)
cv2.createTrackbar('HMax', 'Color Detection', 0, 179, nothing)
cv2.createTrackbar('SMax', 'Color Detection', 0, 255, nothing)
cv2.createTrackbar('VMax', 'Color Detection', 0, 255, nothing)

# Set default value for Max HSV trackbars
cv2.setTrackbarPos('HMax', 'Color Detection', 179)
cv2.setTrackbarPos('SMax', 'Color Detection', 255)
cv2.setTrackbarPos('VMax', 'Color Detection', 255)

# Initialize HSV min/max values
hMin = sMin = vMin = hMax = sMax = vMax = 0
phMin = psMin = pvMin = phMax = psMax = pvMax = 0

# Create a VideoCapture object to capture video from the camera (0 for the default camera)
cap = cv2.VideoCapture(0)

while(1):
    # Read the video frame
    ret, image = cap.read()

    # Resize the camera frame to a smaller size while maintaining the aspect ratio
    resized_cam_frame = cv2.resize(image, (400, 300))

    # Get current positions of all trackbars
    hMin = cv2.getTrackbarPos('HMin', 'Color Detection')
    sMin = cv2.getTrackbarPos('SMin', 'Color Detection')
    vMin = cv2.getTrackbarPos('VMin', 'Color Detection')
    hMax = cv2.getTrackbarPos('HMax', 'Color Detection')
    sMax = cv2.getTrackbarPos('SMax', 'Color Detection')
    vMax = cv2.getTrackbarPos('VMax', 'Color Detection')

    # Set minimum and maximum HSV values to display
    lower = np.array([hMin, sMin, vMin])
    upper = np.array([hMax, sMax, vMax])

    # Convert to HSV format and color threshold
    hsv = cv2.cvtColor(resized_cam_frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, lower, upper)
    result = cv2.bitwise_and(resized_cam_frame, resized_cam_frame, mask=mask)

    # Print if there is a change in HSV value
    if((phMin != hMin) | (psMin != sMin) | (pvMin != vMin) | (phMax != hMax) | (psMax != sMax) | (pvMax != vMax) ):
        print("(hMin = %d , sMin = %d, vMin = %d), (hMax = %d , sMax = %d, vMax = %d)" % (hMin , sMin , vMin, hMax, sMax , vMax))
        phMin = hMin
        psMin = sMin
        pvMin = vMin
        phMax = hMax
        psMax = sMax
        pvMax = vMax

    # Place the HSV trackbars on the left side of the window
    hsv_trackbars = np.zeros((300, 200, 3), dtype=np.uint8)
    cv2.putText(hsv_trackbars, 'HSV Trackbars', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
    cv2.imshow('Color Detection', np.hstack((hsv_trackbars, resized_cam_frame)))

    # Place the color detection result (right side of the window)
    cv2.imshow('Result', result)
    
    # Break the loop when the 'q' key is pressed
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

# Release the VideoCapture object and close the window
cap.release()
cv2.destroyAllWindows()
