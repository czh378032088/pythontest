
MOVECOUNT = 0

def HanNuo(a,b,c,n):
    global MOVECOUNT
    if n == 1:
        print(a + '->' + b + ',' + str(MOVECOUNT))
        MOVECOUNT += 1
    else:
        HanNuo(a,c,b,n - 1)
        print(a + '->' + b + ',' + str(MOVECOUNT))
        MOVECOUNT += 1
        HanNuo(c,b,a,n - 1)

if __name__ == "__main__":
    #global MOVECOUNT
    num = input('请输入数字：')
    HanNuo('A','B','C',int(num))
    print(MOVECOUNT)
