import cv2
import numpy as np
from PIL import Image


# Function to determine HSV color range based on input BGR color
def get_limits(color):
    c = np.uint8([[color]])  # Convert BGR to numpy array
    hsvC = cv2.cvtColor(c, cv2.COLOR_BGR2HSV)

    hue = hsvC[0][0][0]  # Get the hue value from the converted HSV color

    # Handle red hue wrap-around
    if hue >= 165:  # Upper limit for divided red hue
        lowerLimit_act = np.array([hue - 10, 100, 100], dtype=np.uint8)
        upperLimit_act = np.array([180, 255, 255], dtype=np.uint8)
    elif hue <= 15:  # Lower limit for divided red hue
        lowerLimit_act = np.array([0, 100, 100], dtype=np.uint8)
        upperLimit_act = np.array([hue + 10, 255, 255], dtype=np.uint8)
    else:
        lowerLimit_act = np.array([hue - 10, 100, 100], dtype=np.uint8)
        upperLimit_act = np.array([hue + 10, 255, 255], dtype=np.uint8)

    return lowerLimit_act, upperLimit_act


# Open video capture
cap = cv2.VideoCapture(0)

# BGR color values for detection
red = [0, 0, 255]  # Red
blue = [255, 0, 0]  # Blue
green = [0, 255, 0]  # Green
yellow = [0, 255, 255]  # Yellow

# Parameters for morphological operations
kernel_size = 5

# Capture the initial background image
_, background = cap.read()
background = cv2.cvtColor(background, cv2.COLOR_BGR2GRAY)

while True:
    # Read a frame from the video capture
    ret, frame = cap.read()

    # Convert the current frame to grayscale
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Calculate the absolute difference between the current frame and the background
    diff = cv2.absdiff(gray_frame, background)

    # Threshold the difference image to obtain the foreground mask
    _, thresh = cv2.threshold(diff, 30, 255, cv2.THRESH_BINARY)

    # Morphological operations to clean up the thresholded image
    kernel = np.ones((kernel_size, kernel_size), np.uint8)
    thresh = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)

    # Apply color-based detection on the original frame using the thresholded mask
    hsvImage = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lowerLimit, upperLimit = get_limits(red)
    mask = cv2.inRange(hsvImage, lowerLimit, upperLimit)
    mask = cv2.bitwise_and(mask, thresh)

    # Convert the mask to a PIL Image for further processing
    mask_ = Image.fromarray(mask)

    # Get the bounding box of the detected region in the mask
    bbox = mask_.getbbox()

    # If a bounding box is found, draw a rectangle on the original frame around the detected region
    if bbox is not None:
        x1, y1, x2, y2 = bbox
        frame = cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 5)

    # Display the original frame with the detected region highlighted
    cv2.imshow('frame', frame)

    # Break the loop if the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture object
cap.release()

# Close all OpenCV windows
cv2.destroyAllWindows()
