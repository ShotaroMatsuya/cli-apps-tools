import time

from halo import Halo


# Method Decorator
@Halo(text='Loading', spinner='dots', color='cyan')
def loading_fxn():
    # Time Cousuming Activity
    time.sleep(5)
    print("\nAnalyzing Task Completed")


loading_fxn()

print("Continuing Break")

loading_fxn()