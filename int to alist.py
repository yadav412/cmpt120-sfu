n= int(input("value"))

def tolist(n):
    if n==0:
        return(0)
    
    lst=[]
    while n>0: 
        lst.append(n%10)
        n=n//10 
    lst=lst[::-1]

    return lst

print(tolist(n))
