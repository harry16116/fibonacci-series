x=0
y=1
z=int(input("enter how many numbers of fibonacci series you want :"))
COUNT = 0
while COUNT< z :
    print(x)
    nth = x+y
    x = y
    y = nth
    COUNT+=1

