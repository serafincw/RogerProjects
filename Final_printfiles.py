#!/Library/Frameworks/Python.framework/Versions/3.5/bin/python3

import os

root = "/Users/StanleyW/Desktop"

for filename in os.listdir(root):
    print (os.path.join(root, filename))