num=int(input("enter your num: "))        
sum=0                                 
for i in range(1,num):
    sum=i+sum                         
    print(i,end="+")
print("=",sum)                           
print(sum)