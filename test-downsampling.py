import shytlight_simulator as shytlight
import time
import cv2
import numpy as np

# initialize threads
shytlight.init_shitlight()


for i in range(10):
  for j in range(200):
    # create image on large basis
    circles = np.zeros((500,800,3))
    # draw a circle with increasing radius
    cv2.circle(circles, (400,250), j*2, (0, 255, 0), 80)
    # blur circle
    bl_circles = cv2.blur(circles, (201,201))
    # resize image to our real led size
    test_geometry = cv2.resize(bl_circles,(8,5))
    # add frame to buffer
    shytlight.add_frame(1, test_geometry)

 
time.sleep(10)

