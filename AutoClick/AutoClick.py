import pyautogui
import time


for i in range(0, 100):
    pyautogui.PAUSE = 0
    time.sleep(10)
    pyautogui.typewrite('3')
    print("Отзываем льва")
    
    time.sleep(9)
    pyautogui.typewrite('3')
    print("Призываем льва")
    
    time.sleep(5)
    pyautogui.press('4')
    print("Отправляем льва в атаку")
    
    time.sleep(5)
    pyautogui.press('t')
    print("Побежали по кругу")
    
    time.sleep(300)