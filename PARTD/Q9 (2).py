import threading

class FibonacciThread(threading.Thread):
    def run(self):
        fib_0, fib_1 = 0, 1
        print(f"Fibonacci Series: {fib_0}", end=", ")
        while fib_1 <= 10000:
            print(f"{fib_1}", end=", ")
            fib_0, fib_1 = fib_1, fib_0 + fib_1

class SquareThread(threading.Thread):
    def run(self):
        print("\nSquares:")
        for i in range(1, 10001):
            print(f"{i}^2 = {i**2}")

class CubeThread(threading.Thread):
    def run(self):
        print("\nCubes:")
        for i in range(1, 10001):
            print(f"{i}^3 = {i**3}")

# Create and start the threads
fib_thread = FibonacciThread()
square_thread = SquareThread()
cube_thread = CubeThread()

fib_thread.start()
square_thread.start()
cube_thread.start()

# Wait for all threads to finish
fib_thread.join()
square_thread.join()
cube_thread.join()




