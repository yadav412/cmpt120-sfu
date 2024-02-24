lst=[1,1,2,2,2]

def revlist(lst):
    
    for i in range(len(lst)//2):
        temp=lst[i]
        lst[i]=lst[len(lst)-1-i]
        lst[len(lst)-1-i]=temp

    print(lst)

revlist(lst)

    