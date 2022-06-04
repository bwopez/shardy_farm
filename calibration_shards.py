import pyautogui
import keyboard
import json
import time

locations = {
    "collections": [], "armor_tab": [], "leveling": [], "right_arrow": [],
    "helm_buy": [], "arm_buy": [], "chest_buy": [], "leg_buy": [], "class_item_buy": [],
    "dismiss": [], "character_tab": [],
    "helm": [], "helm_sell": [], "arm": [], "arm_sell": [], "chest": [], "chest_sell": [], "leg": [], "leg_sell": [],
    "class_item": [], "class_item_sell": [],
}

def change_locations(name):
    while True:
        if keyboard.is_pressed("space"):
            locations[name] = pyautogui.position()
            break
    print("Very good.")
    time.sleep(1)
    print()

def save_to_file(file_name):
    with open(file_name, "w") as f:
        json.dump(locations, f)

if __name__ == "__main__":
    print("Open your character screen [i]")
    print("Hover over the [COLLECTIONS] tab and press the Space key")
    change_locations("collections")
    print("Click the [COLLECTIONS] tab.")

    print("Hover over the [ARMOR] tab and press the Space key")
    change_locations("armor_tab")
    print("Click the [ARMOR] tab.")

    print("Hover over the [LEVELING] tab and press the Space key")
    change_locations("leveling")
    print("Click the [LEVELING] tab.")
    
    print("Hover over the [NEXT PAGE] arrow and press the Space key")
    change_locations("right_arrow")
    print("Click the [NEXT PAGE] arrow.")
    
    print("Hover over the helmet to purchase and press the Space key")
    change_locations("helm_buy")
    
    print("Hover over the arms to purchase and press the Space key")
    change_locations("arm_buy")
    
    print("Hover over the chest to purchase and press the Space key")
    change_locations("chest_buy")
    
    print("Hover over the legs to purchase and press the Space key")
    change_locations("leg_buy")
    
    print("Hover over the class item to purchase and press the Space key")
    change_locations("class_item_buy")
    
    print("Hover over the [Dismiss] button in the bottom right and press the Space key")
    change_locations("dismiss")
    print("Click the [Dismiss] button.")
    
    print("Hover over the [CHARACTER] tab and press the Space key")
    change_locations("character_tab")
    print("Click the [CHARACTER] tab.")    
    
    print("Hover over your helmet slot and press the Space key")
    change_locations("helm")
    
    print("Hover over the FIRST EMPTY SLOT of your helmts and press the Space key")
    change_locations("helm_sell")
    
    print("Hover over your arms slot and press the Space key")
    change_locations("arm")
    
    print("Hover over the FIRST EMPTY SLOT of your arms and press the Space key")
    change_locations("arm_sell")
    
    print("Hover over your chest slot and press the Space key")
    change_locations("chest")
    
    print("Hover over the FIRST EMPTY SLOT of your chest and press the Space key")
    change_locations("chest_sell")
    
    print("Hover over your leg slot and press the Space key")
    change_locations("leg")
    
    print("Hover over the FIRST EMPTY SLOT of your legs and press the Space key")
    change_locations("leg_sell")
    
    print("Hover over your class item slot and press the Space key")
    change_locations("class_item")
    
    print("Hover over the FIRST EMPTY SLOT of your class item and press the Space key")
    change_locations("class_item_sell")
    
    save_to_file("locations.json")
    print("Calibration complete.")