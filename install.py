#!/usr/bin/env python3
# Install Logbook
# Harry Beadle and Rhys Thomas

# harrybeadle.xyz

import platform, os
from shutil import copyfile

p = platform.system()

if p == "Linux" or p == "Darwin":
    if os.path.isdir(os.path.expanduser("~/.bin")):
        dir = os.path.expanduser("~/.bin")
    else:
        dir = "/usr/local/bin"

    print("Copying files to %s" % dir)
    copyfile("log.py", dir + "/log")
    print("Done.")


if p == "Windows":
    print("Windows is not currently supported by the installer.")
    print("Please install manually.")

