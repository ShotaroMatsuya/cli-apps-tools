import time

from halo import Halo

# Method
spinner = Halo(text="Loading", spinner="dots", color="magenta", text_color="red")

spinner.start()
time.sleep(4)
spinner.start("\nAdding Files")
# Time Consuming Activity
time.sleep(4)
spinner.succeed("\nAdded Files")
time.sleep(4)

spinner.start("\nSetting Up System")
time.sleep(4)
spinner.succeed("\nFinished Setting Up System")

spinner.stop()
