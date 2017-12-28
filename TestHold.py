
from threading import *
import time
import socket



def listen_thread(args):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    countNum = 0
    s.bind(('0.0.0.0',80))
    s.listen(5)
    s1 , addr = s.accept()
    for i in range(1000):
        data = s1.recv(1024)
        datastr = data.decode('utf-8')
        print(datastr)
        datastrlist=datastr.split('\n')
        if(countNum != int(datastrlist[0])):
            print(str(countNum) + '!=' + datastr)
        countNum = int(datastrlist[-1]) + 1

        #time.sleep(0.1)
    s1.close()
    s.close()

def connect_threead(args):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    time.sleep(2)
    s.connect(('127.0.0.1',8011))
    print('socket已经链接')
    for i in range(1000):
        s.send((str(i) + '\n').encode('utf-8'))
        time.sleep(0.001)
    s.close()

t1 = Thread(target=listen_thread,args=('thread1',))
t2 = Thread(target=connect_threead,args=('thread2',))
t1.start()
t2.start()
t1.join()
t2.join()



