from threading import Thread

x = 1 # Shared resource


def fibonaci(n):
    if n<=2 : return 1
    return fibonaci(n-1) + fibonaci(n-2)


def firstFibonaci():
    global x
    print("firstFibonaci resource is {} \n".format(x) )
    while x <= 10:
        print(fibonaci(x))
        x+=1


def secondFibonaci():
    global x
    print("secondFibonaci resource is {} \n".format(x) )
    while x <= 10:
        print(fibonaci(x))
        x+=1


if __name__ == "__main__":
    Parallel_1 = Thread(target=firstFibonaci)
    Parallel_2 = Thread(target=secondFibonaci)
    Parallel_1.start()
    Parallel_2.start()
    Parallel_1.join()
    Parallel_2.join()