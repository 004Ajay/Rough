import win32api
import win32gui

WM_APPCOMMAND = 0x319

for i in range(15): # running 15 times means increasing volume by 30 points, i.e, (no_of_times * 2 vol_points)
    vol_inc = 0xA0000 # Virtual-Key Code for increasing volume
    hwnd_active = win32gui.GetForegroundWindow() # Getting active window
    win32api.SendMessage(hwnd_active, WM_APPCOMMAND, None, vol_inc) # Executing command
    # APPCOMMAND_VOLUME_MUTE(8) (0xFFFF + 1) * 8 = 0x80000
    # APPCOMMAND_VOLUME_UP (10) (0xFFFF + 1) * 10 = 0xA0000
    