import json

x = '{ "name":"John", "age":30, "city":"New York"}'  # PYTHON OBJ ---> DICTIONARY

y = json.loads(x)
print(y["age"])

x = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

# Convert into JSON
y = json.dumps(x)

print(y)

print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "carrot"]))
print(json.dumps(("apple", "banana")))
print(json.dumps("hello"))
print(json.dumps(46))
print(json.dumps(True))
print(json.dumps(4.76))
print(json.dumps(None))
print(json.dumps(False))

x = {
    "name": "John",
    "age": 30,
    "married": True,
    "divorced": False,
    "children": ("Ann", "Billy"),
    "pets": None,
    "cars": [
        {"model": "BMW 230", "mpg": 27.5},
        {"model": "Ford Edge", "mpg": 24.1}
            ]
}

print(json.dumps(x))
print(json.dumps(x, indent=4, separators=(". ", " ---> ")))
print(json.dumps(x, indent=4, sort_keys=True))