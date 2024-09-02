from openai import OpenAI

#Tuples
tuple1=('disco', 10, 1.2)
print(type(tuple1))
print(tuple1[0])
tuple2=tuple1+("hard rock", 10)
print(tuple2[0:3])
print(len(tuple1))
#Tuples are immutable!!!!->So, they can't be changed
#So create a new tuple and set the changed tuple equal to the new one
tupleNum=(9,8,5,30,2,9,10,4,5)
tupleNumSorted=sorted(tupleNum)
tupleNest=(1,2,("pop","rock"),(3,4),("disco",(1,2)))
print(tupleNest[4][1][1])
for x in tuple1:
    print(x)


#List
#Like tuples but mutable
L=["Michael Jackson",10.1,1982]
L.extend(["pop", 10])
L.append("A")
del(L[0])
#can convert string to list
"hi, i am divya".split() #if no delimiter passed, splits based on spaces
"A,B,C,D".split(",") #using delimiter of ","

#Dictionaries
#Have keys that are indexes by label
#Keys are immutable
#Values are immutable/mutable/duplicates
songs={"Thriller": 1982, "Back in Black": 1980, "The Dark Side of the Moon": 1973, "The Bodyguard": 1992}
print(songs["Thriller"])
songs["Graduation"]="2007"
del(songs["Back in Black"])
print("Thriller" in songs)
print(songs.keys())
print(songs.values())

for x in songs:
    print(songs[x])
    print(x)

#Sets
#type of collection, so accept different types as input
#unordered
#only unique elements
setMain={"pop", "rock", "soul","hard rock","rock", "R&B", "rock", "disco"} 
print(setMain) #rock will be included only once despite repetition
#Can convert lists to sets with set() method
album_list=["Michael Jackson", "Thriller", "Thriller", 1982]
album_set=set(album_list)
print(album_set)
album_set.add("Back in Black")
album_set.remove("Thriller")
print(1982 in album_set)
#Can do math operations on sets
alb1={"AC/DC", "Back in Black", "Thriller"}
alb2={"AC/DC", "Back in Black", "The Dark Side of the Moon"}
alb3=alb1&alb2 #only info in both lists is within alb3, all other info isn't included
alb1.union(alb2) #also creates new set where alb1 and alb2 have the same data
print(alb3.issubset(alb1))


