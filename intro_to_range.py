"""
Program following the video.

Args:
    variable (type): description

Returns:
    type: description

Raises:
    Exception: description

"""
# Example 1
my_list = list(range(10))
print(my_list)

# Example 2
even = list(range(0, 20, 2))
odd = list(range(1, 20, 2))
print(even)
print(odd)

# Example 3

sevens = range(7, 1000000, 7)
x = int(input("Please enter a positive number less than a million: "))
if x in sevens:
    print("{} is divisible by seven".format(x))

# Example 4

decimals = range(0, 100)
print(decimals)

my_range = decimals[3:40:3]
print(my_range)

for i in my_range:
    print(i)

print("=" * 40)

for i in range(3, 40, 3):
    print(i)

print(my_range == range(3, 40, 3))


def hello():
    """
    Short description.

    A bit longer description.

    Args:
        variable (type): description

    Returns:
        type: description

    Raises:
        Exception: description

    """
    print("hello")
