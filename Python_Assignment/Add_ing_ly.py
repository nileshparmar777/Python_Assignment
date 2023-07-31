addnam=input("enter a syntex: ")

if len(addnam)>=3:                         
    if addnam.endswith('ing'):              
        addnam  += 'ly'                    
    else:
        addnam += 'ing'
print(addnam)