import pyautogui
import time
import cv2
import numpy as np

while True:
    if pyautogui.locateCenterOnScreen('yeme.png'):
        a = pyautogui.locateCenterOnScreen('yeme.png')
        pyautogui.click(a)
        break
while True:
    if pyautogui.locateCenterOnScreen('all.png'):
        time.sleep(0.5)
        '''pyautogui.click(548, 500)
        time.sleep(2.5)
        pyautogui.click(147, 361)'''
        pyautogui.screenshot('scrs.png', region=(90,220,530,400))
        img_seat = cv2.imread('scrs.png')
        seat_r = cv2.imread('box.png')
        w, h = img_seat.shape[:-1]
        res = cv2.matchTemplate(img_seat, seat_r, cv2.TM_CCOEFF_NORMED)
        threshold = 0.7
        loc = np.where(res >= threshold)
        seat_rPt = (0,0)
        for pt in zip(*loc[::-1]):
            print (pt)                                                                                 
            seat_rPt = pt                                                                                        
            cv2.rectangle(img_seat, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)
            break
        cv2.imwrite('scrs2.png', img_seat)
        x = seat_rPt[0] + 93
        y = seat_rPt[1] + 223
        seat_rPt1 = (x,y)
        print(seat_rPt1)
        pyautogui.click(seat_rPt1)
        pyautogui.click(852, 625)
        time.sleep(0.5)
        pyautogui.click(pyautogui.locateCenterOnScreen('zero.png'))
        time.sleep(0.5)
        pyautogui.click(603, 266)
        pyautogui.click(844, 624)
        time.sleep(0.5)
        pyautogui.click(437, 227)
        pyautogui.typewrite("자신의 생년월일")
        pyautogui.click(844, 624)
        time.sleep(0.5)
        pyautogui.click(60, 297)
        break