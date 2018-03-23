from lights import lightFunc as lf
from lights import allOn as ao
from lights import allOff as aoff

def init():
    global b
    global lightFunc
    global allOn
    global allOff
    global lights
    lightFunc = lf
    allOn = ao
    allOff = aoff
