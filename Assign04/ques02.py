def count_occurrences(l, element):
    count = 0
    for item in l:
        if item == element:
            count += 1
    return count

def get_list():
    l = []
    n = int(input("Enter the number of elements in the list: "))
    print("Enter the elements of the list:")
    for i in range(n):
        x = int(input())
        l.append(x)
    return l

list1 = get_list()  
find = int(input("Enter the element to find frequency for: "))
result = count_occurrences(list1,find)
print(f"The element {find} found {result} times in the list.")


