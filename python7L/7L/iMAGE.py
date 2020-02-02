import os
from os import *
Title=('title iMAGE7L')
os.system(Title)
os.system("color 01")
os.system("mode con: cols=65 lines=15")
cls = 'cls'
os.system(cls)

print ("Choose Your .File Type")
a=(raw_input("Converting File Type Only: "))
b=(raw_input("Finish Photo File Type Only: "))
file0='.\magick.exe'
Folder0=' .\Photo'
Folder1=' .\Done'
MKDIR=('mkdir '+Folder0+Folder1) 

os.system(MKDIR)
os.system(file0+Folder0+Folder1)
print (file0+Folder0+Folder1)
print ("DoneFinish...")

input()
