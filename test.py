import threading
import time
def add():
    sum = 1
    for i in range(1,200000):
        sum *= i
    print('和是:%d'%sum)
    print('和结束时间:%s'%(time.time()-start_time))


def mul():
    sum1 = 1
    for i in range(1,100000):
        sum1 *= i
    print('集是:%d' % sum1)
    print('ji结束时间:%s'% (time.time() - start_time))

threads = []

t1 = threading.Thread(target=add)
t2 = threading.Thread(target=mul)

threads.append(t1)
threads.append(t2)

start_time = time.time()

if __name__ == '__main__':
    # t1.setDaemon(True)

    #for t in threads:
    #    t.start()
    #for t in threads:
    #    t.join()
    add()
    mul()
