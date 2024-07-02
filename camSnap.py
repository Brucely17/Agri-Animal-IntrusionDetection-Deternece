import pyautogui
import time

# time.sleep(5)


# pyautogui.click(x=200,y=200)
# while True:
#     print(pyautogui.position())
#     time.sleep(5)
def camSnsapShot():
    pyautogui.click(x=764, y=1042)
    time.sleep(9)
    # pyautogui.click(x=236, y=72)
    # time.sleep(2)
    # pyautogui.click(x=293, y=481)
    # time.sleep(20)
    # pyautogui.click(x=709, y=225)
    # time.sleep(10)
    # pyautogui.move(x=713, y=881)
    for i in range(4):
        pyautogui.click(x=713, y=881)
        time.sleep(1)
    return True


# camSnsapShot()
