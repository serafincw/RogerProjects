#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3
import os, sys

#定義function
def search_specific_file(targetFile, targetFolder):
    guessFilepath = []

    for roots, dirs, files in os.walk(targetFolder):
        for filename in files:
            if filename == targetFile:
                guessFilepath.append(os.path.join(roots, filename))

            else:
                ()
                
    if len(guessFilepath) == 0:
        print("No Such File, sorry")
    else:
        for ele in guessFilepath:
            print("File Existed:" + ele)




#使用function
search_specific_file('test1.py', '/Users/StanleyW/Desktop')
print('---------------------------------------------------------')
search_specific_file('stanJerkOff.mov', '/Users/StanleyW/Desktop')