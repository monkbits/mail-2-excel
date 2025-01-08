import pyautogui
import pytesseract
import cv2
from PIL import Image

# Specify the path to the Tesseract executable
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\User 1\AppData\Local\Programs\Tesseract-OCR\tesseract.exe' 

def checkScreen(size):
    x, y = pyautogui.position()
    region = (x - size.get("xm",100), y - size.get("ym",50) , size.get("xs",300), size.get("ys",100))  # Define the region (100x100 pixels around the cursor)
    screenshot = pyautogui.screenshot(region=region)
    screenshot.save("screenshot.png")
    text = pytesseract.image_to_string(screenshot)
    return text


def openMail():
    pyautogui.moveTo(98, 19, duration=0.25)
    pyautogui.click();

def copyMailSubject():
    pyautogui.moveTo(661, 266,1);
    pyautogui.click()
    pyautogui.moveTo(662,255,0.2)
    pyautogui.mouseDown()
    pyautogui.moveTo(1712, 253, 1)
    pyautogui.mouseUp()
    pyautogui.keyDown("ctrl")
    pyautogui.press("c")
    pyautogui.keyUp("ctrl")

def copy():
    pyautogui.keyDown("ctrl")
    pyautogui.press("c")
    pyautogui.sleep(0.2)
    pyautogui.keyUp("ctrl")

def paste():
    pyautogui.keyDown("ctrl")
    pyautogui.press("v")
    pyautogui.sleep(0.2)
    pyautogui.keyUp("ctrl")

def goCenterOf(param = None):
    if param == None : return
    image = cv2.imread(param.get("path"))
    location = None
    try:
        location = pyautogui.locateOnScreen(image)
    except pyautogui.ImageNotFoundException:
        print("Image not found on the screen")
        return False
    if location:
        center = pyautogui.center(location)
        pyautogui.moveTo(center)
        return True
    else: 
        print("Image not found on the screen")
        return False



def openSentItems():
    pyautogui.moveTo(128, 321, duration=0.25)
    onSentItem = goCenterOf({"path": "sentitemimg.png"})
    if not onSentItem: onSentItem = goCenterOf({"path": "sentitemactive.png"})
    pyautogui.click()
    pyautogui.sleep(0.5)