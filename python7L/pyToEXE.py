import os
from os import *
TitleZero=('title EXE.PY')
os.system(TitleZero)
os.system("color 01")
os.system("mode con: cols=55 lines=11")
cls = 'cls'
os.system(cls)
print("By Kia7L: PY to EXE")
print("Type Name Only")
a=(raw_input("ICON?Name! : "))
b=(raw_input(".PY?Name! : "))
c=('pyinstaller -F -i .\\'+a)
d=('.ico ')
e=('.\\'+b)
f=('.py')
os.system(c+d+e+f)
input()
