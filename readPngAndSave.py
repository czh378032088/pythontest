import os
import cv2

dirname = 'F:\\code\\VS2015\\ABPUBM\\ABPUBM\\images\\'
allfilename = os.listdir(dirname)
print(allfilename)
savedir = os.path.join(dirname,'saveimage')
if not os.path.exists(savedir):
    os.makedirs(savedir)

for filename in allfilename:
    filepath = os.path.join(dirname,filename)
    extname = os.path.splitext(filepath)
    if extname[1] == '.png':
        print(filepath)
        img = cv2.imread(filepath,-1)
        print(img)
        #cv2.imshow(filepath,img)
        cv2.imwrite(os.path.join(savedir,filename),img)

