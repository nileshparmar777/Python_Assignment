str1=("Tops")           
a= {}                               
for i in str1:
  if i in a:                        
    a[i]+=1                         
  else:
    a[i]=1                          
print(a)  