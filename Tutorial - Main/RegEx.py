import re
txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)
x = re.findall("ai", txt)
print(x)

x = re.findall("Portugal", txt)
print(x)

x = re.search("\s", txt)
print("The first white-space character is located in position:", x.start())

x = re.search("Portugal", txt)
print(x)

x = re.split("\s", txt)
print(x)

x = re.sub("\s", "--", txt, 2)  #Replace first two occurences
print(x)

x = re.search("ai", txt)
print(x)

x = re.search(r"\bS\w+", txt)
print(x.span())

x = re.search(r"\bS\w+", txt)
print(f"Gibberish: {x}")

x = re.search(r"\bS\w+", txt)
print(x.group())