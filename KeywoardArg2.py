
def Batches(Name, Fees):
    print("Name is: ",Name)
    print("Fees are: ",Fees)

def main():
    print("Demonstration of Keywoard argument")

    Batches(Fees=7000 , Name = "Sagar" )

    Batches(Name="Kartik" , Fees = 10000  )

if __name__ == "__main__":
    main()