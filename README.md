# color_detection_region_highlight
Real-Time Color Detection and Region Highlighting using OpenCV
This Python script leverages the OpenCV library to perform real-time color detection and region highlighting in a video stream from the default camera. 
The primary color of interest (in this case, red) is specified, and the script identifies and highlights the corresponding color region within each frame.

Components:
Function: get_limits(color)

Purpose: Determines the HSV color range for a given BGR color.
Input: BGR color value.
Output: Lower and upper HSV limits for color detection.
Video Capture Initialization:

Opens the default camera using cv2.VideoCapture(0).
Color Specification:

BGR color values are defined for the colors to be detected (e.g., red, blue, green, yellow).
Background Initialization:

Captures an initial background frame to be used for background subtraction.
Main Loop (Real-Time Video Processing):

Reads frames from the video capture in real-time.
Converts each frame to grayscale.
Calculates the absolute difference between the grayscale frame and the background.
Thresholding and Morphological Operations:

Applies thresholding to create a binary mask highlighting differences.
Utilizes morphological operations to clean up the binary mask.
Color-Based Detection:

Converts the current frame to the HSV color space.
Determines the HSV color range for the specified color (e.g., red) using the get_limits function.
Creates a color mask by applying the determined color range to the HSV frame.
Combines the color mask with the thresholded mask using bitwise AND.
Region Highlighting:

Converts the resulting mask to a PIL Image for further processing.
Retrieves the bounding box of the detected region in the mask.
If a bounding box is found, a rectangle is drawn on the original frame around the detected region.
Display:

Displays the original frame with the highlighted color region in real-time.
Termination:

The script continues to run until the 'q' key is pressed, upon which the video capture is released, and all OpenCV windows are closed.
Usage:
Run the script to open a window showing the real-time video feed.
The script will detect and highlight the specified color region in each frame.
Press the 'q' key to close the window and terminate the script.
Note:
Adjustments to the color range and morphological operations may be necessary based on lighting conditions and specific color variations in the environment.
This script serves as a practical example of real-time color detection and region highlighting and can be extended for various applications, such as object tracking or gesture recognition.
