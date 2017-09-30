#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3

import os, sys

def search(target, root):
    for roots, dirs, files in os.walk(root):
        for filename in files:
            if filename == target:
                print("File Existed:" + os.path.join(roots,filename))
            else:
                ()
    

search(sys.argv[1],sys.argv[2])
