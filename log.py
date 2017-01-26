#!/usr/bin/env python3

# Harry Beadle & Rhys Thomas
# log.py logbook generation software

# Debug Tools
CSS_DEBUG = False

import os, sys
from shutil import copyfile 
import argparse 
import datetime
import platform
import webbrowser

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
parser.add_argument('-open', nargs='?', const='html', metavar='extension', type=str, 
    choices=['html'], help='open logbook in <html>')
args = parser.parse_args()

# Opening the Logbook
if args.open:
    print("opening logbook as a " + args.open.upper())
    if args.open == "html":
        webbrowser.open(".log/logbook.html")
    sys.exit()

# Generate Stamps
timestamp = datetime.datetime.now().strftime("%c")
filestamp = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")

# Include CSS
if CSS_DEBUG:
    style = open("logbookstyle.css", "r").read()
else:
    style = '/* Global Styling */\n\n* {\n\tfont-family: monospace;\n\tcolor: #D3D7CF;\n}\n\nbody {\n\twidth: 80%;\n\tmargin: auto;\n\tbackground-color: #151515;\n}\n\na {\n\ttext-decoration: none;\n}\n\nhr {\n\twidth: 100%;\n\tborder-color: #151515;\n}\n\n/* Specific Styling */\n\n.title {}\n\n.section {}\n\n.entry {\n\tbackground: #252525;\n\tborder-radius: 0.25em;\n\tpadding: 1em;\n\tmargin: 0.5em;\n}\n\n.file {\n\tborder: solid 1px;\n\tpadding: 0.5em;\n\ttext-decoration: none;\n}\n\n.important {\n\tcolor: red;\n}\n\n.timestamp {\n\tcolor: #555753;\n}\n\n.copyright {\n\tfont-size: small;\n\ttext-align: center;\n\tpadding: 1em;\n}'

# store everything in .log/
if not os.path.exists(".log"):
    os.makedirs(".log")

# write styles and copyright to new html document
if not os.path.isfile(".log/logbook.html"):
    with open(".log/logbook.html", 'w') as new_logbook:
            new_logbook.write("<style>\n")
            new_logbook.write(style)
            new_logbook.write("</style>\n")
            new_logbook.write("<p class='copyright'>Logbook software by Harry Beadle and Rhys Thomas</p>\n")

# save to temp then logbook.write() if no errors
with open(".log/temp.html", 'a') as temp:
    temp.write("<div class='entry'>")
    temp.write("<span class='timestamp'>" + timestamp + "</span><br />")
    if args.I: # Important
        temp.write("<span class='important'>Important</span><br />")
    if args.c: # Colour
        temp.write("<span style='color:" + args.c + ";'>")
    else:
        temp.write("<span>")
    if args.t: # Title
        temp.write("<h1>" + args.t + "</h1>")
    if args.s: # Section
        temp.write("<h2>" + args.s + "</h2>")
    if args.m: # Message
        message = args.m
        mode = 0
        for char in message:
            if char == '`':
                if mode == 0:
                    temp.write("<code>")
                    mode = 1
                else:
                    temp.write("</code>")
                    mode = 0
            else:
                temp.write(char)
    if args.f: # File Attachments
        if not os.path.exists(".log/logfiles"):
            os.makedirs(".log/logfiles")
        temp.write("<p>")
        for files in args.f:
            name = os.path.basename(files)
            dst = os.path.join(".log/logfiles", filestamp + '-' + name)
            copyfile(files, dst)
            temp.write("<a class='file' href='" + dst + "'>" + name + "</a> ")
        temp.write("</p>")
    if args.u: # Hyperlinks
        temp.write("<p>")
        for link in args.u:
            temp.write("<a class=url href='" + link + "'>" + link + "</a><br />")
            if not link == args.u[-1]:
                temp.write("<br />")
        temp.write("</p>")
    temp.write("</span></div>\n")

# no errors in CLI entry, now print to html
with open(".log/logbook.html",'a') as logbook, open(".log/temp.html",'r') as temp:
    for line in temp:
        logbook.write(line)

# delete temp
os.system("rm .log/temp.html")
