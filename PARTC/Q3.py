import threading

class FThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    
    def run(self):
        n1, n2 = 0, 1
        while n1 <= 10000:
            print(n1)
            n1, n2 = n2, n1 + n2

class SThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    
    def run(self):
        for i in range(10001):
            print(i ** 2)

class CThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    
    def run(self):
        for i in range(10001):
            print(i ** 3)

#  instances
fib_thread = FThread()
square_thread = SThread()
cube_thread = CThread()

# threads
fib_thread.start()
square_thread.start()
cube_thread.start()


fib_thread.join()
square_thread.join()
cube_thread.join()
