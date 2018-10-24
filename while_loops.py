# Example 1
i = 0
while i <= 10:
    print(i)
    i += 1

# Example 2
available_fruits = ["Apple", "Pearl", "Banana", "Grapes"]
chosen_fruit = ''
print("We have the following available fruits:  Apple, Pearl, Banana, Grapes")
while chosen_fruit not in available_fruits:
    chosen_fruit = input("Please choose one of the options above: ")
    if chosen_fruit == "exit":
        print("Good bye!")
        break
else:
    print("Enjoy your fruit!")
