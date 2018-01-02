import ImageGrab
import os
import time
import win32api, win32con
import ImageOps
from numpy import *

"""
All coordinates assume a screen resolution of 1280x1024, and Chrome
maximized with the Bookmarks Toolbar enabled.
Down key has been hit 4 times to center play area in browser.
x_pad = 156
y_pad = 345
Play area =  x_pad+1, y_pad+1, 796, 825
"""

"""
 Plate cords:
 
    87, 208
    194, 208
    288, 208
    395, 208
    491, 208
    591, 208
"""

# Globals
# ------------------

x_pad = 345
y_pad = 365

class Cord:
     
    f_shrimp = (40,340)
    f_rice = (90, 340)
    f_nori = (40, 387)
    f_roe = (90, 387)
    f_salmon = (40, 440)
    f_unagi = (90, 440)
     
#-----------------------------------    
     
    phone = (574, 358)
 
    menu_toppings = (528, 273)
     
    t_shrimp = (495, 224)
    t_nori = (490, 287)
    t_roe = (574, 279)
    t_salmon = (494, 340)
    t_unagi = (576, 218)
    t_exit = (591, 342)
 
    menu_rice = (532, 293)
    buy_rice = (548, 281)
     
    delivery_norm = (490, 292)

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

      def clear_tables():
          mousePos((87, 208))
          leftClick()

          mousePos((194, 208))
          leftClick()

          mousePos((288, 208))
          leftClick()

          mousePos((395, 208))
          leftClick()

          mousePos((491, 208))
          leftClick()

          mousePos((591, 208))
          leftClick()
          time.sleep(1)

      def makeFood(food):
          if food == 'caliroll':
              print 'Making a caliroll'
              mousePos(Cord.f_rice)
              leftClick()
              time.sleep(.05)
              mousePos(Cord.f_nori)
              leftClick()
              time.sleep(.05)
              mousePos(Cord.f_roe)
              leftClick()
              time.sleep(.1)
              foldMat()
              time.sleep(1.5)
           
          elif food == 'onigiri':
              print 'Making a onigiri'
              mousePos(Cord.f_rice)
              leftClick()
              time.sleep(.05)
              mousePos(Cord.f_rice)
              leftClick()
              time.sleep(.05)
              mousePos(Cord.f_nori)
              leftClick()
              time.sleep(.1)
              foldMat()
              time.sleep(.05)
               
              time.sleep(1.5)
       
          elif food == 'gunkan':
              mousePos(Cord.f_rice)
              leftClick()
              time.sleep(.05)
              mousePos(Cord.f_nori)
              leftClick()
              time.sleep(.05)
              mousePos(Cord.f_roe)
              leftClick()
              time.sleep(.05)
              mousePos(Cord.f_roe)
              leftClick()
              time.sleep(.1)
              foldMat()
              time.sleep(1.5)

      def foldMat():
          mousePos((Cord.f_rice[0]+40,Cord.f_rice[1])) 
          leftClick()
          time.sleep(.1)


      def buyFood(food):
           
          mousePos(Cord.phone)
           
          mousePos(Cord.menu_toppings)
           
           
          mousePos(Cord.t_shrimp)
          mousePos(Cord.t_nori)
          mousePos(Cord.t_roe)
          mousePos(Cord.t_salmon)
          mousePos(Cord.t_unagi)
          mousePos(Cord.t_exit)
           
          mousePos(Cord.menu_rice)
          mousePos(Cord.buy_rice)
           
          mousePos(Cord.delivery_norm)

      def screenGrab():
          b1 = (x_pad + 1,y_pad+1,x_pad+641,y_pad+481)
          im = ImageGrab.grab(b1)
       
          ##im.save(os.getcwd() + '\\Snap__' + str(int(time.time())) +'.png', 'PNG')
          return im

def main():
    pass

if __name__ == '__main__':
    main()
