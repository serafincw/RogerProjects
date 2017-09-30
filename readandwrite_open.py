#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3

import os,sys


def lyrics(filename):
    file = os.path.abspath(filename)
    hellofiles = open(file)
    for i in hellofiles.readlines():
        print(i)

    hellofiles.close()

lyrics(sys.argv[1])

