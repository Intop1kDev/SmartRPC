from pypresence import Presence
import time
import ctypes

user32 = ctypes.windll.user32

cli_id = "1516069274119180328"
RPC = Presence(cli_id)
RPC.connect()

start_time = time.time()

icons = {
    "Visual Studio Code": "vscode",
    "Discord": "discord",
    "Vivaldi": "vivaldi",
    "Steam": "steam",
    "Figma": "figma",
    "PowerShell": "terminal",
    "cmd.exe": "terminal",
    "Happ ": "happ",
    "Блокнот": "notepad",
    "Microsoft Edge": "edge"
}

def getWindowText():
    hwnd = user32.GetForegroundWindow()
    buffer = ctypes.create_unicode_buffer(256)

    user32.GetWindowTextW(hwnd, ctypes.byref(buffer), ctypes.sizeof(buffer))

    return buffer.value

def getCursorPos():
    class POINT(ctypes.Structure):
        _fields_ = [
            ("x", ctypes.c_long),
            ("y", ctypes.c_long)
        ]
    cords = POINT()
    user32.GetCursorPos(ctypes.byref(cords))
    return cords.x, cords.y

print(time.time())

time.sleep(1)

while True:
    x, y = getCursorPos()
    windowText = getWindowText()

    image = "unknown"

    for key, value in icons.items():
        if key in windowText:
            image = value
            windowText = key

    RPC.update(
    state="ShitRPC V0.1",
    details=f"MousePos: {x}, {y}",
    name=windowText,
    start=start_time,
    large_image=image,
    buttons=[
        {"label": "GitHub", "url": "https://github.com"}
    ]
)
    time.sleep(15)