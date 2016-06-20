from .shitlight_simulator.Main import Light
import ctypes
import threading
import queue
import time

q = queue.Queue()
light = Light(5,8)

class simulator_thread(threading.Thread):
    def __init__(self):
        super(simulator_thread, self).__init__()


    def run(self):
        while True:
            item = q.get(True)
            light.set_color(item[1])
            time.sleep(0.01 * item[0])


# use the same frame definition as the real api
class t_chitframe (ctypes.Structure):
    _fields_ = [("brightness", ((ctypes.c_uint8 * 3) * 8 * 5))]


st = simulator_thread()

def init_shitlight():
    st.start()

def add_frame(rep, frame):
    # adapt chitframe to simulator color
    color = []
    for br in frame.brightness:
        for led in br:
            color.append((led[0],led[1],led[2]))
    print(len(color))
    q.put((rep, color))

def get_fps():
    return 100
