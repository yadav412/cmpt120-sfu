n= int(input("value"))

def dectobin(n):
    bin=[]
    while n>0:

        p=n%2
        n=n//2 
        bin.append(p)
    print(bin[::-1])

dectobin(n)