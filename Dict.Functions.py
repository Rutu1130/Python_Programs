#Functions in Dictionary are:
#  1.len() 
#  2.pop()
#  3.popitem()
#  4.del()
#  5.clear()

print("---------------------------Len() Functio-----------------------------------")
Dict = {'Brand':'Maruti','Model':'Dzire','Year':2020 }
print(Dict)
X = len(Dict)
print("Length of Dictionary is :",X)

print("---------------------------pop() Function -----------------------------------")
Dict = {'Brand':'Maruti','Model':'Dzire','Year':2020 }
print(Dict)
Dict.pop('Model')
print("Dictionary after removing 'Model ': ", Dict)

print("---------------------------popitem() Function-----------------------------------")
Dict = {'Brand':'Maruti','Model':'Dzire','Year':2020 }
print(Dict)
Dict.popitem()
print("Dictionary after removing last element : ", Dict)


print("---------------------------Del() Function-----------------------------------")
Dict = {'Brand':'Maruti','Model':'Dzire','Year':2020 }
print(Dict)
del Dict['Year']
print("Dictionaryafter use Del function :",Dict)


print("---------------------------Del() Function-----------------------------------")
Dict = {'Brand':'Maruti','Model':'Dzire','Year':2020 }
print(Dict)
Dict.clear()
print("Dictionaryafter use Del function :",Dict)