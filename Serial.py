
def fun(No):
    Sum = 0

    for i in range(100000):
        Sum = Sum + (No * No)

    return Sum

def main():
    print("Demonstration of Serial Exucation using single Core")

    ret = fun(10)
    print(ret)

if __name__ == "__main__":
    main()