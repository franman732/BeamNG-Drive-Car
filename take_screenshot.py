import pyautogui
import cv2
import time
import numpy as np

time.sleep(3)

pil_image = pyautogui.screenshot()

numpyImage = np.array(pil_image)

opencvImage = cv2.cvtColor(numpyImage, cv2.COLOR_RGB2BGR)

cv2.imshow("SCREENSHOT", opencvImage)
cv2.waitKey(0)
cv2.destroyAllWindows()