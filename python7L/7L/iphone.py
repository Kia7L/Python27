import webbrowser
import os
import colorama
import tkinter
from os import *
from subprocess import call
from time import sleep
from tkinter import *
from colorama import *
root = Tk()
init()
#--------------Swiss-Photo.gif-only-Verry-small---------
photo0=PhotoImage(file=".\gif\python.gif")
photo3=PhotoImage(file=".\gif\google.gif")
cecho='.\\cecho.exe';
nircmd='.\\nircmd.exe';
READFILE=(' ".\Image\iphone\\')
ADDFILE=(' ".\Image\iphone\Photo.png"')
Copy='copy /Y'
DELETE=' del /F'
cls='cls'
Refresh='"C:\Program Files\Rainmeter\Rainmeter.exe" !Refresh'
topmost=' win settopmost ititle'
#-------------------------------------------------------
titlezero='title iphone11'
os.system(titlezero)
os.system("color 01")
os.system("mode con: cols=55 lines=11")
root.geometry("221x150")
os.system(cls)
#-------------------------------------------------------
class  Application(Frame):
    def CLS(APP):
        print(Style.BRIGHT + Fore.BLUE + Back.BLACK + 'CLEAR') 
        sleep(1) 
        os.system(cls);
    
    def UP(APP):
        print(Style.BRIGHT + Fore.BLUE + Back.BLACK + '+') 
        command1 = (nircmd +' changesysvolume +2000')
        os.system(command1);
        sleep(1)
        os.system(cls);
        
    def DOWN(APP):
        print(Style.BRIGHT + Fore.BLUE + Back.BLACK + '-') 
        command2 = (nircmd +' changesysvolume -2000')
        os.system(command2);
        sleep(1)
        os.system(cls);
        
    def IPHONE(APP):        
        print(Style.BRIGHT + Fore.BLUE + Back.BLACK + 'IPHONE WALLPAPER')
        os.system(cls);
        #os.system(nircmd + topmost +' "iphone11" 1')
        a=input('Choose1-17-21: ')
        aa='0-'
        command3=(Copy+READFILE+aa+a+'.png"')
        command3A=(command3+ADDFILE)
        os.system(command3A)
        print(a+'=iphone')
        os.system(Refresh)
        os.system(cls);
        
    def VOL3(APP):        
        print(Style.BRIGHT + Fore.BLUE + Back.BLACK + 'Street') 
        command5 = nircmd +' setsysVOL 42000'
        os.system(command5);
        sleep(1)
        os.system(cls);
        
    def COLOR(APP): 
       print (Style.BRIGHT + Fore.GREEN + Back.BLACK + "Color")
       webbrowser.open_new('http://www.science.smith.edu/dftwiki/images/3/3d/TkInterColorCharts.png')      
#------------------------------------------------------------
    def PYTHON(APP):
        os.system(cls);
        print (Style.BRIGHT + Fore.RED + Back.BLACK + "by:KIA7L")
        print (Style.BRIGHT + Fore.BLUE + Back.BLACK + "Python:Search")
        Pytho=(input('Type Search:'))
        webbrowser.open_new('https://www.google.com/search?source=hp&ei=ki36XOL4EYv3-gTbl5HoDg&q=Python:'+Pytho)

    def CHROME(APP):
        os.system(cls);
        print (Style.BRIGHT + Fore.RED + Back.BLACK + "Chrome")
        GoogleSearch = input('Google: ')
        webbrowser.open_new_tab('https://www.google.com/search?q='+ GoogleSearch)

    def createWidgets(APP):
#------------------------------------------------------------
        root.title('iph7L')
#------------------------------------------------------------
        commandcecho1 = cecho +' {01} High Low? {\n} '
        commandcecho2 = cecho +' {06} Welcome To Iphoneia... {\n} ' 
        os.system(cls);
        os.system(commandcecho1);
        os.system(commandcecho2);
#-------------------------Buttons----------------------------
        APP.VOL0=Button(APP)
        APP.VOL0["text"] = ("Swiss")
        APP.VOL0.config(image=photo0,height="20")
        APP.VOL0["width"] = "47"
        APP.VOL0["fg"]   = "gray70"
        APP.VOL0["command"] = APP.PYTHON
        APP.VOL0.grid(row = 1, column = 6, padx = 1, pady = 1)       
        
        APP.VOL1 = Button(APP)
        APP.VOL1["text"] = ("UP+")
        APP.VOL1["width"] = "6"
        APP.VOL1["fg"]   = "gray70"
        APP.VOL1["bg"]   = "gray24"
        APP.VOL1["command"] = APP.UP
        APP.VOL1.grid(row = 1, column = 7, padx = 1, pady = 1)
        
        APP.VOL2 = Button(APP)
        APP.VOL2["text"] = ("DOWN-")
        APP.VOL2["width"] = "6"
        APP.VOL2["fg"]   = "gray70"
        APP.VOL2["bg"]   = "gray24"
        APP.VOL2["command"] = APP.DOWN
        APP.VOL2.grid(row = 3, column = 7, padx = 1, pady = 1)
        
        APP.VOL3 = Button(APP)
        APP.VOL3["text"] = ("Wallpaper")
        APP.VOL3["width"] = "6"
        APP.VOL3["fg"]   = "gray70"
        APP.VOL3["bg"]   = "gray24"
        APP.VOL3["command"] = APP.IPHONE
        APP.VOL3.grid(row = 4, column = 7, padx = 1, pady = 1)

        APP.VOL4 = Button(APP)
        APP.VOL4["text"] = ("GOOGLE")
        APP.VOL4.config(image=photo3,height="20")
        APP.VOL4["width"] = "47"
        APP.VOL4["fg"]   = "gray70"
        APP.VOL4["command"] = APP.CHROME
        APP.VOL4.grid(row = 6, column = 6, padx = 9, pady = 1)

        APP.VOL5 = Button(APP) 
        APP.VOL5["text"] = ("CLS")
        APP.VOL5["width"] = "6"
        APP.VOL5["fg"]   = "black"
        APP.VOL5["bg"]   = "snow"
        APP.VOL5["command"] = APP.CLS
        APP.VOL5.grid(row = 4, column = 6, padx = 1, pady = 1)

        APP.VOL6 = Button(APP)
        APP.VOL6["text"] = ("COLOR")
        APP.VOL6["width"] = "6"
        APP.VOL6["fg"]   = "ivory"
        APP.VOL6["bg"]   = "gray85"
        APP.VOL6["command"] = APP.COLOR
        APP.VOL6.grid(row = 5, column = 6, padx = 9, pady = 1)
        
        APP.QUIT = Button(APP)
        APP.QUIT["text"] = ("QUIT")
        APP.QUIT["width"] = "6"
        APP.QUIT['fg']=('#CCCCCC')
        APP.QUIT['bg']=('#CD0000')
        APP.QUIT["command"] = APP.quit
        APP.QUIT.grid(row = 3, column = 6, padx = 9, pady = 1)
#----------------------------------------------------------        
        root.configure(bg='#000015')#color
#----------------------------------------------------------

    def __init__(app, master=None):
        Frame.__init__(app, master)
        app.pack()
        app.createWidgets()
#----------------------------------------------------------
APP = Application(master=root)
#----------------------------------------------------------
APP.mainloop()
APP.createWidgets()
root.destroy()
root.mainloop()
