
def Add(*No):
    Ans = 0
    for i in No :
        Ans = Ans + i

    return Ans

def main():

    print("Demonstration of Variable arguments")

    Ret = Add(10,20,30,)
    print("Addition is: ",Ret)

    Ret = Add(11,21,51,101,111)
    print("Addition is: ",Ret)

    Ret = Add(10,20,)
    print("Addition is: ",Ret)

if __name__ == "__main__":
    main()