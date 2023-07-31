import cv2
import numpy as np

def DetectShapes(frame, canny):
    contours, hierarchy = cv2.findContours(canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        print("area =", area)
        if area > 100:
            cv2.drawContours(frame, contours, -1, (255, 0, 255), 1)
            arc = cv2.arcLength(cnt, True)
            poly = cv2.approxPolyDP(cnt, 0.02*arc, True)
            rect = len(poly)
            x, y, w, h = cv2.boundingRect(poly)
            print("x, y, w, h =", x, y, w, h)
            if rect == 3:
                objType = 'Triangle'
            elif rect == 4:
                objType = 'Square'
            elif rect == 5:
                objType = 'Pentagon'
            elif rect == 6:
                objType = 'Hexagon'
            elif rect > 6:
                objType = 'Circle'
            else:
                objType = 'Unknown'
            
            # Calculate the centroid of the shape
            centroid_x = x + (w // 3)
            centroid_y = y + (h // 2)

            # Draw a line passing through the centroid of the shape
            cv2.line(frame, (centroid_x, centroid_y), (frame.shape[1] // 2, frame.shape[0] // 2), (0, 255, 0), 2)

    return frame


cam = cv2.VideoCapture(0)

while True:
    check, frame = cam.read()
    height, width = frame.shape[:2]
    print("height :", height, "width", width)
    center_x, center_y = width // 2, height // 2
    cv2.line(frame, (center_x, 0), (center_x, height), (0, 255, 0), 2)
    cv2.line(frame, (0, center_y), (width, center_y), (0, 255, 0), 2)

    #cv2.imshow('Select Color', frame)
    key = cv2.waitKey(1)
    if key == 27:
        break

    #hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    #pixel_value = hsv_frame[int(hsv_frame.shape[0] / 2), int(hsv_frame.shape[1] / 2)]
    #color_lower = np.array([max(pixel_value[0] - 10, 0), 100, 100])
    #color_upper = np.array([min(pixel_value[0] + 10, 255), 255, 255])

    # Convert the frame to grayscale
    whiteBlack = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Apply Gaussian blur to the grayscale image
    imgBlur = cv2.GaussianBlur(whiteBlack, (7, 7), 1)
    
    # Apply Canny edge detection to the blurred image
    canny = cv2.Canny(imgBlur, 40, 100)

    annotated_frame = DetectShapes(frame, canny)

    cv2.imshow('Annotated Video', annotated_frame)
    key = cv2.waitKey(1)
    if key == 27:
        break

cam.release()
cv2.destroyAllWindows()
