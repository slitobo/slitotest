from multiprocessing import Process,Pool
import time,os
def foo(i):
    time.sleep(1)
    print(i)

def bar(test):
    print('i am callback')


if __name__ == '__main__':
    pool = Pool()
    for i in range(10):
         pool.apply_async(func=foo,args=(i,),callback=bar)
    pool.close()
    pool.join()
    print('end...')
