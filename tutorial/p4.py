def func(f):
    def wrapper(*args , **kwags): ## accepts any number of postional arguments/paramters
        print("Started")
        rv= f(*args,**kwags)
        print("Ended")
        return rv
    return wrapper
@func # same as func2=func(func2)
def func2(x):
    print(x)
    return x
@func # same as func3=func(func3)
def func3():
    print("i am funk3")
x=func(func2)
# print(x)
# x()
#func2=func(func2)# this us storing the func with func2 as a paramater this is the begining of the decrator
x=func2("e")
func3()
print(x)
# this can be used to generlise minual tasks such as checking values of paramater
