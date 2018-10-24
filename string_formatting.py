print("STRING FORMATTING\n-----------------")
# -> STRINGS, COMMAND "print" AND SOME VARIABLE USE:
print(1+3)
print(3*5)
print()
print('The end')
print("Python's strings are easy to use")
print('We can include "quotes" in strings')
print("Hello" + " World")
greeting = "Hello"
name = "Carlos"
print(greeting + name)
print(greeting + ' ' + name)

# -> GETTING AN INPUT:

greeting = "Hello"
name = input("Please, enter your name: ")
print(greeting + " " + name + "!")

# -> SPLIT OVER, TAB SPACE AND QUOTES CHARACTERS

splitString = "This string has been\nsplit over\nby\nCarlos\nMertens"
print(splitString)
tabbedString = "1\t2\t3\t4\t5\t"
print(tabbedString)
otheSplitString = """This string has been
split over
by
Carlos
Mertens"""
print(otheSplitString)
print("""Nicole said: "I don't know where the car is" """)

# -> OPERATORS
a=12
b=3
print(a+b)
print(a-b)
print(a*b)
print(a/b) #returns float (double)
print(a//b) #returs int
print(a%b) #returns the residue after dividing
for i in range(1, a//b): #returns numbers from 1 to 4 (no included) Do not use / becuase will give error
    print(i)

print(a+b*4-5/3) #calculation order (/,*,+ and -)

# -> STRINGS
parrot = "Norwegian Blue"
print(parrot)
print(parrot[3])
print(parrot[0]) #positions on the strings begin with 0
print(parrot[9])
print(parrot[-1])
print(parrot[0:6])
print(parrot[6:])
print(parrot[:6])
print(parrot[-6:])
print(parrot[:-6])
number="1,2,3,4,5,6,7,8,9"
print(number[1::4])
number1="1, 2, 3, 4, 5, 6, 7, 8, 9"
print(number1[0::3])
print("Hello " *5) # returns the sring x times
today="friday"
print("day" in today) #in returns true or false
print("fri" in today)
print("thr" in today)
age=38
print("My age is " + str(age) + " years!")
# -> RELACEMENT FIELDS "Text{x}".format(x)
print("My age is {0} years!".format(age))
print("My age is %d years!" % age) # Python 2 format %d -> % int variable
print("There are {0} days in {1}, {2}, {3}, {4}, {5}, {6}, {7}".format(31, "January", "March", "May",
        "July", "August", "October", "December"))
print("""January: {0} days
February: {1} days
March: {0} days
April: {2} days
May: {0} days
June: {2} days
July: {0} days
August: {2} days
September: {0} days
October: {2} days
November: {0} days
December: {2} days""".format(31,28,30))

# MATH CALCULATIONS
# Squares and cubes

#for i in range(1, 12):
#    print("No. %2d squared is %4d and cube is %4d" %(i, i **2, i**3)) # %(space x)d returns with x space

for i in range(1, 12):
    print("No. {0:2} squared is {1:4} and cube is {2:4}".format(i, i **2, i**3))

# Pi
#print("Pi is approximately: %10f" % (22/7))

print("Pi is approximately: {0:10}".format(22/7))

