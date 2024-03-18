# Q1
a=2
print(type(a))
b=6
c=2
print(b+c)
print(b-c)
print(b*c)
print(b/c)
str="hello world"
print(len(str))
str1="22"
print(int(str1),"->",type(str1))

#Q2
print("Before Swapping:-")
print("Value of b is :",b,"\nValue of c is: ",c)
b,c=c,b
print("After Swapping:-")
print("Value of b is :",b,"\nValue of c is: ",c)

# Q3
str2 ="I am a computer science student"
print(str2[0])
print(str2[2:5])
print(str2[2:])

# Q4
list=[10,20,30,50,60,70]
print(list)
print(list[2:])
list.insert(int((len(list)/2)),40)
print(list)
list.append(100)
print(list)
print(list[2:5])

# Q5
list2=[80,90]
list3=list+list2
list4=[]
print(list3)
for i in list3:
    if(i%2==0):
        list4.append(i)
print(list4)

# Q6
list5=['hello',False,2]
print(list5)
list6=["programming"]*3
print(list6)
print(list5+list6)

# Q7
person = { 'first_name': 'John','last_name': 'Doe','age': 25,
'favorite_colors': ['blue', 'green'],'active': True}
print(person)
list11=[]
list12=[]
for key in person:
    list11.append(key)
for value in person.values():
    list12.append(value)
print(list11)
print(list12)
print(list12[1])

# Q8
inp=int(input("Enter the Number: "))
if(inp%2==0):
    print("even Number")
else:
    print("odd Number")

# Q9
for i in list:
    print(i)

# Q10
list111=[]
def unique_elements(l):
    x=[]
    for a in l:
        if a not in x:
            x.append(a)
    return x
print(unique_elements([1, 2, 3, 3, 3, 3, 4, 5]))  

    