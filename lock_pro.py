from multiprocessing import Process,JoinableQueue,Lock
from threading import Thread
from queue import Queue
import os,time,random

def foo(q):
    for i in range(5):
        time.sleep(random.randint(1,3))
        ret = '%s%s'%(os.getpid(),i)
        q.put(ret)
        print('%s 生产了 %s'%(os.getpid(),i))
   #     q.task_done()
    q.join()
    
def bar(q,name):
    while True:
        data = q.get()
      #  if data is None:
      #      print('get None')
      #      break
        print('%s 得到的数据是:%s'%(name,data))
       # time.sleep(random.randint(1,3))
        #print(q.qsize())
        q.task_done()
       # q.join()

if __name__ == '__main__':
    #q = JoinableQueue()
    q = Queue()
    p1 = Thread(target=foo,args=(q,))
    p4 = Thread(target=foo,args=(q,))
    p2 = Thread(target=bar,args=(q,'slito'))
    p3 = Thread(target=bar,args=(q,'bo'))
    p_list = [p1,p2,p3,p4]
    p2.daemon = True
    p3.daemon = True
    for p in p_list:
        p.start()
    p1.join()
    p4.join()
    #q.put(None)
    #q.put(None)
    print('end')
