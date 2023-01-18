import os
import cv2
from pathlib import Path

def countFiles(dir):
    aux = 0
    for path in os.listdir(dir):
        if os.path.isfile(os.path.join(dir, path)):
            aux += 1
    return aux

def imgTreatment():
    
    numFiles = countFiles(os.path.join(Path(__file__).parent,"data","captchaDataSet"))
    for i in range(numFiles):
        imgPath = os.path.join(Path(__file__).parent,"data","captchaDataSet",f"img{i+1}.png")
        img = cv2.imread(imgPath)
        gray = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
        _,imgT = cv2.threshold(gray,110,255,cv2.THRESH_TRUNC or cv2.THRESH_OTSU)
        imgT = cv2.adaptiveThreshold(imgT,255,cv2.ADAPTIVE_THRESH_MEAN_C,
        cv2.THRESH_BINARY,47,11)
        cv2.imwrite(os.path.join(Path(__file__).parent,"data","binaryImages",f"img{i+1}.png"),imgT)

if __name__ == "__main__":
    imgTreatment()