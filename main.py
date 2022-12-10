import sys

import cv2
import os
import time
from ffpyplayer.player import MediaPlayer

c = cv2.VideoCapture('original.mp4')
audio = MediaPlayer('original.mp4') # start playing audio immediately.

clearing = 0  # clearing memory
SIZE = (80, 30)  # size of the video
while c.isOpened():  # while video opened
    ta = time.time()  # to calculate delta time which is no longer use
    working, frames = c.read()  # reading file.
    if not working:
        audio.close_player()
        os.system("cls")
        print("This Is The end guys and girls :p . Never gonna give you up, never gonna let you down! ")
        time.sleep(2)
        with open('ricky.txt', "r") as f:
            print(f.read())
        time.sleep(3)
        sys.exit()
    gray = frames[:, :, 0]  # getting B(RGB)

    resized = cv2.resize(gray, SIZE)  # resizing video in grey
    working, new = cv2.threshold(resized, 10, 255, cv2.THRESH_BINARY)  # adding binary value to each color.

    # new[new == 0] = "&" # a cool way to change each character in list !
    # new[new == 1] = " "

    new = new.tolist()
    new_str = str(new)

    new_str = new_str.replace('[', '').replace(']', "").replace(' ', '')  # clearing the shisssh of the string array
    new_str = new_str.replace('0', "&")  # replacing 0 standing for black by & character.
    new_str = new_str.replace('255', " ")  # replacing white color by space.
    new_str = "\n".join(
        new_str[i:i + 2 * SIZE[0]] for i in range(0, len(new_str), 2 * SIZE[0]))  # hard to understand simple
    # it juste adding a "\n" each
    #        160 frames.

    if clearing % 200 == 0:
        os.system("cls")
    new_str = new_str.split(",")  # splitting with coma because it's still a string list.
    print("".join(new_str))  # printing result.
    clearing += 1
    dt = (time.time() - ta) / 1000  # delta time not used anymore.
    time.sleep(dt)
    print("\033[12A")  # the clearing character.

    cv2.imshow('video', gray)  # making video appear on left screen
    if cv2.waitKey(28) & 0xFF == ord('a'):
        break
c.release()
cv2.destroyAllWindows() # after video closing it
