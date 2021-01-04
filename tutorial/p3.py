def hello():
    class Hi:
        pass
    return Hi
#class Test:
#    pass
class foo:
    def show(self):
        print("HI")
def add_attribute(self):
    self.z=9
Test = type("Test",(foo,),{"x":5 ,"a_a":add_attribute }) ## same as line 5-6 1st parameter name of class 2nd parameter inhertance 3rd parameter is attributes
t=Test()
print(t.x)
t.show()
t.a_a()
print(t.z)


class Meta(type):#creating a meta class that inherting the type class
    def __new__(self,class_name,bases,attributes):#modifing how the class is constructed init only initliase
                                        #when we create a new method/instance of class it will be constructed based on parameters
        print(attributes)
        a={}
        for name, values in attributes.items():
            if name.startswith("__"):
                a[name]=values
            else:
                a[name.upper()]=values
        print(a)
        return type(class_name,bases,a)
class Dog(metaclass=Meta):
    x=5
    y=8
    def hello(self):
        print("HI")

d=Dog()
#print(d.x) # wont work
print(d.X)
