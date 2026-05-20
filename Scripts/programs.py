import pyautogui
import time

#asks for the program
uiprogram = input("what program do you want to run?: ")
#how many times you want to repeat the process
uicount = input("and for how long?: ")
count = int(uicount)
#sleep so you can focus on terminal
time.sleep(10)

#if you enter 'poop' it constantly sets volume to max and also constantly plays the fart sound effect from repository
if uiprogram == "poop":
    for j in range(1):
        
    pyautogui.write("cd content")
    pyautogui.press('enter')
    time.sleep(5)
    
    for i in range(count):
        
        pyautogui.write("osascript -e \"set volume output volume 100\"")
        pyautogui.press('enter')
        time.sleep(0.1)
        pyautogui.write("afplay Audio/Fart.mp3")
        time.sleep(0.1)
        pyautogui.press('enter')

#hernia opens henrys photo
if uiprogram == "hernia":
    for j in range(1):
        pyautogui.write("cd content")
        pyautogui.press('enter')
        time.sleep(5)
    
    for i in range(count, interval=0.5):
        pyautogui.write("cmd /c start images/hernia.jpg")
        pyautogui.press('enter')
