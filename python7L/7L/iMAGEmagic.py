import webbrowser
import os
import colorama
import tkinter
from os import *
from subprocess import call
from time import sleep
from tkinter import *
from colorama import *

#NOTES-
#url = input('Google: ')
#webbrowser.open_new_tab('https://www.google.com/search?q='+ url)

#top-
os.system("Title iMAGE7L")
os.system("color 01")
os.system("mode con: cols=105 lines=15")
cls = ('cls')
os.system(cls)
#--------------------------------
#Variables-
file0=('.\cecho.exe');
file1=('.\magick.exe')
#file2='C:\L-zipo\nircmd.exe';
#file3='C:\Windows\nircmd.exe';
#--------------------------------
#echo-
echoFirst = (file0+' {01}iMAGIC7L.py{94}ByKia7L{\n}')
echoSecond = (file0+' {06}Write FILETYPE USED{70}{08}{\n}')
os.system(echoFirst)
print("")
os.system(echoSecond)
print("")
#Command-
Name1=(input('Photo\*._FileType_|png,gif,jpeg,ico: '))
Name2=(input('Done/0._FileType_|png,gif,jpeg,ico: '))
XX=(input('X_SIZE: '))
YY=(input('Y_SIZE: '))
#-------------------------------------------------------------
cover=(' "./' )
cap=('"')
one=(file1+'')
two=('"./Photo/*'+Name1)
three=('-resize '+XX)
four=('x'+YY)
five=(' "./Done/0.'+Name2+cap)

print(one + two + three + four + five)
echoThird = (file0+' {04}4sec{03}Continue...?{05}OK...?{\n}')
os.system(echoThird)
print("")
sleep(4)
os.system(one + two + three + four + five) 
print(one + two + three + four + five) 
#--------------------------------
color=(file0+' {94} {\n}')
color2=(file0+' {74} {\n}')
print("")
os.system(color)
echoFinalCode=(input('FinishUP|CODE: '))
os.system(color2)
os.system(echoFinalCode)
print(echoFinalCode)
#--------------------------------
input()
