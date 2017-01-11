# Logbook

Python digital logbook.

Appends logbook entries to a HTML file `logbook.html`.

In it's current state **Logbook** supports:
 - Styling for titles (`-t`), sections (`-s`), colors (`-c color`) and imporant tags (`-I`).
 - Attach multiple files to be saved in the current state for backup and refrance.
 
Usage:

    usage: log.py [-h] [-I] [-t] [-s] [-c C] MESSAGE [-f [F [F ...]]]

    Appends a log to logbook.html

    positional arguments:
      MESSAGE         Text for log, title or section.

    optional arguments:
      -h, --help      show this help message and exit
      -I              Important
      -t              Title
      -s              Section
      -c C            Color the text this CSS color
      -f [F [F ...]]  File to be attached to log.
