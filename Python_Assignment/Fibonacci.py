no=int(input("enter fibonacci series: "))
#print(f"fibonacci num is :{a}")
a,b=0,1
x=0
if no <=0:
    print('number in greater than 0')
else:
    for i in range(0,no):
        print(x,end=" ")
        a=b
        b=x
        x=a+b