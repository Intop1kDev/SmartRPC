from pypresence import Presence
import time
import ctypes

CLIENT_ID = "1516069274119180328"
RPC = Presence(CLIENT_ID)
RPC.connect()

START_TIME = time.time()

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

class _POINT(ctypes.Structure):
        _fields_ = [
            ("x", ctypes.c_long),
            ("y", ctypes.c_long)
        ]

class WinAPIFunctions:
    _user32 = ctypes.windll.user32

    @staticmethod
    def get_window_text():
        hwnd = WinAPIFunctions._user32.GetForegroundWindow()
        buffer = ctypes.create_unicode_buffer(256)

        WinAPIFunctions._user32.GetWindowTextW(hwnd, ctypes.byref(buffer), ctypes.sizeof(buffer))

        return buffer.value
    @staticmethod
    def get_cursor_pos():
        cords = _POINT()
        WinAPIFunctions._user32.GetCursorPos(ctypes.byref(cords))
        return (cords.x, cords.y)

def main():
    is_afk = False
    until_afk = 4
    prev_x, prev_y = (0, 0)

    while True:
        (x, y) = WinAPIFunctions.get_cursor_pos()

        if (x, y) == (prev_x, prev_y):  
            until_afk -= 1
            if until_afk == 0:
                is_afk = True
        else:
            until_afk = 4
            is_afk = False
        
        if not is_afk:
            windowText = WinAPIFunctions.get_window_text()

            image = "unknown"

            for key, value in rpc_icons.items():
                if key in windowText:
                    image = value
                    windowText = key
        else:
            windowText = "AFK"
            image = "afk"

        RPC.update(
        state="ShitRPC V0.2",
        details=f"MousePos: {x}, {y}",
        name=windowText,
        start=START_TIME,
        large_image=image,
        buttons=rpc_buttons
        )
        prev_x = x
        prev_y = y
        time.sleep(15)

if __name__ == "__main__":
    main()