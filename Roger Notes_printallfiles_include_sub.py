#!/Library/Frameworks/Python.framework/Versions/3.5/bin/python3

"""
上面那行就是shebang
基本上就是 !#<你python上which python3指令出來的path>

當你改完shebang後，你還需要到回到終端機，對該檔案改成可執行檔
chmod +x 檔案名稱
例如： chmod +x printallfiles_include_sub.py

這樣之後你再執行這個檔案時，你就可以直接用 ./printallfiles_include_sub.py 直接執行
而不需要再打 python3 printallfiles_include_sub.py


這個網頁有教學：
https://www.tutorialspoint.com/python3/python_basic_syntax.htm

"""


import os

root = "/Users/roger/Desktop"
#如果你用 os.getcwd() 可以得到目前所在的path, cwd = current working directory
#如果你用 os.chdir('Users/Stannley/Desktop') 可以轉換程式到你指定的資料夾位置



pathname = os.path.join(root)
"""
你這行pathname其實可以不用定義
因為通常會用到os.path.join 是想要將兩個以上的path合併起來
你可以參考這個網頁
http://www.bogotobogo.com/python/python_files.php
"""



#這是原本你寫的
#for pathname, subdirs, files in os.walk(root):
#    for filename in files:
#        print(os.path.join(pathname, filename))


#可以改成這樣
for root, dirs, files in os.walk(pathname):
#    print(root)
#    print(dirs)
#    print(files)
    for filename in files:
        print(os.path.join(pathname, filename))
