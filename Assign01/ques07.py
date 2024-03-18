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
