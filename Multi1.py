
import multiprocessing
import os

def Task1():
    print("Executing the first Task...")
    print("PID of ruuning process for task1  : ",os.getpid())


def Task2():
    print("Executing the first Task...")
    print("PID of ruuning process for task2  : ",os.getpid())

def main():
    print("Demonstration of multiprocessing")
    print("PID of ruuning process is : ",os.getpid())

    Task1()
    Task2()

if __name__ == "__main__":
    main()