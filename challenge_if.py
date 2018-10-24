# Write a small program to ask for a name and an age.
# When both values have been entered, check if the person
# is the right age to go on an 18-30 holiday (they must be
# over 18 and under 31).
# If they are, welcome them to the holiday, otherwise print
# a (polite) message refusing them entry.

name = input("May I have your name, please?: ")
age = int(input("Could you also give me your age, please?: "))

if (age >= 18) and (age <= 30):
    print("We welcome you to the 18-30 Holiday, {}!".format(name))
else:
    print("We are sorry, but with {0} you are not able to go in the 18-30 Holiday, {1}".format(age, name))
