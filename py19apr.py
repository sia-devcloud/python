#number=int(input("Enter the number: "))
number=17
while True:
    if number==1:
        break
    elif number%2==0:
        number=number//2
    elif number%2 !=0:
        number=(number*3)+1
    print(number)
print(number)