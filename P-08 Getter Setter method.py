#Getter and Setter method
class car:
    def __init__(self, a=40):
        self.speed=a
    def get_speed(self):    #getter method
        return self.speed
    def set_speed(self,a):  #setter method
        self.speed=a
        return

c1=car()
c1.get_speed()
c1.set_speed(20)
