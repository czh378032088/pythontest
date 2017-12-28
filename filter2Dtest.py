
import datetime
import imutils
import time
import cv2
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
        kern = np.array([[-2,-2,-2],[-2,16,-2],[-2,-2,-2]])
        #kern = np.array([[-1,-1,-1],[-1,9,-1],[-1,-1,-1]])
        #kern = np.array([[0,-1,0],[-1,5,-1],[0,-1,0]])
        #kern = np.array([[0,-1,0],[-1,4,-1],[0,-1,0]])
        #kern = np.array([[0.5,0.5,0.5],[0.5,-4,0.5],[0.5,0.5,0.5]])
        #gray1 = cv2.Canny(gray,50,100)#cv2.filter2D(gray,-1,kern)
        gray1 = cv2.filter2D(gray,-1,kern)

        #显示当前帧并记录用户是否按下按键
        cv2.imshow("frame", frame)
        cv2.imshow("gray", gray)
        cv2.imshow("gray1", gray1)
        key = cv2.waitKey(1) & 0xFF
    
        # 如果q键被按下，跳出循环
        if key == ord("q"):
            break
    cv2.destroyAllWindows() 
