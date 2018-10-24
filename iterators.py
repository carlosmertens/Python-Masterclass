# Example 1
string = ["1234567890"]
# for item in string:
#     print(item)

# Example 2

# my_iterator = iter(string)
# print(my_iterator)
# print(next(my_iterator))
# print(next(my_iterator))

# Example 3

# Create a list of items (you may use either strings or numbers in the list),
# then create an iterator using the iter() function.
#
# Use a for loop to loop "n" times, where n is the number of items in your list.
# Each time round the loop, use next() on your list to print the next item.
#
# hint: use the len() function rather than counting the number of items in the list.

my_working_days = ["monday", "tuesday", "wednesday", "thursday", "friday"]
iterator_created = iter(my_working_days)
for i in range (0, len(my_working_days)):
    day = next(iterator_created)
    print(day)
