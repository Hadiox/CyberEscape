import cv2 as cv

background = None


def find_run_avg(image, accWeight):
    global background
    if background is None:
        background = image.copy().astype("float")
        return
    cv.accumulateWeighted(image, background, accWeight)


def segment(image, threshold=25):
    global background
    diff = cv.absdiff(background.astype("uint8"), image)
    thresholded = cv.threshold(diff, threshold, 255, cv.THRESH_BINARY)[1]
    (cnts, _) = cv.findContours(thresholded.copy(), cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    if len(cnts) == 0:
        return
    else:
        segmented = max(cnts, key=cv.contourArea)
        return (thresholded, segmented)
