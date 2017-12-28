
import os
import cv2
from numpy import *
import matplotlib.pyplot as plt

if __name__ == '__main__':
    files = os.listdir('./image/facedata')
    print(files)
    faceMat = mat(zeros((len(files),48 * 48)))
    i = 0
    for filename in files:
        #print(filename)
        img = cv2.imread('./image/facedata/' + filename)
        img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        #print(type(img))
        faceMat[i,:] = img.flatten() / 255
        i += 1
    print(faceMat.shape)
    avgImg = mean(faceMat,axis = 0)
    #print(avgImg.shape)
    #avgImg = avgImg.reshape([48,48],order='C')
    difImg = faceMat - avgImg
    matImg = difImg * difImg.T / len(files)
    eigvals,eigVects = linalg.eig(matImg)
    print(difImg)
    print(avgImg)
    print(eigvals)

    eigVectsreal = difImg.T * eigVects
    eigVectsreal = eigVectsreal.T
    #eigVectsrealImg0 = eigVectsreal[0,:].reshape([48,48],order='C')

    #print(avgImg.shape)
    #print(avgImg)

    fig = plt.figure()
    for i in range(36):
        ax = fig.add_subplot(6,6,i + 1)
        ax.imshow(eigVectsreal[i,:].reshape([48,48],order='C'),cmap = plt.cm.gray)
    #ax = fig.add_subplot(471)


    
    fig.show()
    daijianyan = cv2.imread('./image/209.jpg')
    daijianyan = cv2.cvtColor(daijianyan,cv2.COLOR_BGR2GRAY).flatten() / 255
    daijianyan = eigVectsreal * (daijianyan - avgImg).T
    print(daijianyan)
    for i in range(len(files)):
        vect = eigVectsreal * difImg.T[:,i]
        diffvect = vect - daijianyan
        print((array(diffvect)**2).sum() / len(files),files[i])

    fig = plt.figure()
    avgImg = avgImg.reshape([48,48],order='C')
    ax = fig.add_subplot(1,1,1)
    ax.imshow(avgImg,cmap = plt.cm.gray)
    fig.show()
    #cv2.imshow("faceMat", faceMat)
    #cv2.imshow("avgImg", avgImg)
    #cv2.waitKey(1)
    while True:
        x = input('按任意按键退出')
        break
    cv2.destroyAllWindows() 