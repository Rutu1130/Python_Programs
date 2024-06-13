import multiprocessing

def Square(No):
    return No * No

def main():
    Arr = [10,20,30,40]
    Result = []

    p = multiprocessing.Pool()
    Result = p.map(Square,Arr)
    p.close()
    p.join()

    print(Result)

if __name__ == "__main__":
    main()