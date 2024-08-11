#Dictionary 
#Write a python program to find the highest 2 values in a dictionary 
n={31:111,22:222,43:333,14:444,25:555}
S=sorted(n.values())
print("Given dictionary is:",n)
print("Highest two values of given dictionary are:",S[-1],S[-2])

#Why is the following code not giving correct output even when 25 is a members of a dictionary
dic1={'age':25,'name':'xyz','Salary':23450.5}
val=dic1['age']
if val in dic1:
    print("This is member of the dictionary")
else:
    print("This is not a member of the dictionary")


d1={5:[6,7,8],"a":(1,2,3)}
print(d1.keys())
print(d1.values())

#Write a program to enter the name of the employees and their salaries as input store then in the dictionary and print it line by line.
emp={"avik":25000,"ajay":27000}
print(emp)

#Write a program in which the dictionary is as follows:- 
n={0:'zero',1:'0',2:'two',3:'three'}
print(n)

#Updation a value 
dic={1:'a',2:'b',3:"c"}
dic[1]="p"
print(dic[1])

Emp=dict(name="John",Salary=10000,age=24)
print(Emp)

Emp=dict([['name','John'],['Salary',10000],['age',24]])
print(Emp)

Emp=dict((('name','John'),('Salary',10000),('age',24)))
print(Emp)

emp=dict(name="John",Salary=10000,age=24)
emp['dept']="Sales"
print(emp)

#Nested Dictionaries 
emp={"John":{"age":24,"Salary":10000},"Sunil":{"age":25,"Salary":11000}}
for key in emp:
    print("Employee Name:",key)
    print("Age:",str(emp[key]['age']))
    print("Salary:",str(emp[key]['Salary']))
