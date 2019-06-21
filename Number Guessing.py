def arrange(l):
    p=[[],[],[]]
    k=0
    for i in range(3):
        for j in range(7):
            if(k%3==0):
                k=0
            p[k].append(l[i][j])
            k+=1
    return p
def middlerow(l,n):
    if n==0:
        return arrange([l[1],l[0],l[2]])
    elif n==1:
        return arrange(l)
    else:
        return arrange([l[0],l[2],l[1]])
def print1(l):
    i=0
    for row in l:
        print(i+1," row :",end="")
        for val in row:
            print(val,end=" ")
        print()
        i+=1
        time.sleep(1)
    print("Enther the row number with your element:")
    n=int(input())
    return n
import time
import random
time.sleep(1)
print("Get ready to cheat the computer if you are a GEM!!")
time.sleep(1)
print("choose the number from the below list of numbers:")
l=list(range(1,22))
random.shuffle(l)
time.sleep(1)
print(l)
time.sleep(5)
print("Dont forget remember that:)")
time.sleep(2)
k=[]
p=0
a=[]
for i in l:
    a.append(i)
    p+=1
    if(p%7==0):
        k.append(a)
        a=[]
print("We display three rows and you have to select a row with your choosen element")
time.sleep(4)
print("it will be repeated for 3 times :)")
time.sleep(1)
print("you have select the row with same choosen element...")
time.sleep(1)
print("get ready!! Man")
time.sleep(1)
p=0
while(p!=3):
    try:
        n=print1(k)
        if(n<1 or n>3):
            raise ValueError
        p+=1
        k=middlerow(k,n-1)
    except ValueError:
        print("you bitch enter correctly")
        print("choose the Number and and select the row where the number is")
print("i got it")
time.sleep(2)
print("Better luck next time to cheat me You dump :(")
time.sleep(3)
print("Your answer is : ",k[1][3])

