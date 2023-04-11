import cv2 as cv
import numpy as np
#https://docs.opencv.org/4.x/d7/d4d/tutorial_py_thresholding.html
#importing a Video
cap = cv.VideoCapture(1,cv.CAP_DSHOW)
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


cv.createTrackbar("Blur Val","TrackBars",0,100,empty)
cv.createTrackbar("Hue Min","TrackBars",0,179,empty)
#hue max
cv.createTrackbar("Hue Max","TrackBars",179,179,empty)
#sat min
cv.createTrackbar("Sat Min","TrackBars",0,255,empty)
#sat max
cv.createTrackbar("Sat Max","TrackBars",255,255,empty)
#val min
cv.createTrackbar("Val Min","TrackBars",0,255,empty)
#val max
cv.createTrackbar("Val Max","TrackBars",255,255,empty)

while True:
#While i can succesfully insert a image from video in img it will run
    succes, img = cap.read()
    img = img[183:515,335:809]
    img_result=img.copy()
    img= cv.cvtColor(img,cv.COLOR_BGR2GRAY) 


    b=cv.getTrackbarPos("Blur Val","TrackBars")
    #Gettrackbar positions


    #create image result based on mask
    



    # Otsu's thresholding
    ret1,th1 = cv.threshold(img,0,255,cv.THRESH_BINARY+cv.THRESH_OTSU)
    # Otsu's thresholding after Gaussian filtering
    blur = cv.GaussianBlur(img,(5,5),b)
    ret2,th2 = cv.threshold(blur,0,255,cv.THRESH_BINARY+cv.THRESH_OTSU)

    result1 = cv.bitwise_and(img_result,img_result,mask= th1)
    result2 = cv.bitwise_and(img_result,img_result,mask= th2)


    #result1 = cv.bitwise_and(img, th1)
    #result2 = cv.bitwise_and(img, th2)
    #result3 = cv.bitwise_and(img, th3)

    h_min=cv.getTrackbarPos("Hue Min","TrackBars")
    h_max=cv.getTrackbarPos("Hue Max","TrackBars")

    s_min=cv.getTrackbarPos("Sat Min","TrackBars")
    s_max=cv.getTrackbarPos("Sat Max","TrackBars")

    v_min=cv.getTrackbarPos("Val Min","TrackBars")
    v_max=cv.getTrackbarPos("Val Max","TrackBars")

    #creating mask
    lower = np.array([h_min,s_min,v_min])
    upper = np.array([h_max,s_max,v_max])
    img_blur=cv.GaussianBlur(result2,(5,5),b)
    imgHSV = cv.cvtColor(img_blur,cv.COLOR_BGR2HSV)    
    mask = cv.inRange(imgHSV,lower,upper)


    imgHSV = cv.bitwise_and(result2,result2,mask=mask)
    StackImages = stackImages(0.5,([[img,th1],[blur,th2]]))
    ResultImages = stackImages(1,([img_blur,imgHSV]))
    MaskedImages = stackImages(1,([result1,result2]))
    #cv.imshow("Masked Image",MaskedImages)
    cv.imshow("Otsu Image",StackImages)
    cv.imshow("Result Image",ResultImages)
    if cv.waitKey(1) & 0xFF ==ord('q'):
        print("Settings Upper:"+str([h_max,s_max,v_max]))
        print("Settings Lower:"+str([h_min,s_min,v_min]))
        print("Settings:"+str([b]))
        break


    