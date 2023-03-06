import time

from halo import Halo

spinner = Halo(text="Loading", spinner="dots")

spinner.start()
time.sleep(4)

spinner.succeed("Loading Successful")
time.sleep(4)

spinner.start()
time.sleep(4)

spinner.fail("Loading FAILED")
time.sleep(4)

spinner.start()
time.sleep(4)

spinner.info("Info About Progress")
time.sleep(2)

spinner.start("Working")
time.sleep(4)

spinner.warn("Warning NOT Recommended")
time.sleep(4)

spinner.stop()
