#
import Marvellous
def main():
    Value1 = int(input("Enter the First number :"))
    Value2 = int(input("Enter the Second number :"))
    
    Result = 0
    Result = Marvellous.Addition(Value1,Value2)
    print("Addition is :",Result)

    Result = Marvellous.Substraction(Value1,Value2)
    print("Substraction is :",Result)

    Result = Marvellous.Multiplication(Value1,Value2)
    print("Multiplication  is :",Result)

if __name__ == "__main__":
    main()