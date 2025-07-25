#conditional statements


#if statements
num = int(input("enter the number:"))
if num%2 ==0:
    print("the number is even")


#else statements
age= int(input("enter your age:"))
if age>=18:
    print("adult")
else:
    print("no adult")


#elif statements
age = int(input("enter the age:"))
if 15<=age<=18:
    print("teenage")
elif age<=10:
    print("infants")
else:
    print("adulthood")
