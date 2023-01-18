import os
import cv2
import numpy as np
from pathlib import Path

def countFiles(dir):
    aux = 0
    for path in os.listdir(dir):
        if os.path.isfile(os.path.join(dir, path)):
            aux += 1
    return aux

def lettersCropping():

    imgPath = os.path.join(Path(__file__).parent,"data")
    numFiles = countFiles(os.path.join(Path(__file__).parent,"data","binaryImages"))
    aux = 0
    

    for i in range(4,10):
        
        img = cv2.imread(os.path.join(imgPath,"binaryImages",f"img{i+1}.png"),0)
        imgCopy = img.copy()
        
        img = cv2.GaussianBlur(img,(3,3),1)
        _,thres = cv2.threshold(img, 101, 255,
                         cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (1,1))       
        thres = cv2.morphologyEx(thres,cv2.MORPH_DILATE,kernel)

        cv2.imshow("Teste",thres)
        cv2.waitKey(0)

        cont,_ = cv2.findContours(thres, cv2.RETR_EXTERNAL, 
        cv2.CHAIN_APPROX_SIMPLE)

        letters = []

        for c in cont:
            (x,y,w,h) = cv2.boundingRect(c)
            area = cv2.contourArea(c)
            if area >= 66:
                cv2.rectangle(imgCopy, (x-2,y-2),(x+w+2,y+h+2), (0, 255,0), 2)
                letters.append((x,y,w,h))
        
        for l in letters:
            x,y,w,h = l
            try:
                aux += 1
                path = os.path.join(imgPath,"letters",f"letter{aux}.png")
                #path = os.path.join(imgPath,"teste",f"letter{aux}.png")
                croppedLetter = imgCopy[y-2:y+h+2, x-2:x+w+2]
                cv2.imwrite(path,croppedLetter)
            except:
                continue
        
if __name__ == '__main__':
    lettersCropping()