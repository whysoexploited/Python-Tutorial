"""#legal variable names
myvar = "John"
my_var = "John"
_my-var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"
illegal variable names
2myvar = "John"
my-var = "John"
my var= "John"

# VARIABLE NAMES ARE CASE SENSITIVE
# Techniques to read multiword variables

#Camel case:
myVariableName = "John"

#Pascal case:
MyVariableName = "John"

#Snake case:
my_variable_name = "John"

############# ------------------------------MULTIPLE VARIABLES

x, y ,z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

x = y = z = "Orange"
print(x)
print(y)
print(z)

#unpacking a collection of data
fruits = ["apple", "banana", "cherry", "kiwi"]
x, y ,z, a = fruits
print(x)
print(y)
print(z)
print(a)

####### ---------------------------OUTPUT VARIABLES---------

x = "Python is awesome"
print(x)

x = "Python "
y = "is "
z = "awesome!"
print(x,y,z)

print(x+y+z)
#Without space after each word the text will be printed like this 'pythonisawesome!'
#We can use + operator to print this!
x = "Python"
y = "is"
z = "awesome!"
print(x + y + z)

#for number + works as a mathematical operator

x = 5
y = 10
print(x+y)

#x = 5
#y = "John"
#print(x+y)
print('')
"""
x = "awesome"
def myfunc():
    print("Python is " + x)


myfunc()

#Create a variable inside a function with the same name

def myfunc1():
    x= "fantastic"
    print("Python is " + x)

myfunc1()

print("Python is " + x)

#normally, when we create a variable inside a function the variable is local and can be used only inside
#to create a global variable inside a function use the global keyword