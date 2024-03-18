import numpy as np
print("\n\nQ4\n")
count=0
file3=open("AI/text.txt",'r')
for each in file3:
    if(each[0]!='T'):
        count=count+1
        print(each)
print(count)
