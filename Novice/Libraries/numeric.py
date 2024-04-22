# program to determine whether a number is even or odd

def is_even(number):
    if number<=0:
        return False
    return number%2==0


# program to find whether a number is prime or not

def is_prime(number):
    if number<=0:
        return False
    for index in range(2,number):
        if number%index==0:
            return False
    return True

# program to find factor of a number

def factor(number):
    for index in range(2,number):
        if number%index==0:
            yield index


    