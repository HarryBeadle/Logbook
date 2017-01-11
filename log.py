# Harry Beadle
# log.py log book generation software

import os
from sys import argv
from shutil import copyfile
import argparse
import datetime

# Parse Arguments
parser = argparse.ArgumentParser(
	description = "Appends a log to logbook.html")
parser.add_argument('text', metavar='MESSAGE', type=str, 
	help = "Text for log, title or section.")
parser.add_argument('-I', action="store_true", help="Important")
parser.add_argument('-t', action="store_true", help="Title")
parser.add_argument('-s', action="store_true", help="Section")
parser.add_argument('-c', default='black', type=str, 
	help="Color the text this CSS color")
parser.add_argument('-f', type=str, 
	help="File to be attached to log.")
args = parser.parse_args()

datemark = datetime.datetime.now().strftime("%Y%m%d%H%M%s")

with open("logbook.html", 'a') as logbook:
	logbook.write("<a name='" + datemark + "'><small>" + os.popen("date", 'r').read()[:-1] + "</small></a> <a href='#" + datemark + "'>🔗</a><br />")
	if args.I:
		logbook.write("<b style='color:red;'>Important</b><br />")
	logbook.write("<span style='font-family:monospace; color:" + args.c + ";'>")
	if args.t:
		# Title
		logbook.write("<h1 style='font-family:serif;'> " + args.text + " </h1>")
	elif args.s:
		# Header
		logbook.write("<h2 style='font-family:serif;'> " + args.text + " </h2>")
	else:
		# Entry
		logbook.write(args.text)
	if args.f:
		logbook.write("<p>")
		if not os.path.exists("files"):
			os.makedirs("files")
		filepath, ext = os.path.splitext(args.f)
		basename = os.path.basename(args.f)
		dst = os.path.join("files", datemark + ext)
		copyfile(args.f, dst)
		logbook.write("<br /><a style='border:solid 1px;padding:0.1em;' href='" + dst + "'>" + basename + "</a>")
		logbook.write("</p>")
	logbook.write("\n<hr></span>")