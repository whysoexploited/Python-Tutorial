a = 33
b = 200
if b > a:
    print("b is greater than a")

a = 33
b = 33
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")

a = 200
b = 33

if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b is equal")
else:
    print("b is less than a")

a = 200
b = 33

if b > a:
    print("b is greater than a")
else:
    print("b iss less than a")

if a > b: print("a is greater than b")
a = 2
b = 330
print("A") if a > b else print("B")

a = 330
b = 330
print("A") if a > b else print("=") if b == a else print("B")

a = 200
b = 33
c = 500
if a > b and c > a:
    print("Both conditions true")

a = 200
b = 33
c = 500
if a> b or a > c:
    print("At least one is True")

a = 33
b = 200
if not a > b:
    print("a is not greater than b")

x = 41

if x > 10:
    print("Above 10")
    if x >20:
        print("Also above 20")
    else:
        print("Not above 20")

a = 33
b = 200

if b > a:
    pass