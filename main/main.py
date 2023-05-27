import subprocess
from time import sleep
import pyautogui


#Declare snapchat buttons
snapchat_reply_button = "images/reply_button.png"
snapchat_red_snap_button = "images/red_snap_button.png"
open_chats_button = "images/open_chats_button.png"
login_button = "images/login_button.png"

#Determines whether to press down arrow 1 time or 10 times
press_down_once = 0


#Send snap sequence
def send_snap():
    print("Reading snap...")
    buttonlocx, buttonlocy = pyautogui.locateCenterOnScreen(snapchat_red_snap_button, region=(726,118, 860, 193), confidence=0.5)
    pyautogui.click(buttonlocx, buttonlocy)
    sleep(1.5)
    pyautogui.click()
    sleep(0.5)
    pyautogui.click(buttonlocx + 450, buttonlocy)
    sleep(1.75)
    pyautogui.click(953,935)
    sleep(1)
    pyautogui.click(1210,1050)
    sleep(0.5)
    press_down_once == 0



print('Initialized!')


#Open bluestacks snapchat and OBS, expand to fullscreen
subprocess.Popen(['D:/Program Files/obs-studio/bin/64bit/obs64.exe'], cwd='D:/Program Files/obs-studio/bin/64bit')
sleep(5)
subprocess.Popen(['C:/Program Files/BlueStacks_nxt/HD-Player.exe', '--instance', 'Nougat32', '--cmd', 'launchApp', '--package', 'com.snapchat.android'])
sleep(20)
pyautogui.press('f11')
print('Snapchat now opened in fullscreen!')
sleep(15)


#Checks to see if user needs to log in to snapchat account
if pyautogui.locateCenterOnScreen(login_button, confidence=0.5) != None:
    login_button_locx, login_button_locy = pyautogui.locateCenterOnScreen(login_button, confidence=0.5)
    pyautogui.click(login_button_locx, login_button_locy)
else:
    print("No login found!")


sleep(7)


#If no new chats are found, program ends. If new chats, conversations tab is opened
if pyautogui.locateCenterOnScreen(open_chats_button, confidence=0.38) != None:
    reply_button_locx, reply_button_locy = pyautogui.locateCenterOnScreen(open_chats_button, confidence=0.39)
    pyautogui.click(reply_button_locx, reply_button_locy)
else:
    print("You have no snaps!")
    subprocess.call("TASKKILL /F /IM obs64.exe /T", shell=True)
    subprocess.call("TASKKILL /F /IM HD-Player.exe /T", shell=True)
    exit()


#Checking snaps loop
sleep(3)
for i in range(70):
    sleep(4)
    if pyautogui.locateCenterOnScreen(snapchat_red_snap_button, region=(726,118, 860, 193), confidence=0.5) != None:
       send_snap()
    

    #Presses the down key and restarts loop
    if press_down_once == 1:
        sleep(0.1)
        pyautogui.press('down')
    else:
        for i in range(11):
            sleep(0.1)
            pyautogui.press('down')
            press_down_once = 1