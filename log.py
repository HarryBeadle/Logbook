#!/usr/bin/env python3

# Harry Beadle & Rhys Thomas
# log.py logbook generation software

# Debug Tools
CSS_DEBUG = False

import os, sys
from shutil import copyfile 
import argparse 
import datetime

# Parse Arguments
parser = argparse.ArgumentParser(
    description = "Appends a log to logbook.html")

parser.add_argument('-m', metavar='message', type=str, 
    help = "message for log")
parser.add_argument('-I', action='store_true', help="important")
parser.add_argument('-t', metavar="title", type=str, help="title")
parser.add_argument('-s', metavar="section header", type=str, 
    help="section header")
parser.add_argument('-c', metavar='color', type=str,
    help="color the text this CSS color")
parser.add_argument('-f', metavar='path', type=str, nargs='*',
    help="file to be attached to log")
parser.add_argument('-u', metavar='url', type=str, nargs='*', 
    help='URL to be attached to log')
parser.add_argument('-o', '--open', metavar='extension', type=str, 
    choices=['html','pdf','md'], help='open logbook.<html|md|pdf>')
args = parser.parse_args()

if args.open:
    print("opening .log/logbook."+args.open)
    os.system("open .log/logbook."+args.open)
    sys.exit()

timestamp = datetime.datetime.now().strftime("%c")
filestamp = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")

if CSS_DEBUG:
    style = open("logbookstyle.css", "r").read()
else:
    style = '/* Global Styling */\n\n* {\n\tfont-family: monospace;\n\tcolor: #D3D7CF;\n}\n\nbody {\n\twidth: 80%;\n\tmargin: auto;\n\tbackground-color: #151515;\n}\n\na {\n\ttext-decoration: none;\n}\n\nhr {\n\twidth: 100%;\n\tborder-color: #151515;\n}\n\n/* Specific Styling */\n\n.title {}\n\n.section {}\n\n.entry {\n\tbackground: #252525;\n\tborder-radius: 0.25em;\n\tpadding: 1em;\n\tmargin: 0.5em;\n}\n\n.file {\n\tborder: solid 1px;\n\tpadding: 0.5em;\n\ttext-decoration: none;\n}\n\n.important {\n\tcolor: red;\n}\n\n.timestamp {\n\tcolor: #555753;\n}\n\n.copyright {\n\tfont-size: small;\n\ttext-align: center;\n\tpadding: 1em;\n}'

# store everything in .log
if not os.path.exists(".log"):
    os.makedirs(".log")

if not os.path.isfile(".log/logbook.html"):
    with open(".log/logbook.html", 'w') as new_logbook:
            new_logbook.write("<style>\n")
            new_logbook.write(style)
            new_logbook.write("</style>\n")
            new_logbook.write("<p class='copyright'>Logbook software by Harry Beadle and Rhys Thomas</p>\n")

with open(".log/logbook.html", 'a') as logbook:
    logbook.write("<div class='entry'>")
    logbook.write("<span class='timestamp'>" + timestamp + "</span><br />") # first, print the timestamp
    if args.I: # Important
        logbook.write("<span class='important'>Important</span><br />")
    if args.c: # Colour
        logbook.write("<span style='color:" + args.c + ";'>")
    else:
        logbook.write("<span>")
    if args.t: # Title
        logbook.write("<h1>" + args.t + "</h1>")
    if args.s: # Section
        logbook.write("<h2>" + args.s + "</h2>")
    if args.m: # Message
        message = args.m
        mode = 0
        for char in message:
            if char == '`':
                if mode == 0:
                    logbook.write("<code>")
                    mode = 1
                else:
                    logbook.write("</code>")
                    mode = 0
            else:
                logbook.write(char)
    if args.f: # File Attachments
        if not os.path.exists(".log/logfiles"):
            os.makedirs(".log/logfiles")
        logbook.write("<p>")
        # list of files
        for files in args.f:
            name = os.path.basename(files)
            dst = os.path.join(".log/logfiles", filestamp + '-' + name)
            copyfile(files, dst)
            logbook.write("<a class='file' href='" + dst + "'>" + name + "</a> ")
        logbook.write("</p>")
    if args.u: # hyperlinks
        logbook.write("<p>")
        for link in args.u:
            logbook.write("<a class=url href='" + link + "'>" + link + "</a><br />")
            if not link == args.u[-1]:
                logbook.write("<br />")
        logbook.write("</p>")
    logbook.write("</span></div>\n")
