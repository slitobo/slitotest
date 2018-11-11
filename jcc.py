from multiprocessing import Process,Lock
def foo(l,i):
    l.acquire()
    print('hello %d'%i)
    l.release()
if __name__ == '__main__':
    lock = Lock()
    for i in range(10):
        p = Process(target=foo,args=(lock,i))
        p.start()
