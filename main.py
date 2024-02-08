import time, pyautogui
from win32gui import GetForegroundWindow, SetForegroundWindow, FindWindow
from cursor import Cursor

screen_size = pyautogui.size()
x, y = int(screen_size[0] * (862 / 1600)), int(screen_size[1] * (129 / 900))
roblox_hwnd = FindWindow(None, 'Roblox')
cursor = Cursor

while True:
    if (
        GetForegroundWindow() == roblox_hwnd and 
        pyautogui.pixel(x, y) == (0, 0, 0)
    ):
        print("Skipping.")

        SetForegroundWindow(roblox_hwnd)
        time.sleep(.1)

        position = pyautogui.position()

        cursor.set_position(x,y)
        cursor.left_click()

        time.sleep(.05)

        cursor.set_position(position.x, position.y)
        cursor.left_click()

        time.sleep(3) # You can adjust this as you like.
