str1=input("hello world: ")
if len(str1)%4==0:
    print(''.join(str1[::-1]))
else:
    print(str1)