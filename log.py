#!/usr/bin/env python3
# Rhys Thomas (forked from harrybeadle/logbook.git)
# log.py logbook generation software

import os 
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

timestamp = datetime.datetime.now().strftime("%c")
filestamp = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")

if not os.path.isfile("logbook.html"):
    os.system("./create-logbook")

with open("logbook.html", 'a') as logbook:
    logbook.write("<p>" + timestamp + "</p>") # first, print the timestamp
    if args.I: # important
        logbook.write("<span class=important>Important</span><br />")
    logbook.write("<span style='color:" + args.c + ";'>")
    if args.t: # title
        logbook.write("<h1>" + args.t + "</h1>")
    if args.s: # section
        logbook.write("<h2>" + args.s + "</h2>")
    if args.m: # message
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
    if args.f: # file attachments
        if not os.path.exists("logfiles"):
            os.makedirs("logfiles")
        logbook.write("<p>")
        # list of files
        for files in args.f:
            name = os.path.basename(files)
            dst = os.path.join("files", filestamp + '-' + name)
            copyfile(files, dst)
            logbook.write("<a class=file href='" + dst + "'>" + name + "</a> ")
        logbook.write("</p>")
    if args.u: # hyperlinks
        logbook.write("<p>")
        for link in args.u:
            logbook.write("<a class=url href='" + link + "'>" + link + "</a><br />")
            if not link == args.u[-1]:
                logbook.write("<br />")
        logbook.write("</p>")

    logbook.write("\n<hr></span>")
