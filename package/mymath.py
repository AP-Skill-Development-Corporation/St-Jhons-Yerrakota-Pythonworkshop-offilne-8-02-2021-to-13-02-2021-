def isEven(n):
    if n%2 == 0:
        return True
    return False

def isOdd(n):
    #if n%2 == 1: or if n%2!=0:
    if n%2 == 0:
        return False
    return True

def isPrime(n):
    for i in range(2,n):
        if n%i == 0:
            return False
    return True