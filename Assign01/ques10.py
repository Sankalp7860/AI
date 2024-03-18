list111=[]
def unique_elements(l):
    x=[]
    for a in l:
        if a not in x:
            x.append(a)
    return x
print(unique_elements([1, 2, 3, 3, 3, 3, 4, 5]))  
