from __future__ import (absolute_import, division,
                        print_function, unicode_literals)

from shitlight_simulator.Main import Light

import ctypes
from ctypes.util import find_library
import threading
try:
    import queue
except ImportError:
    import Queue as queue

import time
import numpy as np

q = queue.Queue()
light = Light(5,8)
# time.sleep(1)

class simulator_thread(threading.Thread):
    def __init__(self):
        super(simulator_thread, self).__init__()
        self.sync_beats = 0


    def run(self):
        internal_beats = 0
        item = q.get(True)
        while True:            
            if self.sync_beats > 0:
                item[0]*=get_bpm()
                if self.sync_beats > 10:
                    if item[2]: internal_beats+=1
                    if internal_beats > _chit.get_beat_count(): internal_beats = sync_beats # counter reset externally
                    if (internal_beats + 2) < _chit.get_beat_count():
                        item[0]/=1.3
                        if item[0] <= 1: continue     
            light.set_color(item[1])
            time.sleep(0.01 * item[0])
            item = q.get(True)
            if self.sync_beats > 10:
                if item[2]:
                    while internal_beats == _chit.get_beat_count():
                        time.sleep(0.01)
                else:
                    if (internal_beats+4) < _chit.get_beat_count():
                        while True:
                            item = q.get(True)
                            if item[2]: 
                                break


# we actually need shitlight library for beat_analysis
# find the shitlight library
_adr = find_library("libshitlight.so")
if _adr is None:
    # test environment? Try again in parent directory
    _chit = ctypes.cdll.LoadLibrary("./libshitlight.so")
    if _chit._name is None:
        # give up
        raise NameError
else:
    _chit = ctypes.cdll.LoadLibrary(_adr)
print(_chit)

# define the function types

_chit.get_fps_limit.argtypes = None
_chit.get_fps_limit.restype = ctypes.c_int

_chit.set_bpm.argtypes = [ctypes.c_float]
_chit.set_bpm.restype = ctypes.c_int

_chit.get_beat_count.argtypes = None
_chit.get_beat_count.restype = ctypes.c_ulong

_chit.get_bpm.argtypes = None
_chit.get_bpm.restype = ctypes.c_double

_chit.get_volume.argtypes = None
_chit.get_volume.restype = ctypes.c_int

_chit.get_analysis_state.argtypes = None
_chit.get_analysis_state.restype = ctypes.c_int

_chit.init_analysis.argtypes = [ctypes.c_int,ctypes.c_char_p]
_chit.init_analysis.restype = ctypes.c_int

_chit.stop_analysis.argtypes = None
_chit.stop_analysis.restype = ctypes.c_int


# use the same frame definition as the real api
class t_chitframe (ctypes.Structure):
    _fields_ = [("brightness", ((ctypes.c_uint8 * 3) * 8 * 5))]


st = simulator_thread()

def init_shitlight():
    _chit.init_nohardware()
    st.start()


def get_bpm():
    bpm = _chit.get_bpm()
    if bpm is None:
        return 120
    else:
        return bpm


def set_bpm(bpm):
    return _chit.set_bpm(bpm) == 1


def get_volume():
    return _chit.get_volume()


def beat_sync(enabled):
    _chit.beat_sync(enabled)
    st.sync_beats = enabled


def get_analysis_state():
    return _chit.get_analysis_state()


def beats(count):
    # converts (fraction of) beats to needed repetitions of frames
    return int(count*_chit.get_fps_limit()*60/120)


def init_analysis(device):
    return _chit.init_analysis(0, device) == 1


def clear_buffer():

    stopping = False
    while not stopping:
        try:
            q.get(False)
        except queue.Empty:
            return

def add_frame(rep, frame, on_beat=False):
    if type(frame) is t_chitframe:
        # adapt chitframe to simulator color
        color = []

        for br in frame.brightness:
            for led in br:
                color.append((led[0],led[1],led[2]))
        q.put((rep, color, on_beat))
    elif type(frame) is np.ndarray:
        # adapt numpy to t_chitframe. Backport to real shitlight!
        temp_frame = t_chitframe()
        # TODO: Trunkate array if longer than our t_chitframe dimensions.
        # TODO: Scale to ubyte if given as float or double
        temp_frame.brightness = np.ctypeslib.as_ctypes(frame.astype("ubyte"))
        
        color = [] 
        for br in temp_frame.brightness:
            for led in br:
                color.append((led[0],led[1],led[2]))
        q.put((rep, color, on_beat))

    else:
        raise NotImplementedError

    while q.qsize() > 1024:
        time.sleep(0.01)

def get_fps():
    return 100
