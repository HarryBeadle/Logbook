# Install Logbook
# Harry Beadle and Rhys Thomas

# harrybeadle.xyz

import platform, os
from shutil import copyfile
from sys import argv

# Move Files
p = platform.system()
if p == "Linux":
	if os.path.isdir("~/.bin"):
		dir = "~/.bin/"
	else:
		dir = "/usr/local/bin"
	print("Copying files to %s..." % dir)
	copyfile("log.py", dir + "/log")
if p == "Windows":
	print("!E Windows is not currently supported by the installer.")
	print("!E Please install manually.")

# Finish
print("Done.")