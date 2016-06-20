# shytlight_simulator
Hardware API compatible simulator for shitlight

This module adapts the shitlight_simulator for the real API provided by shytlight.

## Usage:

clone repository with submodule and place in a valid import location. Then, write your shitlight pattern as usual*, but instead of

    import shytlight
    
use:

    import shytlight_simulator as shytlight
    
    
Have fun!

\* See the tutorial in "test-shytlight.py". If you want to run this file, you need to place it somewhere, where it can import shytlight_simulator of course. If you want to use numpy arrays instead of the internal t_chitframes, see "test-numpy.py"

## Requirements:
* Python 3
* pyqt5
* numpy

## Goodies:
Check "test-downsampling.py" on how to use downsampling to create smooth transitions. Requires cv2
