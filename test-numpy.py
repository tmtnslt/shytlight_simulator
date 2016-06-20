import shytlight_simulator as shytlight
import time
import numpy as np

# initialize threads
shytlight.init_shitlight()

# Be sure to create the array with the right dimension (5,8,3). Color values go from 0..255
# Behaviour for floating types is currently untested!
color_test = np.zeros((5,8,3))
for j in range(5):
  for i in range(8):
    color_test[j,i,1] = 0xff
 
shytlight.add_frame(100, color_test)
time.sleep(10)

