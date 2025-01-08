import pyautogui
import pytesseract
import pyperclip
from funcs import *
from PIL import Image
import cv2

# Specify the path to the Tesseract executable
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\User 1\AppData\Local\Programs\Tesseract-OCR\tesseract.exe' 
ss_size = { 
       "sentItem":  {"xm": 80 , "ym": 50, "xs": 250 , "ys": 50},
       "d"       :  {"xm": 100 , "ym": 50, "xs": 300 , "ys": 100},
}

def organisePullReq():
    openMail()

    pyautogui.moveTo(128, 321, duration=0.25)
    # checkScreen(ss_size["sentItem"])
    # cnt = 0;
    goCenterOf({"path": "sentitemimg.png"})
    image_path = 'sentitemimg.png'
    image = cv2.imread(image_path)
    location = None
    try:
        location = pyautogui.locateOnScreen(image)
    except pyautogui.ImageNotFoundException:
        print("Image not found on the screen")
        return
    if location:
        center = pyautogui.center(location)
        pyautogui.moveTo(center)
    else: 
        print("Image not found on the screen")
        exit()
    # while "Sent items" not in checkScreen(ss_size["sentItem"]) and "Sent Items" not in checkScreen(ss_size["sentItem"]) and "SENT ITEMS" not in checkScreen(ss_size["sentItem"]) and cnt < 100:
    #     vx , vy = pyautogui.position()
    #     print(checkScreen(ss_size["sentItem"]))
    #     pyautogui.moveTo(vx,vy + 15 , duration=0.25)
    #     cnt += 1
    #     print("Scrolling-------------------")
    # print("Sent Items found")
    pyautogui.click()

    pyautogui.moveTo(452, 338, duration=0.50)
    exit()
    isPullRequest = checkScreen()
    c = 1
    print(isPullRequest)

    if "Pull Request" in isPullRequest or "PULL REQUEST" in isPullRequest:
        print("Pull Request found")
        pyautogui.click()
        copyMailSubject()
        pyautogui.moveTo(150, 24,1)
        pyautogui.click()
        pyautogui.moveTo(135,309,1)
        pyautogui.click()
        mainSub = pyperclip.paste()
        checkScreen()
        copy()
        count = 0;
        while (len(pyperclip.paste().strip()) > 0 and pyperclip.paste().strip() != None) and count < 100:
            print(pyperclip.paste().strip())
            pyautogui.press("down")
            pyautogui.scroll(-20)
            pyautogui.sleep(0.8)
            copy()
            count += 1
        pyautogui.write(mainSub)
        exit()
    while ("Pull Request" not in isPullRequest and "PULL REQUEST" not in isPullRequest) and c < 10:
        pyautogui.scroll(-150)
        print("Scrolling-------------------" + str(c))
        print(checkScreen())
        c += 1
        
    pyautogui.scroll(-200)

    
organisePullReq()