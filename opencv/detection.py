from opencv.detection_utils import *
from opencv.finger_counter import *

def detect():
    aWeight = 0.5
    camera = cv.VideoCapture(0)
    top,right,bottom,left = 80,350,295,590
    num_frames = 0
    calibrated = False

    while(True):
        (grabbed,frame) = camera.read()
        frame = imutils.resize(frame,width=700)
        frame = cv.flip(frame,1)
        clone = frame.copy()
        (height,width) = frame.shape[:2]
        roi = frame[top:bottom,right:left]
        gray = cv.cvtColor(roi,cv.COLOR_BGR2GRAY)
        gray = cv.GaussianBlur(gray,(7,7),0)
        if num_frames < 30:
            find_run_avg(gray,aWeight)
            if num_frames == 1:
                print("Calibrating...")
            elif num_frames == 29:
                print("Calibration successfull")
        else:
            hand = segment(gray)
            if hand is not None:
                (thresholded,segmented) = hand
                cv.drawContours(clone,[segmented+(right,top)],-1,(0,0,255))
                fingers = count_fingers(thresholded,segmented)
                cv.putText(clone, str(fingers), (70, 45), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
                cv.imshow("Thresholded",thresholded)
        cv.rectangle(clone,(left,top),(right,bottom),(0,255,0),2)
        num_frames +=1
        cv.imshow("Video Feed",clone)
        keypress = cv.waitKey(1) & 0xFF
        if keypress == ord("q"):
            break
    camera.release()
    cv.destroyAllWindows()