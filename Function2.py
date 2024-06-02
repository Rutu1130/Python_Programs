def Addition(A,B):
    return A+B 

def Substraction(A,B):
    return A-B

def Marvellous(Value1 , Value2):
    Ans = Addition(Value1,Value2)
    print("Addition is: ",Ans)
    Ans = Substraction(Value1,Value2)
    print("Substraction is :",Ans)

def main():
    Marvellous(11,7)

if __name__ == "__main__":
    main()