# to gather input
name=input("What is your name? ") 
#OR: name=input("What is your name? ").strip().title()

#using concatenation to utilize input
print("Hello, " + name)

#using comma as separator to print same thing as above
print("Hello,", name) #when separating the objects to be printed with a comma, space is automatically added since sep=" "

#using f print which treats the contents of the print as a special string
#this ensures the name in curly braces refers to the variable rather than printing the word name itself
print(f"Hello, {name}") 

#using other print parameters for same output
print("Hello, ", end="") #end defines what occurs after the print statement execute; the default is "/n" which tells it to skip a line
print(name)

#using sep parameter which decides what separates each object in the print function
print("Hello", name, sep=", ") # default of sep=" "

#method to get rid of all white spaces
name=name.strip()
print(f"Hello, {name}")

#method to capitalize using titleCase
name=name.title()
print(name)

#method to capitalize only first letter
name=name.capitalize()
print(f"Hello, {name}")

#getting rid of white space and titleCase
name=name.strip().title()
print(name)

#Split user's name into first and last name
first, last = name.split(" ") #Assigns first input to first and last input to last
print(f"Hello {first}")

