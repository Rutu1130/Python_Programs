
def Addition(Value1 , Value2):
    Result = 0
    Result = Value1 + Value2
    return Result    

def main():
    Value1 = int(input("Enter the First number :"))
    Value2 = int(input("Enter the Second number :"))
    Ans = 0
    Ans = Addition(Value1,Value2)
    print("Addition is :",Ans)

if __name__ == "__main__":
    main()