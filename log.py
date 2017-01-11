# Harry Beadle
# log.py log book generation software

from os import popen
from sys import argv

help = """Logbook by Harry Beadle
harrybeadle.xyz

Outputs (appends) to logbook.html in working directory.

Usage: log [option] [argument] text

Options:
	-t         Title
	-s         Section
	-I         Important
	-c [color] Color the text this CSS color.
"""

if argv[1] in ["help", "h", "-h", "-help"]:
	print help
	quit()

with open("logbook.html", 'a') as logbook:
	logbook.write("<small>" + popen("echo $USER").read()[:-1] + " commited at " + popen("date", 'r').read()[:-1] + "</small><br />")
	print "//", popen("date", 'r').read()[:-1]
	if argv[1] == "-t":
		# Title
		logbook.write("<h1> " + " ".join(argv[2:]) + " </h1>")
		print "Title:", " ".join(argv[2:])
	elif argv[1] == "-s":
		# Header
		logbook.write("<h2> " + " ".join(argv[2:]) + " </h2>")
		print "Section:", " ".join(argv[2:])
	elif argv[1] == "-I":
		logbook.write("<span style='color:red;'><b>Important</b><br>")
		logbook.write(" ".join(argv[2:]))
		logbook.write("</span>")
		logbook.write("\n<hr>")
		print "Important"
		print " ".join(argv[2:])
	elif argv[1] == "-c":
		# Color
		logbook.write("<span style='color:" + argv[2] + ";'>")
		logbook.write(" ".join(argv[3:]))
		logbook.write("</span>")
		logbook.write("\n<hr>")
		print " ".join(argv[3:])
	else:
		# Entry
		logbook.write(" ".join(argv[1:]))
		logbook.write("\n<hr>")
		print " ".join(argv[1:])