class Dog:
     def __init__(self, name): #is a required function that is first executed when the class is called
        self.x=name #like the constructor
        self.legs=4 #the parameter self alone doesn't count

     def speak(self):
        print(self.x+" says: Bark")

anotherDog=Dog("Fluffy")

anotherDog.speak()
