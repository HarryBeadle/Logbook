# Install Logbook
# Harry Beadle and Rhys Thomas

# harrybeadle.xyz

import platform, os
from shutil import copyfile

p = platform.system()

if p == "Linux":
    if os.path.isdir("~/.bin"):
        dir = "~/.bin/"
    else:
        dir = "/usr/local/bin"

    print("Copying files to %s." % dir)
    copyfile("log.py", dir + "/log")
    print("Done.")


if p == "Windows":
    print("Windows is not currently supported by the installer.")
    print("Please install manually.")

