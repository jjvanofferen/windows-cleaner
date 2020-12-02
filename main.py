import time
import signal
import random
from mote import Mote
from colorsys import hsv_to_rgb
from RandomColours import RandomColours
from Rainbow import Rainbow

mote = Mote()

mote.configure_channel(1, 16, False)
mote.configure_channel(2, 16, False)
mote.configure_channel(3, 16, False)
mote.configure_channel(4, 16, False)

mote.clear()
mote.show()

colours = RandomColours(random, mote, time)
rainbowColours = Rainbow(mote, time, hsv_to_rgb)

run = True


def runRandomColours():
    signal.signal(signal.SIGINT, signal_handler)

    while run:
        colours.displayColours()
        time.sleep(1)


def runRainbowColours():
    signal.signal(signal.SIGINT, signal_handler)

    while run:
        rainbowColours.rainbow()
        time.sleep(0.01)


menu = {
    "1": ("Random Colours", runRandomColours),
    "2": ("Rainbow", runRainbowColours)
}


def signal_handler(signal, frame):
    global run
    run = False
    mote.clear()
    mote.show()

    ans = input("Make A Choice: ")
    menu.get(ans, [None, invalid])[1]()


def invalid():
    print("INVALID CHOICE!")


for key in sorted(menu.keys()):
    print(key+":" + menu[key][0])

ans = input("Make A Choice")
menu.get(ans, [None, invalid])[1]()

