def is_prime(num: int):
    for index in range(2,num):
        if num%index==0:
            return False
    return True

print(is_prime(71))