# -----> IF ELIF AND ELSE

# -> DRINK AGE TEST
# name = input("What is your name?: ")
# age = int(input("How old are you, {0}?: ".format(name)))
# print(age)
#
# if age >= 21:
#     print("You are old enough to drink!")
#     drink= input("What would you have?: ")
#     print("{0}, it is!".format(drink))
# else:
#     print("No old enough to drink. Please, come back in {0} years, {1}!".format(21-age, name))

# ----------------------------

# -> GUESS NUMBER 5 TEST
# print("Please guess a number between 0 and 9: ")
# guess = int(input())
# print(guess)
#
# if guess < 5:
#     print("Please guess higher: ")
#     guess = int((input()))
#     if guess == 5:
#         print("Well done! You have guessed it")
#     else:
#         print("Sorry, but you were not able to guess")
# elif guess > 5:
#     print("Please guess lower")
#     guess = int(input())
#     if guess == 5:
#         print("Well done! You have guessed it")
#     else:
#         print("Sorry, but you were not able to guess")
# else:
#     print("You got it at first time. You are awesome!")

# ----------------------------

# ------> FOR LOOPS

# for i in range(1,20): # Counter
#   print("i is now: {}.".format(i))

# ---------

# number = "9, 223, 372, 032, 832, 765, 809"
# for i in range(0, len(number)):
#    print(number[i])

# number = "9, 223, 372, 032, 832, 765, 809"
# for i in range(0, len(number)):
#      if number[i] in '0123456789': #removing the comas and spaces from the list
#          print(number[i],end='') # end='' cut the lines

# -> or

# number = "9, 223, 372, 032, 832, 765, 809"
# cleanedNumber = ''

# for i in range(0, len(number)):
#     if number[i] in '0123456789': #removing the comas and spaces from the list
#         cleanedNumber = cleanedNumber +" " + number[i]
#
# newNumber = cleanedNumber
# print('The numbers are: {}.'.format(newNumber))

# --> or using "char"

# number = "9, 223, 372, 032, 832, 765, 809"
# cleanedNumber = ''
#
# for char in number:
#     if char in '0123456789':
#         cleanedNumber = cleanedNumber + char
#
# newNumber = int(cleanedNumber)
# print("The number are {}".format(newNumber))

# ---> Multiplication table (Nesting for loops)

# for i in range (1,13):
#     for j in range(1,13):
#         print("{1} multiply {0} is {2}".format(i, j , i*j))
#     print("===================")

# -> Continue command
shopping_list = ["milk", "pasta", "eggs", "spam", "bread", "rice"]
for item in shopping_list:
    if item == "spam":
        continue  # continue will ignore spam and jump to next item
    print("{} is needed".format(item))

print("---------")

# -> Break command
shopping_list = ["milk", "pasta", "eggs", "spam", "bread", "rice"]
for item in shopping_list:
    if item == "spam":
        break  # break will ignore from spam and on
    print("{} is needed".format(item))

























