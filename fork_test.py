from multiprocessing import Process
import time
start_time = time.time()
def foo():
    sum = 1
    for i in range(1,100000):
        sum *= i
    #print('第一个机是: %d'%sum)
    print('第一个end_time:%d'%(time.time()-start_time))

def bar():
    sum = 1
    for i in range(1, 100000):
        sum *= i
    #print('第二个机是: %d' %sum)
    print('第二个end_time:%d' % (time.time() - start_time))

if __name__ == '__main__':

    print('start time %s'%time.ctime())
    p1=Process(target=foo)
    p2=Process(target=bar)


    p1.start()
    p2.start()

    p1.join()
    p2.join()
    # foo()
    # bar()
    print("计算完成")
    
