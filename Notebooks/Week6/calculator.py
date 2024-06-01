# for addition
def addition(x,y):
    return x+y

# for subtraction
def subtraction(x,y):
    return x-y

# for multiplacation
def multiplacation(x,y):
    return x*y

# for division
def division(x,y):
    return x/y

# for reminder
def reminder(x,y):
    return x%y

# for Square
def square(x):
    return x**2

#for Cube
def cube(x):
    return x**3


def fname(name1):
    def mname(name2):
        def lname(name3):
            return name1+name2+name3
        return lname
    return mname