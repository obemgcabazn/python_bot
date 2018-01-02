import ImageGrab
import os
import time
import win32api, win32con

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

def leftClick():
      win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
      time.sleep(.1)
      win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
      print "Click."          #completely optional. But nice for debugging purposes.

def leftDown():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(.1)
    print 'left Down'

def leftUp():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    time.sleep(.1)
    print 'left release'

def mousePos(cord):
    win32api.SetCursorPos((x_pad + cord[0], y_pad + cord[1]))

def get_cords():
    x,y = win32api.GetCursorPos()
    x = x - x_pad
    y = y - y_pad
    print x,y

def startGame():
      #location of first menu
      mousePos((296, 200))
      leftClick()
      time.sleep(.1)

      #location of second menu
      mousePos((315, 393))
      leftClick()
      time.sleep(.1)

      #location of third menu
      mousePos((585, 453))
      leftClick()
      time.sleep(.1)

      #location of fourth menu
      mousePos((309, 384))
      leftClick()
      time.sleep(.1)


def main():
    pass

if __name__ == '__main__':
    main()
