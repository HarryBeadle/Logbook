# Logbook

Python digital logbook.

Appends logbook entries to a HTML file `logbook.html`.

In it's current state **Logbook** supports:
 - Styling for titles (`-t`), sections (`-s`), colors (`-c color`) and imporant tags (`-I`).
 - Attach multiple files to be saved in the current state for backup and refrance.

usage: log.py [-h] [-m message] [-I] [-t title] [-s section header] [-c color]
              [-f [path [path ...]]] [-u [url [url ...]]]

Appends a log to logbook.html

optional arguments:
  -h, --help            show this help message and exit
  -m message            message for log
  -I                    important
  -t title              title
  -s section header     section header
  -c color              color the text this CSS color
  -f [path [path ...]]  file to be attached to log
  -u [url [url ...]]    URL to be attached to log
