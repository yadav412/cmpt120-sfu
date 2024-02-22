n1 = int(input("Enter your first positive integer: "))
n2 = int(input("Enter your second positive integer: "))

s = n1 + n2
def decimalToBinary(n):             #1st question
    lst1=[]
    lst2=[]
    if n1==n:
        alist=lst1
    else:
        alist=lst2

    while n>0:
        p=n%2
        n=(n-p)/2

        alist.append(int(p))
        
    for i in range(len(alist)//2):
        temp=alist[i]
        alist[i]=alist[len(alist)-1-i]
        alist [len(alist)-1-i]=temp

    return alist
    
lst1 = decimalToBinary(n1)
print("The binary representation of", n1, "is", lst1)

lst2 = decimalToBinary(n2)
print("The binary representation of", n2, "is", lst2)


def binaryAddition(lst1, lst2):       #2nd question
    if len(lst1) < len(lst2):
        lst1, lst2 = lst2, lst1
    carry = 0
    result = []
    for i in range(len(lst1) - 1, -1, -1):
        if i >= len(lst1) - len(lst2):
            digit_sum = lst1[i] + lst2[i - (len(lst1) - len(lst2))] + carry
        else:
            digit_sum = lst1[i] + carry
        result.append(digit_sum % 2)
        carry = digit_sum // 2
    if carry:
        result.append(carry)
    
    for i in range(len(result)//2):
        temp=result[i]
        result[i]=result[len(result)-1-i]
        result [len(result)-1-i]=temp
    return result

lst3 = binaryAddition(lst1, lst2)
print("The binary addition of", n1, "and", n2, "is", lst3)

def binaryToDecimal(lst3):                #3rd question
    number = 0
    for i in (lst3): #change to product of addition of binary list
        number = (2 * number) + i
    return(number)   

n3 = binaryToDecimal(lst3)
print("Converting the binary to decimal gives", n3)
 
if s == n3:
    print("Since", s, "==", n3, ", it seems we did good job.")
else:
    print("Since", s, "!=", n3, ", something went wrong.")

print("----------------------")

n = int(input("Enter a positive integer: "))
lst = decimalToBinary(n)
print("The binary representation of", n, "is", lst)

def reverse(n):
    
    for i in range(len(n)//2):
        temp =n[i]
        n[i]=n[len(n)-1-i]
        n [len(n)-1-i]=temp

    return(n) 

def is_palindromic(lst):
    left = 0
    right = len(lst) - 1
    while left < right:
        if lst[left] != lst[right]:
            return False
        left += 1
        right -= 1
    return True

    
def algo(lst):

    counter = 0
    while counter < 10:
        if is_palindromic(lst):
            return [lst, counter]
        lst_reverse = [0] * len(lst)
        for i in range(len(lst)):
            lst_reverse[i] = lst[-i - 1]
        lst = binaryAddition(lst, lst_reverse)
        counter += 1
    return [None, -1]


result = algo(lst)
print(lst, "became palindrome: ", result[0], "after ", result[1], "iterations")










    
    

      
