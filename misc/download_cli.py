import random
import time

from halo import Halo

spinner = Halo(text="Downloading files.zip", spinner="dots")

try:
    spinner.start()
    for i in range(100):
        spinner.text = '{}% Downloaded file.zip'.format(i)
        time.sleep(random.random())
    spinner.succeed("Finished Downloading File")
    spinner.info("Done !!")
except (KeyboardInterrupt, SystemExit):
    spinner.stop()