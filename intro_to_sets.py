print("========== Example 1 ==========")

# Creating a set, option 1
farm_animals = {"sheep", "cow", "hen"}
# Notice that it is similar to creating a Dictionary but we are not providing the values
print(farm_animals)
for animal in farm_animals:
    print(animal)

print("-" * 20)

# Creating a set, option 2
wild_animals = set(["lion", "tiger", "panther"])
print(wild_animals)
for animal in wild_animals:
    print(animal)

farm_animals.add("horse")  # Add an object to the set
wild_animals.add("crocodile")
print(farm_animals)
print(wild_animals)

print("========== Example 2 ==========")

even = set(range(0, 40, 2))  # Creates a set of even numbers up to but not included 40
print(sorted(even))
print("There is " + str(len(even)) + " numbers in the Set even")

print("-" * 20)

square_tuple = (4, 6, 9, 16, 25)  # We create a Tuple
squares = set(square_tuple)  # We can change Tuples into Sets
print(squares)
print("There is " + str(len(squares)) + " numbers in the Set square")

print("-" * 20)

print(even.union(squares))  # We can join two Sets
print("There is " + str(len(squares.union(even))) + " in the combine Sets")
print("--> Notice, that the repeating objects became one!")

repeating_numbers = even.intersection(squares)  #
print("The repeating numbers are: " + str(sorted(repeating_numbers)))

print("-" * 20)

print(sorted(even))
even.discard(2)  # Remove a value
print(sorted(even))
even.remove(4)  # Remove a value
print(sorted(even))

print("========== Example 3 ==========")
# Frozen Sets

even_immutable = frozenset(range(0, 100, 2))  # Can not be modified, added or removed.
print(even_immutable)

print("-" * 20)

sample_text = "Python is a powerful language"

vowels = frozenset("aeiou")
# vowels = {"a", "e", "i", "o", "u"}
final_set = set(sample_text).difference(vowels)
print(final_set)
