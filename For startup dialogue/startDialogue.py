import win32api
import win32gui

appCmd = 0x319
mute = 0x80000

#APPCOMMAND_VOLUME_MUTE

# APPCOMMAND_VOLUME_UP 10

hwnd_active = win32gui.GetForegroundWindow()
win32api.SendMessage(hwnd_active, appCmd, None, mute)