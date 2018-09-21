import numpy as np

def inputData():
    x = input('请输入9个数字：')
    num = [int(a) for a in x.split(',')]
    if(len(num) == 9):
        return num
    else:
        return None


if __name__ == '__main__':
    x = inputData()
    print(x)
