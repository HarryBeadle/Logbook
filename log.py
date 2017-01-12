#!/usr/bin/env python3

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

parser.add_argument('-m', metavar='message', type=str, help = "message for log")
parser.add_argument('-I', action='store_true', help="important")
parser.add_argument('-t', metavar="title", type=str, help="title")
parser.add_argument('-s', metavar="section header", type=str, help="section header")
parser.add_argument('-c', metavar='color', default='black', type=str,
    help="color the text this CSS color")
parser.add_argument('-f', metavar='path', type=str, nargs='*',
    help="file to be attached to log")
parser.add_argument('-u', metavar='url', type=str, nargs='*', help='URL to be attached to log')
args = parser.parse_args()

datemark = datetime.datetime.now().strftime("%Y%m%d%H%M%s")

with open("logbook.html", 'a') as logbook:
    # Output date
    logbook.write("<a name='" + datemark + "'><small style='font-family:monospace;'>" + os.popen("date", 'r').read()[:-1] + "</small></a> <a href='#" + datemark + "'>🔗</a><br />")
    if args.I:
        # Imporant
        logbook.write("<b style='color:red;font-family:monospace;'>Important</b><br />")
    logbook.write("<span style='font-family:sans-serif; color:" + args.c + ";'>")
    if args.t:
        # Title
        logbook.write("<h1 style='font-family:sans-serif;'>" + args.t + "</h1>")
    if args.s:
        # Header
        logbook.write("<h2 style='font-family:sans-serif;'>" + args.s + "</h2>")
    if args.m:
        # Entry
        message = args.m
        mode = 0
        for char in message:
            if char == '`':
                if mode == 0:
                    logbook.write("<code>")
                    mode = 1;
                else:
                    logbook.write("</code>")
                    mode = 0;
            else:
                logbook.write(char)
    if args.f:
        # Files
        logbook.write("<p style='font-family:monospace;'>")
        if not os.path.exists("files"):
            os.makedirs("files")
        # list of files
        for files in args.f:
            name = os.path.basename(files)
            dst = os.path.join("files", datemark + '-' + name)
            copyfile(files, dst)
            logbook.write("<a style='text-decoration:none;border:solid 1px;padding:0.25em 0.5em 0.25em 0.5em;' href='" + dst + "'>💾 " + name + "</a> ") # Space at end required!
        logbook.write("</p>")
    if args.u:
        # Hyperlinks
        logbook.write("<p style='font-family:monospace;'>")
        for link in args.u:
            logbook.write("<a href='" + link + "'>" + link + "</a>")
            if not link == args.u[-1]:
                logbook.write("<br />")
        logbook.write("</p>")

    logbook.write("\n<hr></span>")
