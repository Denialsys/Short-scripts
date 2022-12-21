'''
    Author: Jenver I
    Keyboard target key watchdog.
    Component for remote control using PC
    Compatible for windows only can be used without external libraries
'''

import ctypes

IS_ON = True
TARGET_KEYS = ['W', 'A', 'S', 'D',
               'Q', 'E', '1', '2',
               '3', '4']

##user32 = ctypes.windll.user32
keyState = ctypes.windll.user32.GetKeyState

## ## Inefficient approach, limitation of old Windows OS
##isTriggered = lambda triggerKey: (user32.GetKeyState(triggerKey) > 1 and
##                                  user32.GetKeyState(triggerKey) )

isPressed = lambda key: (keyState(key) > 1 and keyState(key) )

def watchKeys():

    ##create the dictionary for keystates
    keyStates = {}
    for char in TARGET_KEYS:
        keyStates[ord(char)] = { 'isPressed': False, 'isToggled': False}

    ##watch for keypresses
    while(IS_ON):

        ##check each target keys
        for key in keyStates.keys():
            if isPressed(key):
                if not keyStates[key]['isPressed']:
                    keyStates[key]['isToggled'] = True
                    print (f'{chr(key)} was pressed, {keyStates[key]["isToggled"]}')

                keyStates[key]['isPressed'] = True
            else:
                if keyStates[key]['isToggled']:
                    keyStates[key]['isToggled'] = False
                    print(f'{chr(key)} was lifted, {keyStates[key]["isToggled"]}')

                keyStates[key]['isPressed'] = False
