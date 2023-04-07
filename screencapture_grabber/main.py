from PIL import ImageGrab, Image
import ctypes
import time

user32 = ctypes.windll.user32
isTriggered = lambda triggerKey: user32.GetKeyState(triggerKey) > 1

# Key code for printscreen
VK_F10 = 0x79
VK_SNAPSHOT = 0x2C

# For debouncing
is_key_pressed = {
    VK_SNAPSHOT: False,
    VK_F10: False
}

is_watchdog_loop_enabled = True

file_format = '.png'
output_directory = 'D:\\Desktop'
file_sequence_name = 'screen_capture'
indexer = 0

def save_clipboard_img(indexer):
    time.sleep(.08)
    img = ImageGrab.grabclipboard()
    file_name = f'{output_directory}\\{file_sequence_name}{indexer}{file_format}'
    img.save(file_name)
    print(f'{file_name} created')

print('Starting the watchdog')
while(is_watchdog_loop_enabled):
    try:
        # Screen Capture
        if isTriggered(VK_SNAPSHOT):
            if not is_key_pressed[VK_SNAPSHOT]:
                save_clipboard_img(indexer)
                indexer += 1
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

    except Exception as e:
        print(e.args)
        break
