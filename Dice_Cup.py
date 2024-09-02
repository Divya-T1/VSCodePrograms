#use maps instead
nums=input()
list1=nums.split(" ")
dice1=list(range(int(list1[0])))
for x in range(len(dice1)):
    dice1[x]=x+1
dice2=list(range(int(list1[1])))
for x in range(len(dice2)):
    dice2[x]=x+1
sums=list(range(dice1[len(dice1)-1]+dice2[len(dice2)-1]+1))
for x in range(len(sums)):
    sums[x]=0
for x in range(len(dice1)):
    for y in range(len(dice2)):
        sum=dice1[x]+dice2[y]
        sums[sum]=sums[sum]+1
max=sums[0]
for nums in range(len(sums)-1):
    if(sums[nums+1]>max):
        max=sums[nums+1]
for value in range(len(sums)):
    if(sums[value]==max):
        print(value)





  


