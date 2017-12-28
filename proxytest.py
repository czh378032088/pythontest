
from bs4 import BeautifulSoup
import requests
import queue
from threading import *
import time
import os

runFlag = True

def GetIpThread(args):
    global runFlag
    header = {}
    header['User-Agent'] = 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:57.0) Gecko/20100101 Firefox/57.0'
    header['Accept'] = 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
    header['Accept-Language'] = 'en-US,en;q=0.5'
    header['Accept-Encoding'] = 'gzip, deflate'
    header['Connection'] = 'keep-alive'
    header['Upgrade-Insecure-Requests'] = '1'
    url = args
    i = 1
    while runFlag:
        #print('start ...' + url + str(i))
        try:
            ret = requests.get(url + str(i),headers = header,timeout = 10)
            bs = BeautifulSoup(ret.text,"lxml")
            trs = bs.findAll("tr")
            for tr in trs:
                tds = tr.findAll('td')
                if(len(tds)):
                    print(tds[1].contents[0],tds[2].contents[0])
        except expression as identifier:
            pass
        time.sleep(1)
        i += 1


def SetOsProxyTread(args):
    pass

if __name__ == '__main__':
    t1 = Thread(target=GetIpThread,args=('http://www.xicidaili.com/nn/',))
    t2 = Thread(target=SetOsProxyTread,args=('thread2',))
    t1.start()
    t2.start()
    while True:
        q = input()
        if(q.lower() == 'q'):
            break
    runFlag = False
    t1.join()
    t2.join()
