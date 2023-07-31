add=input("Enter a string :")
a=add.find('not')                            
b=add.find('poor')
if a <b: 
    add1=add.replace(add[a:b+4],"good")       
    print(add1)
else:
    print(add)