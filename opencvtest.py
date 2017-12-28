
import argparse
import datetime
import imutils
import time
import cv2




'''
img = cv2.imread("./image/test.jpg")
cv2.namedWindow('Image')
cv2.imshow('Image',img)
cv2.waitKey(0)
'''

from imutils.video import FPS  
import argparse  
import imutils  
  
  
import fcntl  
  
import select  
import image  
  
import pygame.camera  
import pygame  
import numpy as np  
import time  
  
def surface_to_string(surface):  
    """convert pygame surface into string"""  
    return pygame.image.tostring(surface, 'RGB')  
  
def pygame_to_cvimage(surface):  
    """conver pygame surface into  cvimage"""  
  
    #cv_image = np.zeros(surface.get_size, np.uint8, 3)  
    image_string = surface_to_string(surface)  
    image_np = np.fromstring(image_string, np.uint8).reshape(480, 640, 3)  
    frame = cv2.cvtColor(image_np, cv2.COLOR_BGR2RGB)  
    return frame  

def on_trackbar(a):
    print(a)

    
if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument("-v","--video",help = "path to the video file")
    ap.add_argument("-a","--min_area",type = int,default = 500,help = "minimum area size")
    args = vars(ap.parse_args())

    if args.get("video",None) is None:
        camera = cv2.VideoCapture(0)
        #print(dir(camera))
        #print(camera)
        time.sleep(0.25)
    else:
        camera = cv2.VideoCapture(args["video"])
    firstFrame = None

    if not camera.isOpened():
        pygame.camera.init()  
        pygame.camera.list_cameras()  
        cam = pygame.camera.Camera("/dev/video0", [1024, 768])  
  
        cam.start()  
        time.sleep(1)  
    i = 0
    while True:
        if camera.isOpened():
            grabbed,frame = camera.read()
            if not grabbed:
                print("grabbend = ",grabbed,camera.isOpened())
                break
        else:
            image = cam.get_image()  
            frame = pygame_to_cvimage(image)  
        
        text = "Unoccupied"

        frame = imutils.resize(frame,width = 500)
        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        gray = cv2.GaussianBlur(gray,(21,21),0)
        '''
        cv2.imshow('frame',gray)
        c = cv2.waitKey(1) & 0xff
        if c == ord("q"):
            break
        '''
        if firstFrame is None:
            firstFrame = gray

        if i == 10:
            firstFrame = cv2.addWeighted(firstFrame,0.999,gray,0.001,0)
        else:
            firstFrame = cv2.addWeighted(firstFrame,0.9,gray,0.1,0)
            i += 1
        
        
        frameDelta = cv2.absdiff(firstFrame, gray)
        #firstFrame = gray
        thresh = cv2.threshold(frameDelta, 30, 255, cv2.THRESH_BINARY)[1]
        #thresh = cv2.Canny(frameDelta,20,100)
        thresh = cv2.dilate(thresh, None, iterations=2)
        #print(help(cv2.findContours))
        cnts = cv2.findContours(thresh, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        
        for c in cnts[1:]:
        # if the contour is too small, ignore it
            #print(cnts)
            
            if  c is None:
                continue
            
            if len(c) < 1 or len(c[0]) < 3:
                #print(type(c))
                #print(len(c))
                continue
            '''
            print(c)
            print(type(c))
            print(len(c))
            print(len(c[0]))
            print(len(c[0][0]))
            '''
            if len(c[0][0] ) == 4:
                continue
            #print(c)
            area = cv2.contourArea(c[0])
            #print(area)
            if area < 500:
                continue
    
            # compute the bounding box for the contour, draw it on the frame,
            # and update the text
            # 计算轮廓的边界框，在当前帧中画出该框
            (x, y, w, h) = cv2.boundingRect(c[0])
            print(x, y, w, h)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
            text = "Occupied"
        
        cv2.putText(frame, "Room Status: {}".format(text), (10, 20),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
        cv2.putText(frame, datetime.datetime.now().strftime("%A %d %B %Y %I:%M:%S%p"),(10, frame.shape[0] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.35, (0, 0, 255), 1)
    
        #显示当前帧并记录用户是否按下按键
        cv2.imshow("Security Feed", frame)
        cv2.createTrackbar("test","Security Feed",1,100,on_trackbar)
        cv2.imshow("Thresh", thresh)
        cv2.imshow("Frame Delta", frameDelta)
        key = cv2.waitKey(1) & 0xFF
    
        # 如果q键被按下，跳出循环
        if key == ord("q"):
            break
    cv2.destroyAllWindows() 
