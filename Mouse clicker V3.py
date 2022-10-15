'''This is an auto mouse Clicker
    auto click starts when the triger key was held down
    Programmed at windows 7 ultimate
'''

import ctypes
import time

user32 = ctypes.windll.user32
# isTriggered = lambda triggerKey: (user32.GetKeyState(triggerKey) > 1 and
#                                   user32.GetKeyState(triggerKey) )
isTriggered = lambda triggerKey: user32.GetKeyState(triggerKey) > 1
VK_triggerKey = 0x14 ## The capslock virtual key code
VK_triggerKey = 0x04 ## Middle mouse click virtual key code
VK_addDelay = 0x6B ## Add key
VK_decDelay = 0x6D ## subtract key
VK_C = 0x43
VK_return = 0x0D
VK_key1 = '\x12'
g_isReturnPressed = False

g_isAddPressed = False
g_isDecPressed = False
g_isCPressed = False
g_triggerState = user32.GetKeyState
g_switch = True
g_delayInterval = .047 ##optimal so far
g_delayGranules = 0.002
g_lastClick = 0

g_recognitionOnGoing = False    ## State of recognition
g_baseline = 0                  ## The initial timing
G_SWITCHINTERVAL = .3           ## Threshold time to consider the press
g_switchCount = 0              ## The number of registered switches

def clickMouseLeft():
    '''Send the click buttion command'''
    ##Left mouse button
    user32.mouse_event(2,0,0,0,0) ##press down
    time.sleep(.0001)
    user32.mouse_event(4,0,0,0,0) ##release
    time.sleep(.0001)

def keyPress(keyCode):
    '''Press down then up a key'''
    user32.keybd_event(ord(keyCode),0,0,0) ##press down
    time.sleep(.0001)
    user32.keybd_event(ord(keyCode),0,2,0,0) ##release
    time.sleep(.0001)

def blockPolicy(keyCode):
    time.sleep(.4)
    user32.keybd_event(ord(keyCode),0,0,0) ##press down
    time.sleep(2)
    keyPress('B')
    user32.keybd_event(ord(keyCode),0,2,0,0) ##release
    time.sleep(.03)
    keyPress('\r')
    print ("Firewall policy blocked")
    
## Starcraft 2 Game
def terranBio():
    '''Rapid fire config for terran bio'''
    keyPress('A')
    keyPress('D')
    keyPress('A')
    keyPress('E')

def terranMules():
    '''Rapid fire config for terran bio'''
    keyPress('E')
    clickMouseLeft()

def protossGatewayUnits():
    keyPress('Z')
    clickMouseLeft()
    keyPress('S')
    clickMouseLeft()


def recognizeSwitches(triggerCount, baseLine):
    '''
    Determine the count and pattern of keypress
    :param triggerCount: Number of keypress
    :param baseLine: The last keypress timestamp
    :return: the current number of keypress or 0 if the series was processed
    '''
    global g_recognitionOnGoing

    ## Check if the recognition was on going
    if g_recognitionOnGoing:

        ## If the delay has exceeded the switch interval threshold,
        ## its time to recognize the state
        if time.time() - baseLine >= 1:
            print (f"Trigger state {triggerCount}")
            if triggerCount == 3:
                print("Target state has enabled")

            elif triggerCount == 4:
                print("Target state has disabled")

            else:
                print("Recognition done, unrecognized state")

            g_recognitionOnGoing = False
            triggerCount = 0

        return triggerCount
    else:
        return triggerCount

def startMain():
    '''Starts the clicking if the trigger was high
    also plays a sound ok if activated and sound iconhand on deactivation'''

    global g_lastClick, g_delayInterval
    global isDecPressed, g_isAddPressed, g_isReturnPressed
    global g_switchCount, g_baseline, g_recognitionOnGoing, g_isCPressed

    while(g_switch):
        ##since the keystate picks up the keystate of other keys theres a 
        ##confusion in the return value so we need to read the State twice
        # if isTriggered(VK_triggerKey):
        #     if time.time() - g_lastClick >= g_delayInterval:
        #         g_lastClick = time.time()
        #         clickMouseLeft()
        #
        # ## For increasing delay between clicks
        # if isTriggered(VK_addDelay):
        #     if not g_isAddPressed:
        #         g_delayInterval += g_delayGranules
        #         print(f'Delay interval increased to: {g_delayInterval}')
        #     g_isAddPressed = True
        # else:
        #     g_isAddPressed = False

        # ## For decreasing delay between clicks
        # if isTriggered(VK_decDelay):
        #     if not g_isDecPressed and g_delayInterval - g_delayGranules > 0:
        #         g_delayInterval -= g_delayGranules
        #         print(f'Delay interval decreased to: {g_delayInterval}')
        #     g_isDecPressed = True
        # else:
        #     g_isDecPressed = False

        ## Windows firewall policy blocker
        # if isTriggered(VK_return):
        #     if not g_isReturnPressed:
        #         blockPolicy(VK_key1)
        #         print("policy triggered")
        #     g_isReturnPressed = True
        # else:
        #     g_isReturnPressed = False

        ## Recognize the series of keypress if
        if isTriggered(VK_C):

            if not g_isCPressed:
                # print(f"Time pressed: {time.time()} ")
                if g_recognitionOnGoing:
                    # print(f"trigger count {g_switchCount}")
                    if time.time() - g_baseline < G_SWITCHINTERVAL:
                        g_switchCount += 1
                        g_baseline = time.time()        ## Set a new baseline
                else:
                    g_recognitionOnGoing = True
                    g_baseline = time.time()
                    g_switchCount += 1

            g_isCPressed = True
        else:
            g_isCPressed = False

        g_switchCount = recognizeSwitches(g_switchCount, g_baseline)

            
##Safety delay before starting
##time.sleep(2)
print('Clicker started')

startMain()
