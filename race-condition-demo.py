from threading import Thread, Lock

x = 1 # Shared resource

# Initialize an instance of object Lock
lock_race = Lock()


def fibonaci(n):
    if n<=2 : return 1
    return fibonaci(n-1) + fibonaci(n-2)


def firstFibonaci():
    global x
    try:
        lock_race.acquire() # Graph a lock
        print("firstFibonaci resource is {} \n".format(x) )
        while x <= 10:
            print(fibonaci(x))
            x+=1
    finally:
        print("Done!")


def secondFibonaci():
    global x
    try:
        print("secondFibonaci resource is {} \n".format(x) )
        while x <= 10:
            print(fibonaci(x))
            x+=1
    finally:
        lock_race.release()
        print("Done!")


if __name__ == "__main__":
    Parallel_1 = Thread(target=firstFibonaci)
    Parallel_2 = Thread(target=secondFibonaci)
    Parallel_1.start()
    Parallel_2.start()
    Parallel_1.join()
    Parallel_2.join()