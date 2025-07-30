#magic methods(__new__, __init__, __str__)

class MyClass:
    def __new__(cls, value):
        print("[__new__] Creating instance")     #__new__
        instance = super().__new__(cls)
        return instance

    def __init__(self, value):
        print("[__init__] Initializing instance")  #__init__
        self.value = value

    def __str__(self):
        return f"[__str__] MyClass with value: {self.value}"  #__str__

obj = MyClass(10)
print(obj)
