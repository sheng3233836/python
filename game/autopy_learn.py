import autopy
import win32api, win32con, win32gui
import random


def _MyCallback(hwnd, extra):
    hwnds, classes = extra
    hwnds.append(hwnd)
    classes[win32gui.GetClassName(hwnd)] = hwnd


def win32_learn():
    # windows = []
    # classes = {}
    # win32gui.EnumWindows(_MyCallback, (windows, classes))
    wnhd = win32gui.FindWindow(0, 'TCDEV - Google Chrome')
    print(wnhd)
    win32gui.SetForegroundWindow(wnhd)
    # win32gui.PostMessage(wnhd, win32con.WM_CHAR, 'asfdsf', 0)
    win32api.keybd_event(70, 0)
    win32api.keybd_event(70, 0, win32con.KEYEVENTF_KEYUP, 0)
    # win32api.keybd_event(17, 0)
    # win32api.keybd_event(76, 0)
    # win32api.keybd_event(76, 0, win32con.KEYEVENTF_KEYUP, 0)
    # win32api.keybd_event(17, 0, win32con.KEYEVENTF_KEYUP, 0)
    win32gui.PostMessage(wnhd, win32con.WM_CHAR, 'f', 0)



def left_click(x=None, y=None):
    if x and y:
        win32api.SetCursorPos([x, y])
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN | win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)


def autopy_bitmap_learn():
    screen_bitmap = autopy.bitmap.capture_screen()
    print(format_color(screen_bitmap.get_color(1, 1)))
    screen_bitmap.save('screen.bmp')
    rubbish = autopy.bitmap.Bitmap.open('rubbish.bmp')
    screen_bitmap = autopy.bitmap.capture_screen()
    pos = screen_bitmap.find_bitmap(rubbish)
    if pos:
        print("find, the position:", pos[0], pos[1])
    else:
        print("not find")


def format_color(rgb_color):
    return hex(autopy.color.rgb_to_hex(rgb_color[0], rgb_color[1], rgb_color[2]))


# left_click()
win32_learn()
# autopy_bitmap_learn()
