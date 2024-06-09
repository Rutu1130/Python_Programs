
def main():
    print("Enter the number of elements that you want to store : ")
    Length = int(input())

    Arr = list()

    print("Enter the Elements : ")
    for i in range(Length):
        Value = int(input())
        Arr.append(Value)

    print("Elements from the list are : ")
    for i in range(len(Arr)):
        print(Arr[i])

if __name__ == "__main__":
    main()
