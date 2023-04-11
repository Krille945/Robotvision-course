import cv2 
import numpy as np

#importing a Video
cap = cv2.VideoCapture(1,cv2.CAP_DSHOW)
#define width
cap.set(3,1000) #width of webcam
cap.set(4,1000) # height
#to define Brightness not need but nice to know
#cap.set(10,100)

def getCombinedDis (e,e1,f,f1,g,g1,h,h1):
    dis = int(np.sqrt((e-f)**2+(e1-f1)**2)+np.sqrt((e-g)**2+(e1-g1)**2)+np.sqrt((e-h)**2+(e1-h1)**2))
    return dis

def transLengthToPoint (len1,len2,len3,len4,e,e1,f,f1,g,g1,h,h1):
    list=([len1,len2,len3,len4])
    list1 =np.array([[e,e1],[f,f1],[g,g1],[h,h1]])
    list2 =np.array([[0,0],[0,0],[0,0],[0,0]])
    i=0
    tt=3
    while i <= tt:
        p=list.index(max(list))
        list2[p,0]=list1[p,0]
        list2[p,1]=list1[p,1]
        list[p]=0
        list[p]=0


        i = i+1
    
    return list2

#OBJECT GENDKENDELSE#
def getContours(img):
    contours,hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        #finds area
        area = cv2.contourArea(cnt)
        
        #check for min area to remove noice
        if area>500:
            cv2.drawContours(imgContour,cnt,-1,(255,0,0),3)
            #length around 
            peri = cv2.arcLength(cnt,True)


            #finds the cornor points
            #true means we expect it to be closed
            approx = cv2.approxPolyDP(cnt,0.02*peri,True)


            #create object corners and creat bounding box
            objCor = len(approx)
            x,y,w,h = cv2.boundingRect(approx)

            #(x+(w//2),y+(h//2) finds center
            #draw bounding box
            cv2.rectangle(imgContour,(x,y),(x+w,y+h),(0,255,0),2)

###FARVE SORTERING###
#empty function for creating trackbars
def empty(a):
    pass

#To determine the optimal color range we wil intruduce track bars
#create window
cv2.namedWindow("TrackBars")
#resize window
cv2.resizeWindow("TrackBars",640,240)

#create first track bar hue min
#(name,whichwindom , minval, maxval,funktion)
cv2.createTrackbar("Hue Min","TrackBars",0,179,empty)

#hue max
cv2.createTrackbar("Hue Max","TrackBars",179,179,empty)
#sat min
cv2.createTrackbar("Sat Min","TrackBars",0,255,empty)
#sat max
cv2.createTrackbar("Sat Max","TrackBars",255,255,empty)
#val min
cv2.createTrackbar("Val Min","TrackBars",0,255,empty)
#val max
cv2.createTrackbar("Val Max","TrackBars",255,255,empty)

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
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (0,0), None, scale, scale)
                else:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1],imgArray[0][0].shape[0]), None, scale, scale)
                if len(imgArray[x][y]) == 2: imgArray[x][y]= cv2.cvtColor(imgArray[x][y], cv2.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank]*rows
        hor_con = [imageBlank]*rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv2.resize(imgArray[x], (0,0), None, scale, scale)
            else:
                imgArray[x]= cv2.resize(imgArray[x], (imgArray[0].shape[1],imgArray[0].shape[0]), None, scale, scale)
            if len(imgArray[x]) == 2: imgArray[x]= cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)   
        hor = np.hstack(imgArray)
        ver = hor 
    return ver

while True:
    #While i can succesfully insert a image from video in img it will run
    succes, img = cap.read()
    #cv2.imshow("Video",img)
    img = img[183:515,335:809]

    imgContour = img.copy()

    ###FARVE SORTERING###

    #CONVERT TO HSV
    imgHSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)    
    #imgHSV[:,:,2] += 200
    #img=cv2.cvtColor(imgHSV,cv2.COLOR_HSV2BGR) 
    #Gettrackbar positions
    h_min=cv2.getTrackbarPos("Hue Min","TrackBars")
    h_max=cv2.getTrackbarPos("Hue Max","TrackBars")

    s_min=cv2.getTrackbarPos("Sat Min","TrackBars")
    s_max=cv2.getTrackbarPos("Sat Max","TrackBars")

    v_min=cv2.getTrackbarPos("Val Min","TrackBars")
    v_max=cv2.getTrackbarPos("Val Max","TrackBars")

    #creating mask
    lower = np.array([h_min,s_min,v_min])
    upper = np.array([h_max,s_max,v_max])

    mask = cv2.inRange(imgHSV,lower,upper)

    #create image result based on mask
    imgResult = cv2.bitwise_and(img,img,mask=mask)

    ###OBJECT GENKENDELSE###
    imgGray = cv2.cvtColor(imgResult,cv2.COLOR_BGR2GRAY)

    imgBlur = cv2.GaussianBlur(imgGray,(7,7),1)

    imgCanny = cv2.Canny(imgBlur,70,70)

    getContours(imgCanny)
    cv2.circle(imgContour,(800,430), radius=5, color=(0, 0, 255), thickness=-1)
    cv2.circle(imgContour,(390,430), radius=5, color=(0, 0, 255), thickness=-1)
    #[imgCanny, imgResult]
    StackImages = stackImages(0.5,([imgContour, imgResult]))
    cv2.imshow("Result Image",StackImages)
    #cv2.imshow("Contour Image",imgContour)
    #cv2.imshow("Grayscale Image",imgGray)
    cv2.imshow("Canny Image",imgCanny)
    #cv2.imshow("Mask Image",imgResult)

    #ads delay and waits for the keypress q
    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break
