

def Display(*Values):
    
    for i in range (len(Values)):
        print(Values[i])

def main():

    print("Demonstration of Variable arguments")
    Display(10,20,30,40,50)
    Display(11,21,51)

if __name__ == "__main__":
    main()