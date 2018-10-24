print("========== Example 1 ==========")
# Dictionaries are represented as: Name = {"key1" : "value1", "key2" : "key3" : "value3", ...}

fruit = {"orange": "a sweet, orange, citrus fruit",
         "apple": "good for making cider",
         "lemon": "a sour, yellow citrus fruit",
         "grape": "good for making wine",
         "lime": "a sour, green citrus fruit"}
print(fruit)
print(fruit["lemon"])

print("========== Example 2 ==========")
# Working with Dictionary

# Creating a second Dictionary
veggies = {"cabbage": "every child's favorite",
           "sprouts": "mmmmh, lovely",
           "spinach": "can I have some more, please"}
print(veggies)
veggies.update(fruit) # Add fruit Dictionary to the veggies Dictionary
print(veggies)

nice_and_nasty = fruit.copy()  # Create a new Dictionary copying fruit Dictionary
nice_and_nasty.update(veggies)  # Add veggies Dictionary to new one
print(nice_and_nasty)

fruit["pearl"] = "an odd shaped apple"  # add a case to the Dictionary
print(fruit)

fruit["lime"] = "great with tequila"  # replace the value of a case in the Dictionary
print(fruit)

del fruit["orange"]  # delete a case
print(fruit)

# fruit.clear()  # empty the Dictionary
print(fruit)

print("========== Example 3 ==========")
# Sorting the dictionary in order

ordered_keys = sorted(list(fruit.keys()))  # This will create a List
for f in ordered_keys:
    print(f + " - " + fruit[f])

print("========== OR ==========")

for f in sorted(fruit.keys()):  # This will just print the Dictionary
    print(f + " - " + fruit[f])

print("========== Example 4 ==========")
# Getting input by keyboard

while True:
    my_fruit = input("Please, enter a fruit: ")
    if my_fruit == "exit":
        print("Good Bye!")
        break
    if my_fruit in fruit:
        description = fruit.get(my_fruit)
        print(description)
    else:
        print("Sorry, I do not know " + my_fruit)

print("========== Example 5 ==========")
# Converting Dictionaries to Tuples

print(fruit)
print(fruit.items())
my_tuple = tuple(fruit.items())  # creating a Tuple with the Dictionary
print(my_tuple)

for snack in my_tuple:
    item, description = snack  # Separating the individual objects of the Tuple
    print(item + " is " + description)

# print(dict(my_tuple))

print("========== Example 6 ==========")
# Mini game program about mapping roads

# Creating a Dictionary with the values on the location of the player
# ===================================================================
# locations = {0: "You are sitting in from of the computer learning Python",
#              1: "You are standing at the end of the road in front of a brick building",
#              2: "You are at the top of the hill",
#              3: "You are inside a building, a well house for a small stream",
#              4: "You are in a valley beside a stream",
#              5: "You are in the forest"}
#
# # Creating a List that contains the Dictionaries calling the location Dictionary
# exits = [{"Q": 0},
#          {"W": 2, "E": 3, "N": 5, "S": 4, "Q": 0},
#          {"N": 5, "Q": 0},
#          {"W": 1, "Q": 0},
#          {"N": 1, "W": 2, "Q": 0},
#          {"W": 2, "S": 1, "Q": 0}]
#
# loc = 1
# while True:
#     available_exits = ", ".join(exits[loc].keys())
#     # Calling all the exits available in the List "exits" according to where the player stands
#     print(locations[loc])
#
#     if loc == 0:
#         print("Game Over")
#         break
#
#     direction = input("Available directions to take are " + available_exits + ": ").upper()
#     print()
#     if direction in exits[loc]:
#         loc = exits[loc][direction]
#     else:
#         print("Sorry, you can not go in that direction")
# ====================================================================

print("========== Challenge 1 ==========")

# Modify the program so that the exits is a dictionary rather than a list,
# with the keys being the numbers of the locations and the values being
# dictionaries holding the exits (as they do at present). No change should
# be needed to the actual code.
#
# Once that is working, create another dictionary that contains words that
# players may use. These words will be the keys, and their values will be
# a single letter that the program can use to determine which way to go.
# Improve it as you see it fits

locations = {0: "You are sitting in from of the computer learning Python",
             1: "You are standing at the end of the road in front of a brick building",
             2: "You are at the top of the hill",
             3: "You are inside a building, a well house for a small stream",
             4: "You are in a valley beside a stream",
             5: "You are in the forest"}

# Replacing [] with {}. Also, add the keys to each element (0:, 1:, 2:...)
exits = {0: {"Q": 0},
         1: {"W": 2, "E": 3, "N": 5, "S": 4, "Q": 0},
         2: {"N": 5, "Q": 0},
         3: {"W": 1, "Q": 0},
         4: {"N": 1, "W": 2, "Q": 0},
         5: {"W": 2, "S": 1, "Q": 0}}

# Adding vocabulary Dictionary
vocabulary = {"QUIT": "Q",
              "NORTH": "N",
              "SOUTH": "S",
              "EAST": "E",
              "WEST": "W"}

# Adding the name of the destinations Dictionary
name_exits = {1: {"2": 2, "3": 3, "5": 5, "4": 4},
              2: {"5": 5},
              3: {"1": 1},
              4: {"1": 1, "2": 2},
              5: {"2": 2, "1": 1}}

loc = 1
while True:
    available_exits = ", ".join(exits[loc].keys())
    # Calling all the exits available in the List "exits" according to where the player stands
    print(locations[loc])

    if loc == 0:
        print("Game Over")
        break
    else:
        all_exits = exits[loc].copy()
        all_exits.update(name_exits[loc])

    direction = input("Available directions to take are " + available_exits + ": ").upper()
    print()

    # Pass the user input, using the vocabulary Dictionary if necessary
    if len(direction) > 1:
        words = direction.split()
        for word in words:
            if word in vocabulary:
                direction = vocabulary[word]
                break

    if direction in all_exits:
        loc = all_exits[direction]
    else:
        print("Sorry, you can not go in that direction")

print("========== Challenge Advance Improvement ==========")
# Challenge time!
# We have mentioned that the data for the Adventure game could be organised in many
# different ways.  We've created another way for you.
# Your mission, if you choose to accept it, is to
# change the code to make it work.
# Below is the the complete program from the last video, but with the
# locations dictionary modified so that everything is in a single dictionary.
# N.B. Yes the code has some errors, thats what you need to fix!

locations = {0: {"desc": "You are sitting in front of a computer learning Python",
                 "exits": {},
                 "namedExits": {}},
             1: {"desc": "You are standing at the end of a road before a small brick building",
                 "exits": {"W": 2, "E": 3, "N": 5, "S": 4, "Q": 0},
                 "namedExits": {"2": 2, "3": 3, "5": 5, "4": 4}},
             2: {"desc": "You are at the top of a hill",
                 "exits": {"N": 5, "Q": 0},
                 "namedExits": {"5": 5}},
             3: {"desc": "You are inside a building, a well house for a small stream",
                 "exits": {"W": 1, "Q": 0},
                 "namedExits": {"1": 1}},
             4: {"desc": "You are in a valley beside a stream",
                 "exits": {"N": 1, "W": 2, "Q": 0},
                 "namedExits": {"1": 1, "2": 2}},
             5: {"desc": "You are in the forest",
                 "exits": {"W": 2, "S": 1, "Q": 0},
                 "namedExits": {"2": 2, "1": 1}}
             }

vocabulary = {"QUIT": "Q",
              "NORTH": "N",
              "SOUTH": "S",
              "EAST": "E",
              "WEST": "W",
              "ROAD": "1",
              "HILL": "2",
              "BUILDING": "3",
              "VALLEY": "4",
              "FOREST": "5"}

loc = 1
while True:
    availableExits = ", ".join(locations[loc]["exits"].keys())

    print(locations[loc]["desc"])

    if loc == 0:
        break
    else:
        allExits = locations[loc]["exits"].copy()
        allExits.update(locations[loc]["namedExits"])

    direction = input("Available exits are " + availableExits).upper()
    print()

    # Parse the user input, using our vocabulary dictionary if necessary
    if len(direction) > 1:  # more than 1 letter, so check vocab
        words = direction.split()
        for word in words:
            if word in vocabulary:   # does it contain a word we know?
                direction = vocabulary[word]
                break

    if direction in allExits:
        loc = allExits[direction]
    else:
        print("You cannot go in that direction")
