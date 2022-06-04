import pyautogui
import time
import json
import keyboard

def get_locations():
    f = open("Rahool_mats.json")
    data = json.load(f)
    f.close()
    return data

def body():
    while True:
        pyautogui.moveTo(
            material_locs["first"][0], material_locs["first"][1],
            .5, pyautogui.easeInQuad
        )
        pyautogui.click()
        pyautogui.moveTo(
            material_locs["second"][0], material_locs["second"][1],
            .5, pyautogui.easeInQuad
        )
        pyautogui.click()
        pyautogui.moveTo(
            material_locs["third"][0], material_locs["third"][1],
            .5, pyautogui.easeInQuad
        )
        pyautogui.click()
        pyautogui.moveTo(
            material_locs["fourth"][0], material_locs["fourth"][1],
            .5, pyautogui.easeInQuad
        )
        pyautogui.click()

if __name__ == "__main__":
    material_locs = get_locations()
    print("Speak to Rahool and get to his wares.")
    print("Press Space to start.")
    while True:
        if keyboard.is_pressed("space"):
            break
    print("Starting")
    body()