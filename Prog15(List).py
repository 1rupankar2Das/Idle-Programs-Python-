L=[1,2,3,4]
print(L)

L=[1,1.2,3.5,7,8,9]
print(L)

L=['a','b','c']
print(L)

L1=[2,2,[4,5],7,8]
print(L1)

L1=list("hello")
print(L1)

t=('a','b','c','d','e')
L1=list(t)
print(L1)

L1=list(input("Enter list elements: "))
print(L1)

L1=eval(input("Enter list elements: "))
print("list you entered",L1)

a=eval('5+8')
print(a)

y=eval("3*10")
print(y)

var1=eval(input("Enter value: "))
print(var1,type(var1))

var2=eval(input("Enter value: "))
print(var2,type(var2))

var3=eval(input("Enter value: "))
print(var3,type(var3))

L1=[1,2,3,4,5]
L1[0]='A'
print(L1)

L1=[1,2,3,4,5]
L1[-3]='W'
print(L1)

L1=[1,2,3,4,5,6]
for a in L1:
    print('value',a)

L=[1,2,3,4,5,6,7]
length=len(L)
for a in range(length):
    print("At index",a,"and",(a-length),"element:",L[a])

L1=[1,2,3]
L2=[1,2,3]
L3=[1,[2,3]]
a=L1==L2
print(a)
b=L1==L3
print(b)

