# import the necessary package
from __future__ import print_function

import cv2
import imutils
import argparse
from imutil import FPS
from imutil import WebCamVideoStream

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("-n", "--num-frames", type=int, default=100,
            help="# of frames to loop over FPS test")
    ap.add_argument("-d", "--display", type=int, default=-1,
            help="whether or not frames should be displayed")
    args = vars(ap.parse_args())

    # grab a pointer to the video stream and initialize the FPS counter
    print ("[INFO] sampling frames from webcam")
    stream = WebCamVideoStream(src=0).start()
    fps = FPS().start()

    # loop over some frames
    while fps._numFrames < args["num_frames"]:
        # grab the frame from the stream and resize it to have a maximum 
        # width of 400 pixels
        frame = stream.read()
        frame = imutils.resize(frame, width=400)

        # check to see if the frame should be displayed on screen
        if args["display"] > 0:
            cv2.imshow("Frame", frame)
            key = cv2.waitKey(1) & 0xff

        # update the fps counter
        fps.update()

    # stop the timer and display the information
    fps.stop()
    print ("[INFO] elapsed time : {:.2f}".format(fps.elapsed()))
    print ("[INFO] approx. FPS: {:.2f}".format(fps.fps()))

    # do a bit of cleanup
    stream.stop()
    cv2.destroyAllWindows()



