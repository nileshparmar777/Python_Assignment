num=int(input("enter fibonacci series: "))

a,b=0,1
x=0
if num <=0:
    print('number in greater than 0')
else:
    for i in range(0,num):
        print(x,end=" ")
        a=b
        b=x
        x=a+b