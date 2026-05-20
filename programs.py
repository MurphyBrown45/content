import pyautogui
import time

#asks for the program
uiprogram = input("what program do you want to run?: ")
#how many times you want to repeat the process
uicount = input("and for how long?: ")
count = int(uicount)
#sleep so you can focus on terminal
time.sleep(20)

#if you enter 'poop' it constantly sets volume to max and also constantly plays the fart sound effect from repository
if uiprogram == "poop":
    pyautogui.write("cd content")
    time.sleep(1)
    pyautogui.press('enter')
    for i in range(count):
        pyautogui.write("osascript -e \"set volume output volume 100\"")
        pyautogui.press('enter')
        pyautogui.write("afplay Audio/Fart.mp3")
        pyautogui.press('enter')

#hernia opens henrys photo
if uiprogram == "hernia":
    pyautogui.write("cd content")
    time.sleep(1)
    pyautogui.press('enter')
    for i in range(count):
        pyautogui.write("start images/hernia.jpg")
        pyautogui.press('enter')


        
    