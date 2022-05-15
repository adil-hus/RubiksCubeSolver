import cv2

colour = []


def colour_spectrum(r, g, b):
    # Get min and max rgb values for all 6 colours.
    # Depending on the lighting in the room and webcams, the min and max
    # rgb values change for each colour. For example in one location the
    # min and max rgb values for blue could be (65, 35, 30), however in
    # another location its values could be (130, 78, 25). This is why
    # it is important to find the min and max rgb values for each colour
    # so the Rubik's Cube Solver can fully function.
    # Finally, return all 6 colours.
    # These rgb ranges were measured at uni in library.
    # if (15 <= r <= 35) and (40 <= g <= 60) and (100 <= b <= 130):
    #     return 'o'
    # elif (30 <= r <= 50) and (45 <= g <= 75) and (25 <= b <= 50):
    #     return 'g'
    # elif (20 <= r <= 46) and (75 <= g <= 115) and (99 <= b <= 135):
    #     return 'y'
    # elif (65 <= r <= 100) and (35 <= g <= 60) and (10 <= b <= 35):
    #     return 'b'
    # elif (20 <= r <= 40) and (20 <= g <= 35) and (75 <= b <= 100):
    #     return 'r'
    # elif (84 <= r <= 130) and (84 <= g <= 130) and (84 <= b <= 120):
    #     return 'w'
    # else:
    #     pass

    # These rgb ranges were measured at home.
    if (20 <= r <= 90) and (50 <= g <= 110) and (120 <= b <= 185):
        return 'o'
    elif (49 <= r <= 110) and (74 <= g <= 130) and (19 <= b <= 80):
        return 'g'
    elif (44 <= r <= 135) and (113 <= g <= 185) and (115 <= b <= 190):
        return 'y'
    elif (110 <= r <= 165) and (57 <= g <= 100) and (0 <= b <= 40):
        return 'b'
    elif (20 <= r <= 60) and (20 <= g <= 50) and (80 <= b <= 145):
        return 'r'
    elif (150 <= r <= 200) and (135 <= g <= 200) and (105 <= b <= 190):
        return 'w'
    else:
        pass


def process_image(img):
    # The cube outline is sliced into 9 square images for
    # accurate colour detection. Using the webcam capture
    # I got the pixel position of all 9 images so the detection
    # process knows where to look at to extract the rgb values
    # of the scanned colours.
    squ1 = img[50:100, 50:100]
    squ2 = img[50:100, 100:150]
    squ3 = img[50:100, 150:200]
    squ4 = img[100:150, 50:100]
    squ5 = img[100:150, 100:150]
    squ6 = img[100:150, 150:200]
    squ7 = img[150:200, 50:100]
    squ8 = img[150:200, 100:150]
    squ9 = img[150:200, 150:200]
    element = [squ1, squ2, squ3, squ4, squ5, squ6, squ7, squ8, squ9]
    for img in element:
        # Each square is split into 3 channels (r, g, b)
        # so the average for each channel can be calculated.
        # The 3 averages for each square is calculated and
        # printed. For example if squ1 scanned the colour
        # red, the values would print out three values in
        # the terminal e.g. (33, 28, 75).
        r, g, b = cv2.split(img)
        r_average = cv2.mean(r)[0]
        g_average = cv2.mean(g)[0]
        b_average = cv2.mean(b)[0]
        balance = (int(r_average), int(g_average), int(b_average))
        print(balance)
        # Using the range from "colour_spectrum", the average rgb values is
        # used to determine the colour of the square. The value of the colour
        # get printed out in the terminal as a single character. For example
        # using the "uni" ranges, (33, 28, 75) is within the range of red, so
        # first it would get stored in the "colour" array and the letter "r"
        # would get printed out in the terminal.
        ret = colour_spectrum(int(r_average), int(g_average), int(b_average))
        colour.append(ret)
    print(colour)
    return colour
