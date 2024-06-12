
def Display(Name,Age,Marks =90):
    print("Name is: ",Name)
    print("Age is: ",Age)
    print("Marks are: ",Marks)

def main():
    print("Demonstration of Default argument")

    Display("Amit" ,  24  , 76 )

    Display( "Vivek" , 20 )

if __name__ == "__main__":
    main()