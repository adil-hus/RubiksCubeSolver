import cv2
from rubik_solver import utils

colour = (255, 255, 255)
thickness = 2
outline = (0, 0, 0)
font = cv2.FONT_HERSHEY_COMPLEX
size = 0.5
size_2 = 2
hue = (0, 0, 0)

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


def kociemba(colour_list):
    # Using the quotation marks as a separator,
    # join all the items in 'cube' into a string.
    cube = ''.join(str(i) for i in colour_list)
    # Use the 'Kociemba' algorithm to solve the cube
    a = utils.solve(cube, 'Kociemba')
    solution_string = a
    for i in solution_string:
        i = str(i)
        if len(i) > 1:
            if i[1] == '2':
                p = i[0]
                position = solution_string.index(i)
                solution_string.remove(i)
                solution_string.insert(position, p)
                solution_string.insert(position, p)
            elif i == "B":
                # In the string, index() finds the B instruction
                # (Back clockwise face rotation) and get replaced
                # with 3 instructions (B' --> up, U, down)
                position = solution_string.index(i)
                solution_string.remove(i)
                solution_string.insert(position, "up")
                solution_string.insert(position, "U")
                solution_string.insert(position, "down")
            elif i == "B'":
                # In the string, index() finds the B' instruction
                # (Back counterclockwise face rotation) and gets replaced
                # with 3 instructions (B' --> up, U', down)
                position = solution_string.index(i)
                solution_string.remove(i)
                solution_string.insert(position, "up")
                solution_string.insert(position, "U'")
                solution_string.insert(position, "down")

            else:
                continue
    # Print the solution steps in the terminal
    print(solution_string)

    window_reset_count = 120
    window_idx = 0
    solution_guide = 0

    # Define a video capture object
    video = cv2.VideoCapture(0)
    while True:
        # Capture the video frame by frame
        ret, window = video.read()

        # Draw 9 miniature squares to create the Rubik's Cube outline
        cv2.rectangle(window, (50, 50), (100, 100), outline, thickness)
        cv2.rectangle(window, (100, 50), (150, 100), outline, thickness)
        cv2.rectangle(window, (150, 50), (200, 100), outline, thickness)
        cv2.rectangle(window, (50, 50), (100, 150), outline, thickness)
        cv2.rectangle(window, (100, 50), (150, 150), outline, thickness)
        cv2.rectangle(window, (150, 50), (200, 150), outline, thickness)
        cv2.rectangle(window, (50, 50), (100, 200), outline, thickness)
        cv2.rectangle(window, (100, 50), (150, 200), outline, thickness)
        cv2.rectangle(window, (150, 50), (200, 200), outline, thickness)
        # Display the new resulting frame with the drawn
        # Rubik's Cube outline for the solution guide.
        cv2.imshow('frame', window)

        # Once the solution guide is finished let the user
        # know by telling them the cube has been solved.
        if solution_guide >= len(solution_string) - 1:
            cv2.putText(window, "Cube solved!!!", (15, 250), font, size_2, hue)
            cv2.imshow("frame", window)
            # Once the cube has been solved press
            # the 'c' button to close the window.
            if cv2.waitKey(10) == ord('c'):
                break
            continue

        # Give each step a few seconds before
        # moving on to the next so the
        # user has time to rotate the correct
        # sides and get ready for the next step.
        window_idx += 1
        if window_idx > window_reset_count:
            cv2.putText(window, "next step", (15, 250), font, size_2, hue)

            solution_guide += 1
            window_idx = 0

        # Assign each letter solution to an arrow solution.
        # Using the solution_string, display the set of
        # arrow solutions inside the Rubik's Cube outline to
        # help the user visualise what rotations to undertake
        # in order to solve their Rubik's Cube.
        solution = solution_string[solution_guide]
        if solution == "U":
            # arrow starts at position 3 and goes across to position 1 e.g. U3 to U1
            cv2.arrowedLine(window, (200, 75), (50, 75), colour, thickness)
        elif solution == "U'":
            # arrow starts at position 1 and goes across to position 3 e.g. U1 to U3
            cv2.arrowedLine(window, (50, 75), (200, 75), colour, thickness)
        elif solution == "D":
            # arrow starts at position 7 and goes across to position 9 e.g. U7 to U9
            cv2.arrowedLine(window, (50, 175), (200, 175), colour, thickness)
        elif solution == "D'":
            # arrow starts at position 9 and goes across to position 7 e.g. U9 to U7
            cv2.arrowedLine(window, (200, 175), (50, 175), colour, thickness)
        elif solution == "R":
            # arrow starts at position 9 and goes up to position 3 e.g. U9 to U3
            cv2.arrowedLine(window, (175, 200), (175, 50), colour, thickness)
        elif solution == "R'":
            # arrow starts at position 3 and goes down to position 9 e.g. U3 to U9
            cv2.arrowedLine(window, (175, 50), (175, 200), colour, thickness)
        elif solution == "L":
            # arrow starts at position 1 and goes down to position 7 e.g. U1 to U7
            cv2.arrowedLine(window, (75, 50), (75, 200), colour, thickness)
        elif solution == "L'":
            # arrow starts at position 7 and goes up to position 1 e.g. U7 to U1
            cv2.arrowedLine(window, (75, 200), (75, 50), colour, thickness)
        elif solution == "F":
            # arrow instructs the player to rotate the face clockwise
            cv2.arrowedLine(window, (125, 75), (175, 120), colour, thickness)
            cv2.arrowedLine(window, (175, 125), (130, 175), colour, thickness)
            cv2.arrowedLine(window, (125, 175), (80, 125), colour, thickness)
            cv2.arrowedLine(window, (75, 125), (125, 80), colour, thickness)
        elif solution == "F'":
            # arrow instructs the player to rotate the face counterclockwise
            cv2.arrowedLine(window, (175, 125), (125, 75), colour, thickness)
            cv2.arrowedLine(window, (120, 85), (75, 125), colour, thickness)
            cv2.arrowedLine(window, (75, 130), (125, 175), colour, thickness)
            cv2.arrowedLine(window, (130, 175), (175, 130), colour, thickness)
        elif solution == "up":
            # Up means moving the cube upwards, so the user ends on the face
            # below e.g. starting position is the red centre and moving the cube
            # downwards means the user will end on the face with the white centre.
            # arrow starts at position 7 and goes up to position 1 e.g. U7 to U1
            cv2.arrowedLine(window, (75, 200), (75, 50), colour, thickness)
            # arrow starts at position 8 and goes up to position 2 e.g. U8 to U2
            cv2.arrowedLine(window, (125, 200), (125, 50), colour, thickness)
            # arrow starts at position 9 and goes up to position 3 e.g. U9 to U3
            cv2.arrowedLine(window, (175, 200), (175, 50), colour, thickness)
        elif solution == "right":
            # Right means turning the cube right, so the user ends on the left sided face
            # e.g. starting position is the red centre and turning the cube
            # right means the user will end on the face with the blue centre.
            # arrow starts at position 1 and goes across to position 3 e.g. U1 to U3
            cv2.arrowedLine(window, (50, 75), (200, 75), colour, thickness)
            # arrow starts at position 4 and goes across to position 6 e.g. U4 to U6
            cv2.arrowedLine(window, (50, 125), (200, 125), colour, thickness)
            # arrow starts at position 7 and goes across to position 9 e.g. U7 to U9
            cv2.arrowedLine(window, (50, 175), (200, 175), colour, thickness)
        elif solution == "down":
            # Down means moving the cube downwards, so the user ends on the face
            # above e.g. starting position is the red centre and moving the cube
            # downwards means the user will end on the face with the yellow centre.
            # arrow starts at position 1 and goes down to position 7 e.g. U1 to U7
            cv2.arrowedLine(window, (75, 50), (75, 200), colour, thickness)
            # arrow starts at position 2 and goes down to position 8 e.g. U2 to U8
            cv2.arrowedLine(window, (125, 50), (125, 200), colour, thickness)
            # arrow starts at position 3 and goes down to position 9 e.g. U3 to U9
            cv2.arrowedLine(window, (175, 50), (175, 200), colour, thickness)
        elif solution == "left":
            # Left means turning the cube left, so the user ends on the right sided face
            # e.g. starting position is the red centre and turning the cube
            # left means the user will end on the face with the green centre.
            # arrow starts at position 3 and goes across to position 1 e.g. U3 to U1
            cv2.arrowedLine(window, (200, 75), (50, 75), colour, thickness)
            # arrow starts at position 6 and goes across to position 4 e.g. U6 to U4
            cv2.arrowedLine(window, (200, 125), (50, 125), colour, thickness)
            # arrow starts at position 9 and goes across to position 7 e.g. U9 to U7
            cv2.arrowedLine(window, (200, 175), (50, 175), colour, thickness)
        # Display the resulting frame with the drawn
        # Rubik's Cube outline and a set of arrow solutions.
        cv2.imshow("frame", window)
        # The 'c' button is set as the "close window" button
        if cv2.waitKey(10) == ord('c'):
            break
