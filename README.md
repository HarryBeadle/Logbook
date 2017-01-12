# Logbook

Python digital logbook.

Appends logbook entries to a HTML file `logbook.html`.

In it's current state **Logbook** supports:
 - Styling for titles (`-t`), sections (`-s`), colors (`-c color`) and imporant tags (`-I`).
 - Attach multiple files to be saved in the current state for backup and refrance.

Usage:

```
usage: logbook [-h] [-m message] [-I] [-t title] [-s section header]
               [-c color] [-f [path [path ...]]]

Appends a log to logbook.html

optional arguments:
  -h, --help            show this help message and exit
  -m message            Text for log, title or section.
  -I                    Important
  -t title              Title
  -s section header     Section
  -c color              Color the text this CSS color
  -f [path [path ...]]  File to be attached to log.
```
