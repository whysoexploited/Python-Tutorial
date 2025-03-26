import mymodule
import platform
from mymodule import person1

a = mymodule.person1["age"]
print(a)
x = platform.system()
print(x)

x = dir(platform)
print(x)

print(person1["age"])

