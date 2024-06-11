#Functions in Dictionary are:
#  1.copy() 
#  2.fromkeys()
#  3.update()


print("---------------------------copy() Function-----------------------------------")
Dict = {'Brand':'Maruti','Model':'Dzire','Year':2020 }
print(Dict)
X = Dict.copy()
print("Copy of Dictionary is :",X)


print("---------------------------Fromkeys() Function-----------------------------------")
X = ('Firstkey','Secondkey','Thirdkey')
y = 0
Dict = Dict.fromkeys(X,y)
print("Dictionary values are :",Dict)

print("---------------------------update() Function-----------------------------------")
Dict = {'Brand':'Maruti','Model':'Dzire','Year':2020 }
print(Dict)
Dict.update({'location':'Pune'})
print("Updated  Dictionary is :",Dict)
