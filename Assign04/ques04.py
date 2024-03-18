def find_max_between_lists(l1, l2):
    if len(l1) != len(l2):
        print("Error: Lists must have the same size.")
        return None
    
    l3 = []
    for num1, num2 in zip(l1, l2):
        l3.append(max(num1, num2))
    
    return l3

def get_lists():
    l1,l2 = [],[]
    n = int(input("Enter the number of elements in the list: "))
    print("Enter the elements of the list1:")
    for i in range(n):
        x =int(input())
        l1.append(x)
    print("Enter the elements of the list2:")
    for i in range(n):
        x =int(input())
        l2.append(x)
    return l1,l2

l1,l2=get_lists()
l3 = find_max_between_lists(l1, l2)
print("Maximum elements between corresponding elements of the two lists:",l3)

