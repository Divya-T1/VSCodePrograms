#Lists

list1=[1,2,3,4] #list of ints
list2=["Hey", "Hi", "Hola", "Hello"] #list of strings
list3=[1,"Hey", True] #True and False must be capitalized to be recognized; list of various data types
list4=[[1,2,3], ["Hi", "Hey", "Hola"], [False, True, False]] #list of lists
list5=[list1, list2, list3]
print(list1)
print(list2)
print(list3)
print(list4)
print(list5)
print(len(list5))
print()

#Sets-elements are unique
set1={1,2,3,4,5}
print(set1)
print(type(set1))
print(len(set1))
set2={1,1,2,2}
len(set2) #displays 2 because only 2 unique elements are present
print(set2) #displays {1,2} because only 2 unique elements are present
print()

#order of elements doesn't matter for a set, but it does matter for a list
print([1,2] == [2,1])
print({1,2} == {2,1})
print({1,2,3} == {3,2,1,1,1})

#Tuples-like lists, but once established, can't be changed
tuple1=(1,2,3)
tuple2=(3,2,1)
#Order matters: 
print(tuple1==tuple2)
print(len(tuple1))
#tuple1.append(4) will cause an error

#Dictionaries
dictionary1={"apple":"A red fruit", 
"bear":"A scary animal"
}
print(dictionary1["apple"])

dictionary1={"apple":"A red fruit", 
"bear":"A scary animal",
"apple":"sometimes green"
}
 
#will print the most recent definition
print(dictionary1["apple"])


