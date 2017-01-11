# Harry Beadle
# log.py log book generation software

from os import popen
from sys import argv

import argparse

# Parse Arguments
parser = argparse.ArgumentParser(description = "Appends a log to logbook.html")
parser.add_argument('text', metavar='s', type=str, 
	help = "Text for log, title or section.")
parser.add_argument('-I', action="store_true", help="Important")
parser.add_argument('-t', action="store_true", help="Title")
parser.add_argument('-s', action="store_true", help="Section")
parser.add_argument('-c', default='black', type=str, help="Color the text this CSS color")

args = parser.parse_args()
print "Text", args.text

with open("logbook.html", 'a') as logbook:
	logbook.write("<small>" + popen("echo $USER").read()[:-1] + " commited at " + popen("date", 'r').read()[:-1] + "</small><br />")
	print "//", popen("date", 'r').read()[:-1]
	if args.I:
		logbook.write("<b style='color:red;'>Important</b><br />")
	logbook.write("<span style='color:" + args.c + ";'>")
	if args.t:
		# Title
		logbook.write("<h1> " + args.text + " </h1>")
	elif args.s:
		# Header
		logbook.write("<h2> " + args.text + " </h2>")
	else:
		# Entry
		logbook.write(args.text)
	logbook.write("\n<hr></span>")