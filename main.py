from pypresence import Presence
import time
import ctypes

user32 = ctypes.windll.user32

cli_id = "1516069274119180328"
RPC = Presence(cli_id)
RPC.connect()

start_time = time.time()

rpc_icons = {
    "Visual Studio Code": "vscode",
    "Discord": "discord",
    "Vivaldi": "vivaldi",
    "Steam": "steam",
    "Figma": "figma",
    "PowerShell": "terminal",
    "cmd.exe": "terminal",
    "Happ ": "happ",
    "Блокнот": "notepad",
    "Edge": "edge",
    "Program Manager": "windows"
}

rpc_buttons = [
            {"label": "GitHub", "url": "https://github.com/Intop1kDev/SmartRPC"}
]

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
    return (cords.x, cords.y)

print(time.time())

time.sleep(1)

is_afk = False
until_afk = 4
prev_x, prev_y = (0, 0)

while True:
    (x, y) = getCursorPos()

    if (x, y) == (prev_x, prev_y):  
        until_afk -= 1
        if until_afk == 0:
            is_afk = True
    else:
        until_afk = 4
        is_afk = False
    
    if not is_afk:
        windowText = getWindowText()

        image = "unknown"

        for key, value in rpc_icons.items():
            if key in windowText:
                image = value
                windowText = key
    else:
        windowText = "AFK"
        image = "afk"

    RPC.update(
    state="ShitRPC V0.1",
    details=f"MousePos: {x}, {y}",
    name=windowText,
    start=start_time,
    large_image=image,
    buttons=rpc_buttons
    )
    prev_x = x
    prev_y = y
    time.sleep(15)