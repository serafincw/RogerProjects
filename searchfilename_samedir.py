#!/Library/Frameworks/Python.framework/Versions/3.5/bin/python3

import os

root = "/Users/StanleyW/Desktop"
target = 'test1.py'

if target in os.listdir(root):
    print("File Existed: " + os.path.join(root,target))
else:
    print("File not found, Sorry")
