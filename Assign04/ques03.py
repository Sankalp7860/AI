def is_prime(num):
    k=2
    while(k<num):
        if(num%k==0 ):
            return False
        k=k+1
    return True


def get_list():
    l = []
    n = int(input("Enter the number of elements in the list: "))
    print("Enter the elements of the list:")
    for i in range(n):
        x =int(input())
        l.append(x)
    return l

def count(l):
    odd = 0
    even = 0
    prime = 0
    non_prime = 0
    for num in l:
        if num % 2 == 0:
            even += 1
        else:
            odd += 1

        if is_prime(num):
            prime += 1
        else:
            non_prime += 1

    return odd, even, prime, non_prime



num_list = get_list()
odd, even, prime, non_prime = count(num_list)
print("Number of odd numbers:", odd)
print("Number of even numbers:", even)
print("Number of prime numbers:", prime)
print("Number of non-prime numbers:", non_prime)


