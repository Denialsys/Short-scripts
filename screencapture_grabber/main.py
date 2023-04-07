from PIL import ImageGrab, Image
import ctypes
import time
import winsound

user32 = ctypes.windll.user32
isTriggered = lambda triggerKey: user32.GetKeyState(triggerKey) > 1

# Key code for printscreen
VK_F10 = 0x79
VK_SNAPSHOT = 0x2C
VK_P = 0x50

# For debouncing
is_key_pressed = {
    VK_SNAPSHOT: False,
    VK_F10: False,
    VK_P: False
}

is_watchdog_loop_enabled = True

file_format = '.png'
output_directory = 'D:\\Desktop'
file_sequence_name = 'screen_capture'

img_coord_stack = []

class POINT(ctypes.Structure):
    _fields_ = [("x", ctypes.c_long), ("y", ctypes.c_long)]


def queryMousePosition():
    pt = POINT()
    ctypes.windll.user32.GetCursorPos(ctypes.byref(pt))
    return { "x": pt.x, "y": pt.y}


def snip_screen_capture():
    pos = queryMousePosition()
    if len(img_coord_stack) < 1:
        img_coord_stack.append(pos)

    else:
        img_coord_stack.append(pos)
        screen_capture = ImageGrab.grab()
        cropped = screen_capture.crop((
            img_coord_stack[0]['x'],
            img_coord_stack[0]['y'],
            img_coord_stack[1]['x'],
            img_coord_stack[1]['y']
        ))

        img_coord_stack.clear()
        save_clipboard_img(cropped)
        winsound.MessageBeep(winsound.MB_OK)


def save_clipboard_img(img=None):
    time.sleep(.08)
    if img is None:
        img = ImageGrab.grabclipboard()

    file_name = f'{output_directory}\\{file_sequence_name}{time.time_ns()}{file_format}'
    img.save(file_name)
    print(f'{file_name} created')


print('Starting the watchdog')
while(is_watchdog_loop_enabled):
    try:
        # Screen Capture
        if isTriggered(VK_SNAPSHOT):
            if not is_key_pressed[VK_SNAPSHOT]:
                save_clipboard_img()
            is_key_pressed[VK_SNAPSHOT] = True
        else:
            is_key_pressed[VK_SNAPSHOT] = False

        # Terminate loop
        if isTriggered(VK_F10):
            if not is_key_pressed[VK_F10]:
                is_watchdog_loop_enabled = False
            is_key_pressed[VK_F10] = True
        else:
            is_key_pressed[VK_F10] = False

        # Snip screen capture
        if isTriggered(VK_P):
            if not is_key_pressed[VK_P]:
                snip_screen_capture()
            is_key_pressed[VK_P] = True
        else:
            is_key_pressed[VK_P] = False

    except Exception as e:
        print(e.args)
        break
