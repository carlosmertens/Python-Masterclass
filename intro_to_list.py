print("========== Example 1 ==========")

team_members = ["Carlos", "Antonio", "Daniel", "Dominika", "Michael"]
print(team_members)
team_members.append(input("Enter new member: "))
print(team_members)

for state in team_members:
    print("Team member: " + state)

print("========== Example 2 ==========")

even_numbers = [2, 4, 6, 8]
odd_numbers = [1, 3, 5, 7, 9]
print(even_numbers + odd_numbers)
print(sorted(even_numbers + odd_numbers))  # Arrange the numbers is order
all_numbers = even_numbers + odd_numbers
all_numbers.sort()  # Arrange the numbers is order
print(all_numbers)

print("========== Example 3 ==========")

list_1 = []
list_2 = list()

print("List 1: {}".format(list_1))
print("List 2: {}".format(list_2))

if list_1 == list_2:
    print("The list are equal")

print(list("The list are equal"))

print("========== Example 4 ==========")

# add to the program below so that if it finds a meal without spam
# it prints out each of the ingredients of the meal.
# You will need to set up the menu as we did before

menu = []
menu.append(["egg", "spam", "bacon"])
menu.append(["egg", "sausage", "bacon"])
menu.append(["egg", "spam"])
menu.append(["egg", "bacon", "spam"])
menu.append(["egg", "bacon", "sausage", "spam"])
menu.append(["spam", "bacon", "sausage", "spam"])
menu.append(["spam", "egg", "spam", "spam", "bacon", "spam"])
menu.append(["spam", "egg", "sausage", "spam"])

print(menu)

for meal in menu:
    if "spam" not in meal:
        print(meal)
        for ingredient in meal:
            print(ingredient)

print("========== Example 5 ==========")
# Wrong use of the List

my_list = ["a", "b", "c", "d"]
bad_string = " "

for c in my_list:
    bad_string = ", ".join(my_list)
    # Every time it goes in the loop, it will create a new List because List is immutable

print(bad_string)

# Good use of the List

good_string = ", ".join(my_list)
print(good_string)

my_letters = "abcdefghijklmnopqrstuvwxy"
print(", ".join(my_letters))

