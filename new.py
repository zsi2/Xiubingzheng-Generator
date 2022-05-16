import cv2 as cv
import numpy as np

from PIL import Image, ImageDraw, ImageFont
 
def cv2ImgAddText(img, text, left, top, textColor=(0, 255, 0), textSize=20):
    if (isinstance(img, np.ndarray)):  # 判断是否OpenCV图片类型
        img = Image.fromarray(cv.cvtColor(img, cv.COLOR_BGR2RGB))

    draw = ImageDraw.Draw(img)

    fontStyle = ImageFont.truetype("./simsun.ttc", textSize, encoding="utf-8")
 
    draw.text((left, top), text, textColor, font=fontStyle)
   
    return cv.cvtColor(np.asarray(img), cv.COLOR_RGB2BGR)
 


tbid= input()
kbxbz= cv.imread("./kb.jpg")
xbz=kbxbz.copy()
#print(kbxbz)
x=596
y=415



cv.imwrite("./xbz.png",cv2ImgAddText(xbz,tbid,x,y,(0,0,0),60),[int(cv.IMWRITE_PNG_COMPRESSION),0])