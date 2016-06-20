import shytlight_simulator as shytlight
import time

# initialize threads
shytlight.init_shitlight()

# create new frame instances
test_red = shytlight.t_chitframe()
test_green = shytlight.t_chitframe()
test_blue = shytlight.t_chitframe()

# make all leds one color, test each primary color
# first index is boards (in simulator x dimension)
# second index is LEDs per board (in simulator y dimension)
# third index is brightness value for red, green, blue (0..255)
for j in range(5):
  for i in range(8):
    test_green.brightness[j][i][0] = 0x00
    test_green.brightness[j][i][1] = 0xff
    test_green.brightness[j][i][2] = 0x00
    test_red.brightness[j][i][0] = 128
    test_red.brightness[j][i][1] = 0x00
    test_red.brightness[j][i][2] = 0x00
    test_blue.brightness[j][i][0] = 0xff
    test_blue.brightness[j][i][1] = 0x00
    test_blue.brightness[j][i][2] = 0x00

# now add frames to the buffer,
# first argument is the times the frame should be repeated
# second argument is the instance of frame that should be drawn
# frames will be drawn with 100fps
# if there are no new frames to be drawn, the last frame will be repeated
# note that add_frame will return instantly, as long as there is free memory in the buffer
shytlight.add_frame(200, test_green) 
shytlight.add_frame(200, test_red) 
shytlight.add_frame(200, test_blue) 
shytlight.add_frame(200, test_green) 
shytlight.add_frame(200, test_red) 
shytlight.add_frame(200, test_blue) 
shytlight.add_frame(200, test_green) 
shytlight.add_frame(200, test_red) 
shytlight.add_frame(200, test_blue) 
shytlight.add_frame(200, test_green) 
shytlight.add_frame(200, test_red) 
shytlight.add_frame(200, test_blue) 
shytlight.add_frame(200, test_green) 
shytlight.add_frame(200, test_red) 
shytlight.add_frame(200, test_blue) 
shytlight.add_frame(200, test_green) 
shytlight.add_frame(200, test_red) 
shytlight.add_frame(200, test_blue) 

# now sleep, otherwise threads will finish
time.sleep(1)

# to get the real fps from the board, use get_fps().
print(shytlight.get_fps())
time.sleep(1)
print(shytlight.get_fps())
time.sleep(1000)
print(shytlight.get_fps())

