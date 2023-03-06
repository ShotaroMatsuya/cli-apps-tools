import os
import time

from halo import Halo

# Method 2
# with Halo(text="Analyzing Files", spinner="dots"):
#     for i in range(50):
#         time.sleep(1)
#         print("\n{}".format(i))

with Halo(text="Searching For Files", spinner="dots"):
    list_of_files = os.listdir(".")
    for i in range(len(list_of_files)):
        time.sleep(1)
        print("\nFound File ")
        print("\n{}".format(i))