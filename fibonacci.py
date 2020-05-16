x=0
y=1
z=int(input("enter how many numbers of fibonacci series you want :"))
if(z<=0):
    print('invalid number')
COUNT = 0
while COUNT< z :
    print(x)
    nth = x+y
    x = y
    y = nth
    COUNT+=1

