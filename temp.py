def is_factor(num):
    for index in range(2,num):
        if num%index==0:
            yield index


# def is_prime(num):
#     if num<=0:
#         return False
#     for index in range(2,num):
#         if num%index==0:
#             return False
#     return True)

print(list(is_factor(12)))
