import os

root = "/Users/StanleyW/Desktop"
pathname = os.path.join(root)

for pathname, subdirs, files in os.walk(root):
    for filename in files:
        print(os.path.join(pathname, filename))