
class MyDes():
    def __init__(self,c,d):
        self.c = c
        self.d = d 
        print("__init__")
    def __call__(self,fn):
        def wap(x,y):
            print(self.c)
            fn(x,y)
            print(self.d)
        return wap

'''
def MyDes(c,d):
    def a(fn):
        def e(a,b):
            print(c)
            fn(a,b)
            print(d)
        return e
    return a
'''
@MyDes("c","d")
def MyTest(x,y):
    print(x)
    print("MyTest")
    print(y)



MyTest("x","y")
