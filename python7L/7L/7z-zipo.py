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
os.system("Title L-Zipo")
os.system("color 01")
os.system("mode con: cols=105 lines=15")
cls = ('cls')
os.system(cls)
#--------------------------------
#Variables-
file0=('cecho.exe');
file1=('7z.exe')
#file2='C:\L-zipo\nircmd.exe';
#file3='C:\Windows\nircmd.exe';
#--------------------------------
#echo-
echoFirst = (file0+' {01}L-zipo7zip.py{94}ByKia7L{\n}')
echoSecond = (file0+' {06}ChooseFolder USED .\{70}{08}{\n}')
os.system(echoFirst)
print("")
os.system(echoSecond)
print("")
#Command-
Name2=(input('FOLDER_COMPRESS_LOCATION|.File_Type: '))
Name1=(input('FILE_SAVED|.File_Type-iso,7z,gzip,zip2,zip.100: '))
#Form0=(input('(ctrl+LShift+C) -1111/0x0A/-1111^11111111/0x00 : '))
#-------------------------------------------------------------
Form1=('-1111/0x0A/-1111^11111111/0x00')
cover=(' "./' )
one=(file1+' a')
two=(' -ax'+Form1)
three=(cover+Name1)
four=('" "'+Name2)
cap=('"')
print(one + two + three + four + cap)
echoThird = (file0+' {04}4{03}Continue...?{05}OK...?{\n}')
os.system(echoThird)
print("")
sleep(4)
os.system(one + two + three + four+cap) 
print(one + two + three + four+cap)
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
