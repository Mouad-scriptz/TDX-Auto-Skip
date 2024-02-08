MOUSE_EVENT_LEFTDOWN = 0x0002
MOUSE_EVENT_LEFTUP = 0x0004
MOUSE_EVENT_MOVE = 0x0001

import ctypes, win32api

user32 = ctypes.windll.user32

mouse_event = user32.mouse_event
SetCursorPos = user32.SetCursorPos


class Cursor:
    def set_position(x: int, y: int) : 
        win32api.SetCursorPos((x, y))

    def left_click():
        mouse_event(MOUSE_EVENT_MOVE, 1, 1, 0, 0)
        mouse_event(MOUSE_EVENT_LEFTDOWN, 0, 0, 0, 0)
        mouse_event(MOUSE_EVENT_LEFTUP, 0, 0, 0, 0)
