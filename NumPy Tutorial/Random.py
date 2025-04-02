from numpy import random

x = random.randint(100)
print(x)

x = random.rand()
print(x)

x = random.randint(100, size=(5))
print(x)

x = random.randint(100, size=(3, 5))
print(x)

x = random.rand(5)
print(x)

x = random.rand(3, 5)
print(x)

x = random.choice([3, 5, 7, 9])
print(x)

x = random.choice([3, 5, 7, 9], size=(3, 5))
print(x)

