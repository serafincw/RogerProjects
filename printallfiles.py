#!/Library/Frameworks/Python.framework/Versions/3.5/bin/python3
import os

root = "/Users/StanleyW/Desktop"
pathname = os.listdir(root)

for filename in pathname:
    print (os.path.join(root, filename))
