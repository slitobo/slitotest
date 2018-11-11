
from multiprocessing import Process,Queue,JoinableQueue
import os,time,random



def producer(name,q):
    for i in range(10):
        time.sleep(random.randint(1,3))
        res = '%s%s' %(name,i)
        q.put(res)
        print('\033[31m%s 生产了 %s\033[0m'%(os.getpid(),res))
    q.join()
def consumer(q):
    while True:
        data = q.get()
        time.sleep(random.randint(1,3))
        print('\033[45m%s 吃了 %s\033[0m'%(os.getpid(),data))
        q.task_done()

if __name__ == '__main__':
    q = JoinableQueue()

    #生产者
    p1 = Process(target=producer,args=('馒头',q))
    # p2 = Process(target=producer,args=('包子',q))
    # p3 = Process(target=producer, args=('教团', q))

    #消费者
    c1 = Process(target=consumer,args=(q,))
    c2 = Process(target=consumer,args=(q,))
    c1.daemon = True
    c2.daemon = True

    mudel_list = [p1,c1,c2]
    for p in mudel_list:
        p.start()

    p1.join()
    # p2.join()
    # p3.join()
    print('主')

