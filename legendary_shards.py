import pyautogui
import time
import json
import keyboard

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

def body():
    while True:
        # pyautogui.write("iaa", interval=0.8)
        # manually open up Character menu

        # move mouse to armor, leveling, arrow
        get_to_armor()

        # purchase armor
        for i in range(10):
            purchase(locations["helm_buy"])
            purchase(locations["arm_buy"])
            purchase(locations["chest_buy"])
            purchase(locations["leg_buy"])
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
        delete(locations["helm"], locations["helm_sell"])
        delete(locations["arm"], locations["arm_sell"])
        delete(locations["chest"], locations["chest_sell"])
        delete(locations["leg"], locations["leg_sell"])
        delete(locations["class_item"], locations["class_item_sell"])


if __name__ == "__main__":
    # give time to click into destiny
    locations = get_locations()
    print("Open up to your character menu [i]")
    print("Press Space to start.")
    while True:
        if keyboard.is_pressed("space"):
            break
    print("Starting.")
    body()