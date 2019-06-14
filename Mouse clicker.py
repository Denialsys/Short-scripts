'''This is an auto mouse Clicker
    The capslock is the trigger key that starts the clicking
    Programmed at windows 7 ultimate
'''

import ctypes
import winsound
from time import sleep
from threading import Thread

g_user32 = ctypes.windll.user32
g_mouseEvent = g_user32.mouse_event

VK_triggerKey = 0x14 ## The capslock key

g_triggerState = g_user32.GetKeyState
g_switch = True

def clickMouse():
    '''Send the click buttion command'''
    ##Left mouse button
    g_mouseEvent(2,0,0,0,0) ##click down
    g_mouseEvent(4,0,0,0,0) ##release
    
    ##Right mouse button
##    g_mouseEvent(8,0,0,0,0)
##    g_mouseEvent(10,0,0,0,0)

def startMain():
    '''Starts the clicking if the trigger was high
    also plays a sound ok if activated and sound iconhand on deactivation'''

    m_hasSounded = False
    while(g_switch):
        ##since the keystate picks up the keystate of other keys theres a 
        ##confusion in the return value so we need to read the State twice
        if g_triggerState(VK_triggerKey) > 0 and g_triggerState(VK_triggerKey):
            if not m_hasSounded:
                ##Beep on activation
                winsound.MessageBeep(winsound.MB_OK)
                m_hasSounded = True
            clickMouse()
        else:
            if m_hasSounded:
                ##Beep if deactivated
                winsound.MessageBeep(winsound.MB_ICONHAND)
                m_hasSounded = False

        ##delay between click
        sleep(.10)
            
sleep(3)
print('Clicker started')
##create a safety feature that will stop the system upon activate for 10 mins
Thread (target = startMain ).start()
