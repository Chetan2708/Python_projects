
import  pyautogui

import webbrowser

import time
webbrowser.open('web.whatsapp.com')
time.sleep(30)

count = 10
text = ["hello" ,"I HATE YOU !"]
while count :
    for word in text:
        pyautogui.typewrite(word)
        pyautogui.press('enter')
    count -= 1
