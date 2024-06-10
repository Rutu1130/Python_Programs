
Batches = {"PPA" : 18500, "Python" : 18700, "LB" : 19000, "Angular" : 19200, "LSP" : 18200, "C#" : 21000}

print(Batches)

print(type(Batches))

print(len(Batches))

print(Batches["Python"])

print("Batches in the Above Dictionay: ")
for value in Batches:
    print(value)

print("Values in the batches :")
for value in Batches:
    print(Batches[value])
print("-------------------------------")
for value in Batches:
    print(value, Batches[value])