
def fun(No):
    Sum = 0

    for i in range(100000):
        Sum = Sum + (No * No)

    return Sum

def main():
    print("Demonstration of Serial Exucation using single Core")

    Result = []

    for No in range(100000):
        Result.append(fun(No))

if __name__ == "__main__":
    main()