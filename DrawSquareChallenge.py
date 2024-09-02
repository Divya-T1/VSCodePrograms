import os
import time
class DrawSquare:
    def __init__(size):
        size.dots=int(input())
        
    def drawSquare(size):
        x=1
        while(x<=size.dots):
            if(x==1 or x==size.dots):
                y=1
                while(y<=size.dots):
                    print(". ", end="")
                    time.sleep(0.1)
                    y+=1
            else:
                z=1
                while(z<=size.dots):
                    if(z==1 or z==size.dots):
                        print(".", end=" ")
                        time.sleep(0.1)
                    else:
                        print(" ",end=" ")
                    z+=1
            x+=1
            print()
    
start=DrawSquare()
start.drawSquare()



    
