def tail(n):
    print("Calling tail with n=" + str(n))
    if n==0:
        return
    print(n)
    tail(n-1)

# tail(5)

def head(n):
    print("Calling head with n=" + str(n))
    if n==0:
        return
    head(n-1)
    print(n)

# head(5)

def factorial_head(n):

    # this is a base case - 0!=1
    if n == 0:
        return 1
    # use recursion
    result1 = factorial_head(n-1)
    # we do some operations
    result2 = n* result1
    return result2
# print(factorial_head(10))


def fibonacci_head(n):
    if n==0:
        return 0
    if n == 1:
        return 1

    # we make the recursive function call(s)
    #we are going to do 2 recursion - we keep
    # calculating the fibonacci numbers
    # some values are calculate twice - there are multiple
    # stack frames with the same values
    fib1 = fibonacci_head(n-1)
    fib2 = fibonacci_head(n-2)

    result= fib1 + fib2
    return result
# print(fibonacci_head(40))

# 0 1 1 2 3 5 8 13 21 34 55


def hanoi(disk, source, middle, destination):
    # this is the base case - index 0 is always the smallest plate
#we manipulate the smallest plate in the base case
    if  disk == 0:
        print('Disk %s from %s to %s' %(disk, source, destination))

        return
    hanoi(disk -1, source, destination, middle)
    #this is not necessarily the largest plate - this is not the plate with index 0
    print('Disk %s from %s to %s' %(disk, source, destination))
    hanoi(disk-1,middle, source, destination)

# hanoi(1,'A','B','C')


# GREATEST COMMON DIVISOR
#Recursive Implementation
def gcd(a,b):
    #if  base-case : if b|a (without a remainder) then b is the GCD
    if b//a:
        return b
    return gcd(b, a%b)
gcd(30,10)
