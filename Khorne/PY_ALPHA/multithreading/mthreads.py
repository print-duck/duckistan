import threading
import time


def func1():
    for i in range(10):
        print('loop 1',i)
        time.sleep(0.5)
def func2():
    for i in range(15):
        print('loop 2',i)
        time.sleep(0.5)

t1=threading.Thread(target=func1)

t2=threading.Thread(target=func2)

#start,join :: start,stop
t1.start()
t2.start()
t1.join()
t2.join()
