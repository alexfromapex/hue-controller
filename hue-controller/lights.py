import threading
import globals
import random

class LightThread(threading.Thread):
    def __init__(self,function_name):
        super(LightThread, self).__init__()
        self._stop = threading.Event()

    def stop(self):
        self._stop.set()

    def stopped(self):
        return self._stop.isSet()

def allOn(self):
    try:
        globals.b.set_light(globals.lights,'on',True)
    except KeyboardInterrupt:
        sys.exit(1)

def allOff(self):
    try:
        globals.b.set_light(globals.lights,'on',False)
    except KeyboardInterrupt:
        sys.exit(1)

def lightFunc(self):
    try:
        globals.b.set_light(globals.lights, 'bri', 254)
        for light_id in globals.lights:
            color1 = random.random()
            color2 = random.random()
            name = globals.b.get_light(light_id,'name')
            print(name,':')
            print(color1,color2)
            globals.b.set_light(light_id, 'xy',[color1,color2])
    except KeyboardInterrupt:
        sys.exit(0)
