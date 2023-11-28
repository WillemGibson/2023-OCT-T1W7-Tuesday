# Scope - Global and local

# Global- Can be called anywhere
a = 5
b = [1, 2, 3]

# Local - Can only be called in a function
fname = "Willem"
lname = "Gibson"

def greet():
    fname = "Steve"
    lname = "Smith"
    print("Inside the function")
    print(fname)
    print(lname)

def fn1():
    print(fname)

print("Outside the funciton")
print(fname)
print(lname)

greet()