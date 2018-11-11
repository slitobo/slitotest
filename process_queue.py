from multiprocessing import Process,Queue

# 进程的内存空间隔离，需要把对象q传给子进程
def foo(q):
    q.put(123)
    q.put('hellp test')
    print('子进程是：',id(q))

if __name__ == '__main__':
    q = Queue()
    p = Process(target=foo,args=(q,))

    p.start()
    print('main process',id(q))
    data1 = q.get()
    data2 = q.get()
    print(data1)
    print(data2)
