
def Square(No):
    return No * No

def main():
    Arr = [10,20,30,40]
    Result = []

    for value in Arr:
        Ans = Square(value)
        Result.append(Ans)

    print(Result)

if __name__ == "__main__":
    main()