from sklearn.metrics import pairwise
import cv2 as cv
import numpy as np


def count_fingers(thresholded, segmented):
    chull = cv.convexHull(segmented)

    extreme_top = tuple(chull[chull[:, :, 1].argmin()][0])
    extreme_bottom = tuple(chull[chull[:, :, 1].argmax()][0])
    extreme_left = tuple(chull[chull[:, :, 0].argmin()][0])
    extreme_right = tuple(chull[chull[:, :, 0].argmax()][0])
    center_x = (extreme_left[0] + extreme_right[0]) / 2
    center_y = (extreme_top[1] + extreme_bottom[1]) / 2
    distance = \
    pairwise.euclidean_distances([(center_x, center_y)], Y=[extreme_left, extreme_right, extreme_bottom, extreme_top])[
        0]
    max_distance = distance[distance.argmax()]
    radius = int(0.8 * max_distance)
    circumference = (2 * np.pi * radius)
    circular_roi = np.zeros(thresholded.shape[:2], dtype="uint8")
    cv.circle(circular_roi, (int(center_x), int(center_y)), radius, 255, 1)
    circular_roi = cv.bitwise_and(thresholded, thresholded, mask=circular_roi)
    cnts, hierarchy = cv.findContours(circular_roi.copy(), cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)
    count = 0
    for c in cnts:
        (x, y, w, h) = cv.boundingRect(c)
        if ((center_y + (center_y * 0.25)) > (y + h)) and ((circumference * 0.25) > c.shape[0]):
            count += 1
    return count
