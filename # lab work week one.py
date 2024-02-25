# lab work week one 

#1)
'''''
height= int(input('height'))
base= int(input("base"))

area= 0.5*base*height
print(area,"area of triangle")
'''''

#2)
'''''
feet= int(input("feet value"))
inches= int(input("length in inches value"))

cm1= feet*30.48
cm2= inches*2.54 

cm3=cm1 +cm2 

metres= int(cm1+cm2)//100
cm4= (cm1+cm2)%100

print((metres,"m",cm4,"cm" ))
'''

#3
'''''

n=int(input("degrees in C"))

f= (n *9/5) + 32 
print(f, "american nonsense ")

'''
#4 
'''''
raduis= int(input("raduis in cm"))

volume= 4*3.14**3/3
print(volume, "cm 3")
'''

#5
'''''
a=int(input("a"))
b= int (input("b"))
c= int (input("c"))

dis=b*2-4*a*c
print(b,"*2-4*",a,"*",c) 
print(dis, "discriminant")

'''

#6
''''
principle=int(input("principle investment"))
interest_rate= int(input("interest"))
numberofyears= int(input("years"))

simple= principle*(interest_rate/100)*numberofyears
total= principle+simple 

print(simple,"interest")
print(total,"total")

'''

#7 
''''
amt= float(input("Currency"))

toonies= amt//2
loonies=(amt-(toonies*2))//1
q=(amt-(toonies*2)-loonies)//0.25
d=(amt-(toonies*2)-loonies-(q*0.25))//0.10
n=(amt-(toonies*2)-loonies-(q*0.25)-(d*0.10))//0.05
p=(amt-(toonies*2)-loonies-(q*0.25)-(d*0.10)-(n*0.05))//0.01

print(toonies)
print(loonies)
print(q)
print(int(d))
print (int(n))
print(int(p))

'''


#8
n=int(input("value"))

while n in range(0,255): 
    p= n%2
    n=n//2
    


 