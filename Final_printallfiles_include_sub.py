#!/Library/Frameworks/Python.framework/Versions/3.5/bin/python3

import os

root = "/Users/StanleyW/Desktop"


for roots, dirs, files in os.walk(root):
    for filename in files:
        print(os.path.join(roots, filename))