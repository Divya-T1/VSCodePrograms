# Enter your code here. Read input from STDIN. Print output to STDOUT

run_num=int(input())
count=0
words=list()
nums=list()
tempNum=0
while run_num>0:
    words.append(input())
    run_num-=1
for x in range(0,len(words)):
    if(x<len(words)):
        count+=1
        count2=1
        for y in range(x+1,len(words)):
            if(y<len(words)):
                if words[x] == words[y]:
                    words.pop(y)
                    y-=1
                    count2+=1
        nums.append(count2)
print(count)
for x in nums:
    print(x, end=" ")
            