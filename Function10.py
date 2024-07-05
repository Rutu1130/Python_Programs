
def Add(A, B):
    return A + B

def Sub(A, B):
    return A - B

# Function accept multilpe parameter and  call another function from it

def Marvellous(Value1,Value2):
    Ans = Add(Value1, Value2)
    print("Addition is : ",Ans)
    Ans = Sub(Value1, Value2)
    print(" Substraction is : ",Ans)


def main():

    Marvellous(11,6)
    
if __name__ == "__main__":
    main()