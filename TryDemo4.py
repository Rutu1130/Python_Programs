# Exception Handling
def main():
    print("Enter the First number :")
    No1 = int(input())

    print("Enter the First number : ")
    No2 = int(input())

    Ans = 0
    try :
        Ans  = No1 / No2

    except Exception as zobj:
        print("Exception  occured as", zobj)
        return

    print("Division is : ", Ans)

if __name__ == "__main__":
    main()