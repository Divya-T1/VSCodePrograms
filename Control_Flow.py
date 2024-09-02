a=True
b=True
c=True
if a:
    print("It is true!")
    print("Also print this")
    #Everything indented gets printed if true
    if b:
        print("Both are true")
        if c:
            print("All three are true")
else:
    print("It is false")
print("Always print this")

#Loop
a=[1,2,3,4,5]
for item in a:  #for each item (just a variable name) in the list a
    print(item)

#while loop
print()
a=0
while a<5:
    print(a)
    a=a+1
