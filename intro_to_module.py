# import turtle
import time
import datetime
import pytz
#
# # noinspection PyUnresolvedReferences
# # comment above was used to remove the warning due t o a bug in the turtle module
#
# turtle.forward(150)
# turtle.right(250)
# turtle.forward(150)
#
# time.sleep(5)

# ====================================
# import random
# import webbrowser
#
# # webbrowser.open("https://www.python.org/")
#
# help(webbrowser)
# print("-" * 50)
# help(random)
# print("-" * 50)
# help(random.randint)

# ====================================
# import time (already imported above)
print("=" * 10)

print(time.gmtime(0))
print(time.localtime())
print(time.time())

# ====================================
# import pytz (already imported above)
# import datetime (already imported above)
print("=" * 50)

country = "Europe/Moscow"

tz_to_display = pytz.timezone(country)
local_time = datetime.datetime.now(tz=tz_to_display)
print("The time in {} is {}".format(country, local_time))
print("UTC is {}".format(datetime.datetime.utcnow()))
