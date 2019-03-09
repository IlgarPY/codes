#! /usr/bin/env python3

import sys, webbrowser, pyperclip

sys.argv

if len (sys.argv)>1:
     eingabe=" ".join(sys.avg)
else:
     eingabe=pyperclip.paste()

webbrowser.open("https://www.google.com/search?q=google.com" + eingabe)
