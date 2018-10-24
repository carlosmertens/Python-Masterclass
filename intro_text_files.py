print("========== Example 1 ==========")
# Opening a file save at my desktop (sample.txt)
# command open and close is for text files
jabber = open("/Users/carlosmertens/Desktop/sample.txt", "r")  # "r" is for reading only

for line in jabber:
    print(line)

jabber.close()

print("========== Example 2 ==========")
# Opening using command "with as"
# File is saved in the program folder:
# "/Users/carlosmertens/Documents/Python_Programs/IntroTextFiles/"

with open("sample.txt") as jabber2:
    for line in jabber2:
        if "JAB" in line.upper():  # will find the characters "jab" and converted to upper case to match
            print(line, end='')  # , end='' will drop to a new line every find

print("========== Example 3 ==========")
# Writing files

cities = ["Berlin", "Rome", "Barcelona", "Paris", "New York"]  # List created

with open("cities.txt", 'w') as city_file:  # Empty file create
    for city in cities:
        print(city, file=city_file)  # Write the List into the empty file
print("We have created a file with my favorites cities")
print("Check them out at: /Users/carlosmertens/Documents/Python_Programs/IntroTextFiles/cities.txt")

print("========== Example 4 ==========")

my_cities = []  # Empty List created

with open("cities.txt", 'r') as city_file:
    for city in city_file:
        # my_cities.append(city)  # Add the cities from the file cities.txt
        my_cities.append(city.strip("\n"))  # .strip("\n") cleans the spaces

print(my_cities)  # Print the List my_cities
for city in my_cities:
    print(city)  # Print individual item from the list

print("========== Example 5 ==========")
# Creating a file writing in binary

with open("binary", "bw") as bin_file:  # "bw" for binary write command
    for i in range(17):  # We create number from 0 to 16
        bin_file.write(bytes([i]))  # We write the numbers in binary

with open("binary", "br") as bin_file2:  # "br" to read the binary file
    for b in bin_file2:
        print(b)

# We will not be able to actually read since it is binary file
