import pyautogui
import keyboard
import json
import time
from calibration_shards import (change_locations, save_to_file)

locations = {
    "first": [], "second": [], "third": [], "fourth": []
}

if __name__ == "__main__":
    print("Talk to Rahool and get to his wares.")
    print("Hover over the first planetary material on sale and press the Space key")
    change_locations("first")

    print("Hover over the second planetary material on sale and press the Space key")
    change_locations("second")

    print("Hover over the third planetary material on sale and press the Space key")
    change_locations("third")

    print("Hover over the fourth planetary material on sale and press the Space key")
    change_locations("fourth")

    save_to_file("Rahool_mats.json")
    print("Calibration complete.")