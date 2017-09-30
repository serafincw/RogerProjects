#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3

import os, sys

if len(sys.argv) != 3:
    raise SystemExit('usage: %s <TARGET_FILE> <SEARCH_PATH>' %sys.argv[0])


root = sys.argv[2]
target = sys.argv[1]

for roots, dirs, files in os.walk(root):
    for filename in files:
        if filename == target:
            print("File Existed:" + os.path.join(roots,filename))
        else:
            () 