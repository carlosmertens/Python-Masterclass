# Main difference between List and Tuples:
# 1. List objects have to be the same type while Tuples can be mix types. Example 2
# 2. Tuples are immutable. They can not be change, although they can be reassign or retype individual object
# 3. The objects can easily be assigned to individual variables. Example 3


print("========== Example 1 ==========")  # Type of returns

t = "a", "b", "c"
print(t)  # It will be returned as a Tuple
print("a", "b", "c")  # It will be returned as a String
print(("a", "b", "c"))  # It will be returned a a Tuple due to the double parenthesis

print("========== Example 2 ==========")  # Changing Tuples

welcome = "Welcome to my nightmare", "Alice Cooper", 1975
bad = "Bad company", "Bad company", 1974
budgie = "Nightflight", "Budgie", 1981
imelda = "More mayhem", "Emilda", 2011
metallica = "Ride the lightning", "Metallica", 1984

print(metallica)
print(metallica[0])  # Like Lists, it will return the element on position 0
print(metallica[2])
# metallica[0] = "Master of puppets"  # It will create an error due that Tuples are immutable objects
print(imelda)
imelda = imelda[0], "Imelda May", imelda[2]  # Element could be modified like this command
print(imelda)

print("========== Example 3 ==========")  # Extracting values from a Tuple

title, artist, year = imelda
# The 3 values from Tuple imelda have been extracted to individual variables (title, artist and year)
print(title)
print(artist)
print(year)

print("========== Example 4 ==========")  # Tuples can have sub-tuples

imelda2 = "More mayhem", "Emilda", 2011, ((1, "Pulling the rug"), (2, "Psycho"), (3, "Mayhem"), (4, "Kentish"))
# Element 3 is as follow: ((sub-element 0), (sub-element 1), (sub-element 2),...)
print(imelda2)
title2, artist2, year2, tracks = imelda2
print(title2)
print(artist2)
print(year2)
print(tracks)

print("========== Example 5 ==========")  # Presenting imelda2
print(title2)
print(artist2)
print(year2)
for song in tracks:
    song_track, song_title = song
    # We can assign the value to variables so we can get rid of the parenthesis from the Tuples.
    print("\t{}. {}".format(song_track, song_title))  # "\t" will tab the line of each song

print("========== Example 6 ==========")  # A List within a Tuple. The lists can be change

imelda3 = "More mayhem", "Emilda", 2011, ([(1, "Pulling the rug"), (2, "Psycho"), (3, "Mayhem"), (4, "Kentish")])
# Element 3 was created as a list[]
print(imelda3)

imelda3[3].append((5, "All for you"))
# we have added in the object[3] which is a lists in position(5) of the list
print(imelda3)
imelda3[3].append((6, "Eternity"))

print("---")
title3, artist3, year3, tracks3 = imelda3
print(title3)
print(artist3)
print(year3)
for song in tracks3:
    song_track, song_title = song
    print("\t{}. {}".format(song_track, song_title))