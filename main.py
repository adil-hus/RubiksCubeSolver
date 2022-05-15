from ColourDetection import *
from Algorithm import *
import cv2


colour = []
font = cv2.FONT_HERSHEY_COMPLEX
size = 0.5
hue = (0, 0, 0)
outline = (0, 0, 0)
thickness = 2

# Letters stand for Up, Left, Front, Right, Back, and Down
#             |------------|
#             | U1  U2  U3 |
#             |------------|
#             | U4  U5  U6 |
#             |------------|
#             | U7  U8  U9 |
# |-----------|------------|------------|-----------|
# |L1  L2  L3 | F1  F2  F3 | R1  R2  R3 | B1  B2  B3|
# |-----------|------------|------------|-----------|
# |L4  L5  L6 | F4  F5  F6 | R4  R5  R6 | B4  B5  B6|
# |-----------|------------|------------|-----------|
# |L7  L8  L9 | F7  F8  F9 | R7  R8  R9 | B7  B8  B9|
# |-----------|------------|------------|-----------|
#             | D1  D2  D3 |
#             |------------|
#             | D4  D5  D6 |
#             |------------|
#             | D7  D8  D9 |
#             |------------|


def instructions(img, step):
    # Give first instruction for colour detection
    if step == 1:
        # Up centre is U5
        cv2.putText(window, "Show the face that contains a yellow cube in the centre", (15, 30), font, size, hue)
        cv2.putText(window, "Press the 's' button to start colour extraction", (15, 250), font, size, hue)
        cv2.putText(window, "Press the 'c' button if you want to close the window", (15, 300), font, size, hue)
        cv2.imshow("frame", window)
    # Give second instruction for colour detection
    elif step == 2:
        # Left centre is L5
        cv2.putText(window, "Show the face that contains a blue cube in the centre", (15, 30), font, size, hue)
        cv2.putText(window, "Press the 's' button to continue colour extraction", (15, 250), font, size, hue)
        cv2.putText(window, "If one or more colours isn't extracted", (15, 275), font, size, hue)
        cv2.putText(window, "press the 'c' button to close window and restart process", (15, 300), font, size, hue)
        cv2.imshow("frame", window)
    # Give third instruction for colour detection
    elif step == 3:
        # Front centre is F5
        cv2.putText(window, "Show the face that contains a red cube in the centre", (15, 30), font, size, hue)
        cv2.putText(window, "Press the 's' button to continue colour extraction", (15, 250), font, size, hue)
        cv2.putText(window, "If one or more colours isn't extracted", (15, 275), font, size, hue)
        cv2.putText(window, "press the 'c' button to close window and restart process", (15, 300), font, size, hue)
        cv2.imshow("frame", window)
    # Give fourth instruction for colour detection
    elif step == 4:
        # Right centre is R5
        cv2.putText(window, "Show the face that contains a green cube in the centre", (15, 30), font, size, hue)
        cv2.putText(window, "Press the 's' button to continue colour extraction", (15, 250), font, size, hue)
        cv2.putText(window, "If one or more colours isn't extracted", (15, 275), font, size, hue)
        cv2.putText(window, "press the 'c' button to close window and restart process", (15, 300), font, size, hue)
        cv2.imshow("frame", window)
    # Give fifth instruction for colour detection
    elif step == 5:
        # Back centre is B5
        cv2.putText(window, "Show the face that contains a orange cube in the centre", (15, 30), font, size, hue)
        cv2.putText(window, "Press the 's' button to continue colour extraction", (15, 250), font, size, hue)
        cv2.putText(window, "If one or more colours isn't extracted", (15, 275), font, size, hue)
        cv2.putText(window, "press the 'c' button to close window and restart process", (15, 300), font, size, hue)
        cv2.imshow("frame", window)
    # Give sixth instruction for colour detection
    elif step == 6:
        # Down centre is D5
        cv2.putText(window, "Show the face that contains a white cube in the centre", (15, 30), font, size, hue)
        cv2.putText(window, "Press the 's' button to continue colour extraction", (15, 250), font, size, hue)
        cv2.putText(window, "If one or more colours isn't extracted", (15, 275), font, size, hue)
        cv2.putText(window, "press the 'c' button to close window and restart process", (15, 300), font, size, hue)
        cv2.imshow("frame", window)
    # Give seventh instruction for solving process
    elif step == 7:
        cv2.putText(window, "If one or more colours isn't extracted", (15, 250), font, size, hue)
        cv2.putText(window, "press the 'c' button to close window and restart process", (15, 275), font, size, hue)
        cv2.putText(window, "If all colours have been extracted", (15, 300), font, size, hue)
        cv2.putText(window, "press the 'k' button to start solving process", (15, 325), font, size, hue)
        cv2.imshow("frame", window)
    else:
        pass


# Define a video capture object
video = cv2.VideoCapture(0)
# Define the first step
step = 1
while True:
    # Capture the video frame by frame
    ret, window = video.read()

    # Draw 9 miniature squares to create the Rubik's Cube outline
    squ1 = cv2.rectangle(window, (50, 50), (100, 100), outline, thickness)
    squ2 = cv2.rectangle(window, (100, 50), (150, 100), outline, thickness)
    squ3 = cv2.rectangle(window, (150, 50), (200, 100), outline, thickness)
    squ4 = cv2.rectangle(window, (50, 50), (100, 150), outline, thickness)
    squ5 = cv2.rectangle(window, (100, 50), (150, 150), outline, thickness)
    squ6 = cv2.rectangle(window, (150, 50), (200, 150), outline, thickness)
    squ7 = cv2.rectangle(window, (50, 50), (100, 200), outline, thickness)
    squ8 = cv2.rectangle(window, (100, 50), (150, 200), outline, thickness)
    squ9 = cv2.rectangle(window, (150, 50), (200, 200), outline, thickness)
    # Display the resulting frame with the drawn Rubik's Cube outline
    cv2.imshow('frame', window)
    # Display the instructions on the screen after each next step
    instructions(window, step)
    # The 's' button is set as the colour detection button
    # Everytime the user presses 's' the next instruction
    # is displayed on the screen.
    if cv2.waitKey(1) == ord('s'):
        step = step + 1
        # Message is printed in the terminal
        print("colour extraction process is starting")
        img = window.copy()
        # Call method from ColourDetection class to start colour detection process
        colour = process_image(img)
    # The 'k' button is set as the "start solving process" button
    if cv2.waitKey(1) == ord('k'):
        kociemba(colour)
    # The 'c' button is set as the "close window" button
    if cv2.waitKey(1) == ord('c'):
        break
# After the loop release the capture object
video.release()
# Destroy all the windows
cv2.destroyAllWindows()
