import pyautogui
import keyboard
import time
import tomllib

with open("config.toml", "rb") as f:
    config = tomllib.load(f)

enabled_sword = False
enabled_pickaxe = False
interval = config["interval"]
next_click = 0.0


def sword():
    global enabled_sword, next_click, enabled_pickaxe
    enabled_pickaxe = False
    pyautogui.mouseUp()
    enabled_sword = not enabled_sword
    if enabled_sword:
        next_click = time.time()


def pickaxe():
    global enabled_pickaxe, enabled_sword
    enabled_sword = False
    enabled_pickaxe = not enabled_pickaxe
    if enabled_pickaxe:
        pyautogui.mouseDown()
    else:
        pyautogui.mouseUp()


def off():
    global enabled_pickaxe, enabled_sword
    enabled_pickaxe = False
    enabled_sword = False
    pyautogui.mouseUp()


keyboard.add_hotkey(config["off_hotkey"], off)
keyboard.add_hotkey(config["sword_hotkey"], sword)
keyboard.add_hotkey(config["pickaxe_hotkey"], pickaxe)

print(
    f"Clicker started!\nSword: {config['sword_hotkey']}\nPickaxe: {config['pickaxe_hotkey']}\nOff: {config['off_hotkey']}"
)

while True:
    now = time.time()
    if enabled_sword and now >= next_click:
        pyautogui.click()
        next_click = now + interval
    time.sleep(0.01)
