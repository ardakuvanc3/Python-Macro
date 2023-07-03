import keyboard
from pynput.keyboard import Controller as keyboard_controller 
from pynput.mouse import Controller as mouse_controller
from pynput.mouse import *
import pyautogui
import time
import ctypes
import datetime
from colorama import Fore, Back, Style, init



print(Fore.LIGHTBLUE_EX+ """                                                                         
  _ __ ___    __ _   ___  _ __  ___  
 | '_ ` _ \  / _` | / __|| '__|/ _ \ 
 | | | | | || (_| || (__ | |  | (_) |
 |_| |_| |_| \__,_| \___||_|   \___/                                                                     
""")
print(Style.RESET_ALL)


print("Kullanmak istediğiniz makrolari e kullanmak istemediğiniz makrolari ise h harfi ile seçebilirsiniz")

leftClickAsk = input("Sol makroyu kullanmak ister misiniz?: ")

if leftClickAsk == "e":
    leftClickKey = input("Makroyu hangi tuşa atamak istersiniz?: ")

rightClickAsk = input("Sağ makroyu kullanmak ister misiniz?: ")

if rightClickAsk == "e":
    rightClickKey=input("Makroyu hangi tuşa atamak istersiniz?: ")

rodAsk = input("Olta Makrosunu kullanmak ister misiniz?: ")

if rodAsk == "e":
    rodSlot = input("Oltayi hangi slotta kullanıyorsunuz?: ")
    rodClickKey = input("Makroyu hangi tuşa atamak istersiniz?: ")


speedBridgeAsk = input("Hizli Köprü Makrosunu kullanmak ister misiniz?: ")

if speedBridgeAsk == "e":
    speedBridgeKey = input("Makroyu hangi tuşa atamak istersiniz?: ")
    speedBridgeBlock = input("Kaç Blokluk yol yapmak istersiniz?: ")

CPS = int(input("Kaç CPS yapmak istiyorsunuz? (craftrise öneri(18)): "))
exitTask = input("Makroyu hangi tuşla kapatmak istersiniz?: ")

if CPS == 0:
    delay = 0
else:
    delay = 1/CPS

mouse = mouse_controller()
keys = keyboard_controller()

while True:
    if(leftClickAsk =="e"):
        if keyboard.is_pressed(leftClickKey):
            for i in range(1):
                mouse.click(Button.left)
                time.sleep(delay)
    if(rightClickAsk == "e"):
        if keyboard.is_pressed(rightClickKey):
            for i in range(1):
                mouse.click(Button.right)
                time.sleep(delay)

    if(rodAsk == "e"):
        if keyboard.is_pressed("c"):
            for i in range(1):
                mouse.click(Button.left)
                time.sleep(delay)
                pyautogui.press(rodSlot)
                mouse.click(Button.right)
                time.sleep(delay)
                pyautogui.press("1")

    if(speedBridgeAsk == "e"):
        for i in range(int(speedBridgeBlock)):
            pyautogui.keyDown("shift")
            pyautogui.keyDown("s")
            time.sleep(0.2)
            pyautogui.click(Button.right)
            pyautogui.keyUp("shift")
        pyautogui.keyUp("s")
        pyautogui.keyUp("w")
        time.sleep(2)
        pyautogui.keyUp("s")

    if keyboard.is_pressed(exitTask):
        print("Makro Kapandi")
        ctypes.windll.user32.MessageBoxA(0, "Makro Kapandi","Biliglendirme",1)
        exit()