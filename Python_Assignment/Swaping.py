a=56
b=67
 
temp=a                                  
a=b
b=temp
print("with swapping: ")
print("a" ,a)
print("b" ,b)

a=a+b                                   
b=a-b
a=a-b
print("without swapping: ")
print("a",  a)
print("b",  b)