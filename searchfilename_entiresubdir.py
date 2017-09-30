#!/Library/Frameworks/Python.framework/Versions/3.5/bin/python3

import os

root = '/Users/StanleyW/Desktop'
target = 'SAS-PHX.pdf'

for roots, dirs, files in os.walk(root):
    for filename in files:
        if target == filename:
           print('File Existed:' + os.path.join(roots,filename))
        else:
            ()
