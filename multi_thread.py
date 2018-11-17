import threading

#线程A
class A(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    def run(self):
        for i in range(0, 10):
            print("Thread A")

#线程B
class B(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    def run(self):
        for i in range(0, 10):
            print("Thread B")

#开启线程
t1=A()
t1.start()
t2=B()
t2.start()
