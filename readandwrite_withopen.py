#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3

import os,sys


def lyrics(filename):
    file = os.path.abspath(filename)
    with open(file) as i:
        readlyrics = i.readlines()
        for i in readlyrics:
            print(i)
    
lyrics(sys.argv[1])

