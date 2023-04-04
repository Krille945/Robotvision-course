import cv2 as cv
import numpy as np
#https://docs.opencv.org/4.x/d7/d4d/tutorial_py_thresholding.html
#importing a Video
cap = cv.VideoCapture(1)
#define width
cap.set(3,1000) #width of webcam
cap.set(4,1000) # height

def stackImages(scale,imgArray):
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range (0, rows):
            for y in range(0,cols):
                if imgArray [x][y].shape[:2] == imgArray[0][0].shape[:2]:
                    imgArray[x][y] = cv.resize(imgArray[x][y], (0,0), None, scale, scale)
                else:
                    imgArray[x][y] = cv.resize(imgArray[x][y], (imgArray[0][0].shape[1],imgArray[0][0].shape[0]), None, scale, scale)
                if len(imgArray[x][y]) == 2: imgArray[x][y]= cv.cvtColor(imgArray[x][y], cv.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank]*rows
        hor_con = [imageBlank]*rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv.resize(imgArray[x], (0,0), None, scale, scale)
            else:
                imgArray[x]= cv.resize(imgArray[x], (imgArray[0].shape[1],imgArray[0].shape[0]), None, scale, scale)
            if len(imgArray[x]) == 2: imgArray[x]= cv.cvtColor(imgArray[x], cv.COLOR_GRAY2BGR)   
        hor = np.hstack(imgArray)
        ver = hor 
    return ver


def empty(a):
    pass

cv.namedWindow("TrackBars")
#resize window
cv.resizeWindow("TrackBars",640,240)

#create first track bar hue min

#val min
cv.createTrackbar("Val Min","TrackBars",0,255,empty)
#val max
cv.createTrackbar("Val Max","TrackBars",255,255,empty)
cv.createTrackbar("Blur Val","TrackBars",0,100,empty)

while True:
#While i can succesfully insert a image from video in img it will run
    succes, img = cap.read()
    img_result=img.copy()
    img= cv.cvtColor(img,cv.COLOR_BGR2GRAY) 

    v_min=cv.getTrackbarPos("Val Min","TrackBars")
    v_max=cv.getTrackbarPos("Val Max","TrackBars")
    b=cv.getTrackbarPos("Blur Val","TrackBars")
    # global thresholding
    ret1,th1 = cv.threshold(img,v_min,v_max,cv.THRESH_BINARY)
    # Otsu's thresholding
    ret2,th2 = cv.threshold(img,v_min,v_max,cv.THRESH_BINARY+cv.THRESH_OTSU)
    # Otsu's thresholding after Gaussian filtering
    blur = cv.GaussianBlur(img,(5,5),b)
    ret3,th3 = cv.threshold(blur,v_min,v_max,cv.THRESH_BINARY+cv.THRESH_OTSU)

    result1 = cv.bitwise_and(img_result,img_result,mask= th1)
    result2 = cv.bitwise_and(img_result,img_result,mask= th2)
    result3 = cv.bitwise_and(img_result,img_result,mask= th3)

    #result1 = cv.bitwise_and(img, th1)
    #result2 = cv.bitwise_and(img, th2)
    #result3 = cv.bitwise_and(img, th3)

    StackImages = stackImages(0.5,([[img,th1],[img,th2],[blur,th3]]))
    MaskedImages = stackImages(1,([result1,result2,result3]))
    cv.imshow("masked Image",MaskedImages)
    cv.imshow("Result Image",StackImages)

    if cv.waitKey(1) & 0xFF ==ord('q'):
        print("Settings:"+str([v_min,v_max,b]))
        break


    