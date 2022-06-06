import pyautogui
import time
import json
import keyboard
import threading
import sys

def kill_app():
    print("Kill finished.")
    sys.exit()

def kill_switch():
    global kill
    if keyboard.is_pressed("right ctrl"):
        kill = True
        print("Killing application.")
    else:
        time.sleep(0.1)
        kill_switch()

def get_locations():
    f = open("locations.json")
    data = json.load(f)
    f.close()
    return data

def get_to_armor():
    pyautogui.moveTo(
        locations["collections"][0], locations["collections"][1],
        1, pyautogui.easeInQuad
    )
    pyautogui.click()

    pyautogui.moveTo(
        locations["armor_tab"][0], locations["armor_tab"][1],
        1, pyautogui.easeInQuad
    )
    pyautogui.click()

    pyautogui.moveTo(
        locations["leveling"][0], locations["leveling"][1],
        1, pyautogui.easeInQuad
    )
    pyautogui.click()

    pyautogui.moveTo(
        locations["right_arrow"][0], locations["right_arrow"][1],
        1, pyautogui.easeInQuad
    )
    pyautogui.click()
    if kill:
        kill_app()

# def purchase(x, y):
def purchase(points_array):
    # pyautogui.moveTo(x, y, .5, pyautogui.easeInQuad)
    pyautogui.moveTo(
        points_array[0], points_array[1],
        .5, pyautogui.easeInQuad
    )
    pyautogui.mouseDown()
    time.sleep(3.2)
    pyautogui.mouseUp()
    if kill:
        kill_app()

# def delete(x1, y1, x2, y2):
def delete(points_array1, points_array2):
    # pyautogui.moveTo(x1, y1, 1, pyautogui.easeInQuad)
    # pyautogui.moveTo(x2, y2, 1, pyautogui.easeInQuad)
    pyautogui.moveTo(
        points_array1[0], points_array1[1],
        1, pyautogui.easeInQuad
    )
    pyautogui.moveTo(
        points_array2[0], points_array2[1],
        1, pyautogui.easeInQuad
    )
    for i in range(10):
        pyautogui.keyDown("f")
        time.sleep(2)
        pyautogui.keyUp("f")
        if kill:
            kill_app()

def body(buy_helm, buy_arm, buy_chest, buy_leg, buy_class):
    while True:
        # move mouse to armor, leveling, arrow
        get_to_armor()

        # purchase armor
        for i in range(9):
            if buy_helm:
                purchase(locations["helm_buy"])
            if buy_arm:
                purchase(locations["arm_buy"])
            if buy_chest:
                purchase(locations["chest_buy"])
            if buy_leg:
                purchase(locations["leg_buy"])
            if buy_class:                
                purchase(locations["class_item_buy"])
        
        # dismiss
        pyautogui.moveTo(
            locations["dismiss"][0], locations["dismiss"][1],
            1, pyautogui.easeInQuad
        )
        pyautogui.click()

        # sell armor
        # character tab
        pyautogui.moveTo(
            locations["character_tab"][0], locations["character_tab"][1],
            1, pyautogui.easeInQuad
        )
        pyautogui.click()
        if buy_helm:
            delete(locations["helm"], locations["helm_sell"])
        if buy_arm:
            delete(locations["arm"], locations["arm_sell"])
        if buy_chest:
            delete(locations["chest"], locations["chest_sell"])
        if buy_leg:
            delete(locations["leg"], locations["leg_sell"])
        if buy_class:
            delete(locations["class_item"], locations["class_item_sell"])


if __name__ == "__main__":
    buy_helm = True
    buy_arms = True
    buy_chest = True
    buy_legs = True
    buy_class = True
    if len(sys.argv) > 1:
        exclusions = str(sys.argv).split("-x")[1]
        print("Excluding" + exclusions.replace(",", "").replace("'", "").replace("]", ""))
        if "helm" in exclusions:
            buy_helm = False
        if "arms" in exclusions:
            buy_arms = False
        if "chest" in exclusions:
            buy_chest = False
        if "legs" in exclusions:
            buy_legs = False
        if "class" in exclusions:
            buy_class = False
    # give time to click into destiny
    locations = get_locations()
    print("Open up to your character menu [i]")
    print("Press Space to start.")
    while True:
        if keyboard.is_pressed("space"):
            kill = False
            break
    print("Starting.")

    kill_thread = threading.Thread(target=kill_switch)
    kill_thread.start()

    if kill is False:
        body(buy_helm, buy_arms, buy_chest, buy_legs, buy_class)