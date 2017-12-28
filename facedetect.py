
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
    
        nowTime = time.time()
        i = 200
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

        frame = imutils.resize(frame,width = 1000)
        
        face_patterns = cv2.CascadeClassifier('./data/haarcascade_frontalface_default.xml')
        #frame = cv2.imread('./image/face.jpg')
        faces = face_patterns.detectMultiScale(frame,scaleFactor=1.1,minNeighbors=5,minSize=(100, 100))
        
        
        if(time.time()- nowTime > 1):
            nowTime = time.time()
            for (x, y, w, h) in faces:
                subFrame = frame[y : y + h , x : x + w]
                subFrame = imutils.resize(subFrame,width = 48)
                cv2.imwrite('./image/' + str(i) + '.jpg',subFrame)
                i = i + 1
        

        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
            

        #显示当前帧并记录用户是否按下按键
        frame = imutils.resize(frame,width = 1024)
        cv2.imshow("frame", frame)
        key = cv2.waitKey(1) & 0xFF
        if key == ord("q"):
            break
        #x = input('按任意按键退出')
        #break
        # 如果q键被按下，跳出循环
        
    cv2.destroyAllWindows() 
