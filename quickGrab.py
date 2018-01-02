"""

All coordinates assume a screen resolution of 1280x1024, and Chrome
maximized with the Bookmarks Toolbar enabled.
Down key has been hit 4 times to center play area in browser.
x_pad = 156
y_pad = 345
Play area =  x_pad+1, y_pad+1, 796, 825
"""

# Globals
# ------------------

x_pad = 345
y_pad = 365

import ImageGrab
import os
import time

def screenGrab():
    box = (x_pad+1,y_pad+1, x_pad+641, y_pad+481)
    im = ImageGrab.grab(box)
    im.save(os.getcwd() + '\\full_snap__' + str(int(time.time())) +
'.png', 'PNG')

def main():
    screenGrab()

if __name__ == '__main__':
    main()