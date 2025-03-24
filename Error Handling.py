try:
    print(x)
except NameError:
    print("Variable x is not defined!")
except:
    print("Something else is wrong.")
else:
    print("Nothing went wrong.")


try:
    f = open("demofile.txt")
    try:
        f.write("Lorum Ipsum")
    except:
        print("Something went wrong when writing to the file")
    finally:
        f.close()
except:
    print("Something went wrong when opening the file")

"""x = -1

if x < 0:
    raise Exception("No numbers bellow 0!")

"""

x = "hello"

if not type(x) is int:
    raise TypeError("Only integers are allowed!")