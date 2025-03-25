#f = open("demofile.txt")
#f = open("demofile.txt", "rt")

#f = open("demofile.txt", "r")
#print(f.read(57))
#print(f.readline())
#print(f.readline())

#for x in f:
    #print(x)

#print(f.readline())
#f.close()

#f = open("demofile.txt", "r")
#print(f.readline())
#f.close()

f = open("demofile2.txt", "a")
f.write(" Add a new line of content!")
f.close()

f = open("demofile2.txt", "r")
print(f.read())

f = open("demofile3.txt", "w")
f.write("Woops! I have deleted the content!")
f.close()

f = open("demofile3.txt", "r")
print(f.read())


