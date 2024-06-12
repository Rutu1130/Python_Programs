
def Display(Name,Age,Marks):
    print("Name is: ",Name)
    print("Age is: ",Age)
    print("Marks are: ",Marks)

def main():
    print("Demonstration of Keywoard argument")

    Display(Name="Amit" , Age = 24 , Marks = 89 )

    Display(Marks = 75 ,Name="Vivek" , Age = 20  )

if __name__ == "__main__":
    main()