#FUNCTIONS

#using one arguments
def greet(name):
    print("hello", {name})
    greet("coco")

#using two arguments
def add(a,b):
    return a+b
result=add(5,5)
print("the addition is:")

#using default arguments
def add(a,b=10):
    return a+b
print(add())

#using keyword arguments
def myself(name,age,city):
    print(f"my name is {name}, from {city} and age is {age}")
    
