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
#--------------------------------------------------------
titlezero='title Swisscmd'
os.system(titlezero)
os.system("color 01")
os.system("mode con: cols=55 lines=11")
root.geometry("399x349")
#--------------Swiss-Photo.gif-only-Verry-small----------
photo0=PhotoImage(file=".\gif\switzerland.gif")
photo1=PhotoImage(file=".\gif\datpiff.gif")
photo2=PhotoImage(file=".\gif\python.gif")
photo3=PhotoImage(file=".\gif\google.gif")
photo4=PhotoImage(file=".\gif\pandora.gif")
photo5=PhotoImage(file=".\gif\snake.gif")
file0='.\\cecho.exe';
file1='.\\nircmd.exe';
cls = 'cls'
READFILE=(' "%UserProfile%\Documents\Rainmeter\Skins\-Supreme-11\@Resources\Image\iphone\\')
ADDFILE=(' "%UserProfile%\Documents\Rainmeter\Skins\-Supreme-11\@Resources\Image\iphone\Photo.png"')
Copy='copy /Y'
DELETE=' del /F'

class  Application(Frame):
#---------------------------------------------------------
    def SNAKE(APP):
        os.system(cls);
        print (Style.BRIGHT + Fore.GREEN + Back.BLACK + "SNAKE")
        YU=raw_input('SNAKE-Search:')
        webbrowser.open_new('https://www.Google.com/results?search_query='+ YU)

    def IPHONE(APP):        
        print(Style.BRIGHT + Fore.BLUE + Back.BLACK + 'IPHONE WALLPAPER')
        os.system(cls);
        #os.system(nircmd + topmost +' "iphone11" 1')
        a=raw_input('Choose1-19: ')
        aa='0-'
        command3=(Copy+READFILE+aa+a+'.png"')
        command3A=(command3+ADDFILE)
        os.system(command3A)
        print(a+'=iphone')
        os.system(Refresh)
        sleep(2)
        os.system(cls);   
        
#---------------------------------------------------------

#----------------------------------------------------------

    def CLS(APP):
        print(Style.BRIGHT + Fore.BLUE + Back.BLACK + 'CLEAR') 
        sleep(1) 
        os.system(cls);
    
    def UP(APP):
        print(Style.BRIGHT + Fore.BLUE + Back.BLACK + '+') 
        command1 = file1 +' changesysvolume +2000'
        os.system(command1);
        
    def DOWN(APP):
        print(Style.BRIGHT + Fore.BLUE + Back.BLACK + '-') 
        command2 = file1 +' changesysvolume -2000'
        os.system(command2);
        
    def VOL1(APP):        
        print(Style.BRIGHT + Fore.BLUE + Back.BLACK + 'low') 
        command3 = file1 +' setsysvolume 5200'
        os.system(command3);
        sleep(1)
        os.system(cls);
        
    def VOL2(APP):        
        print(Style.BRIGHT + Fore.BLUE + Back.BLACK + 'Ambient') 
        command4 = file1 +' setsysvolume 19200'
        os.system(command4);
        sleep(1)
        os.system(cls);
        
    def VOL3(APP):        
        print(Style.BRIGHT + Fore.BLUE + Back.BLACK + 'Street') 
        command5 = file1 +' setsysvolume 42000'
        os.system(command5);
        sleep(1)
        os.system(cls);
#-------------------------------------------------------------------------        
#-------------------------------------------------------------------------
    def PYTHON(APP):
        os.system(cls);
        print (Style.BRIGHT + Fore.RED + Back.BLACK + "by:KIA7L")
        print (Style.BRIGHT + Fore.BLUE + Back.BLACK + "Python:Search")
        Pytho=(raw_input('Type Search:'))
        webbrowser.open_new('https://www.google.com/search?source=hp&ei=ki36XOL4EYv3-gTbl5HoDg&q=Python:'+Pytho)

    def CHROME(APP):
        os.system(cls);
        print (Style.BRIGHT + Fore.RED + Back.BLACK + "Chrome")
        GoogleSearch = raw_input('Google: ')
        webbrowser.open_new_tab('https://www.google.com/search?q='+ GoogleSearch)

    def DATPIFF(APP):
        os.system(cls);
        print (Style.BRIGHT + Fore.BLUE + Back.BLACK + "Rappers:")
        DAT=raw_input('Datpiff:')
        print('')
        webbrowser.open_new('https://www.datpiff.com/mixtapes-search?criteria='+ DAT)
    
    def createWidgets(APP):
#----------------------------------------------------------------------------------------
        commandcecho1 = file0 +' {01} High Im Kia? {\n} '
        commandcecho2 = file0 +' {06} Welcome As I Comfort your D3ZIERS {\n} ' 
        os.system(cls);
        os.system(commandcecho1);
        print('')
        os.system(commandcecho2);
        print('')
#-----------------------------------------------------------------------------------------
        root.title('SNAKE7L')
        
        APP.GH = Button(APP)
        APP.GH["text"] = ("PLISKEN")
        APP.GH.config(image=photo5,height="200")
        APP.GH["width"] = "250"
        APP.GH["fg"]   = "gray70"
        APP.GH["command"] = APP.SNAKE
        APP.GH.grid(row = 1, column = 2, padx = 1, pady = 1)
#-------------------------SWISS-PHOTO.gif------------------------------
        APP.AABBCCZ=Button(APP)
        APP.AABBCCZ["text"] = ("Swiss")
        APP.AABBCCZ.config(image=photo0,height="20")
        APP.AABBCCZ["width"] = "45"
        APP.AABBCCZ["fg"]   = "gray70"
        APP.AABBCCZ["command"] = APP.PYTHON
        APP.AABBCCZ.grid(row = 2, column = 6, padx = 1, pady = 1)       
       
#--------------------------VOLUME--------------------------------------------
        APP.VOLUME1 = Button(APP)
        APP.VOLUME1["text"] = ("UP+")
        APP.VOLUME1["width"] = "6"
        APP.VOLUME1["fg"]   = "gray70"
        APP.VOLUME1["bg"]   = "gray24"
        APP.VOLUME1["command"] = APP.UP
        APP.VOLUME1.grid(row = 2, column = 7, padx = 1, pady = 1)
        
        APP.VOLUME2 = Button(APP)
        APP.VOLUME2["text"] = ("DOWN-")
        APP.VOLUME2["width"] = "6"
        APP.VOLUME2["fg"]   = "gray70"
        APP.VOLUME2["bg"]   = "gray24"
        APP.VOLUME2["command"] = APP.DOWN
        APP.VOLUME2.grid(row = 3, column = 7, padx = 1, pady = 1)
        
        APP.VOLUME3 = Button(APP)
        APP.VOLUME3["text"] = ("L")
        APP.VOLUME3["width"] = "6"
        APP.VOLUME3["fg"]   = "gray70"
        APP.VOLUME3["bg"]   = "gray24"
        APP.VOLUME3["command"] = APP.VOL1
        APP.VOLUME3.grid(row = 4, column = 7, padx = 1, pady = 1)

        APP.VOLUME3 = Button(APP)
        APP.VOLUME3["text"] = ("M")
        APP.VOLUME3["width"] = "6"
        APP.VOLUME3["fg"]   = "gray70"
        APP.VOLUME3["bg"]   = "gray24"
        APP.VOLUME3["command"] = APP.VOL2
        APP.VOLUME3.grid(row = 5, column = 7, padx = 1, pady = 1)

        APP.VOLUME4 = Button(APP)
        APP.VOLUME4["text"] = ("H")
        APP.VOLUME4["width"] = "6"
        APP.VOLUME4["fg"]   = "gray70"
        APP.VOLUME4["bg"]   = "gray24"
        APP.VOLUME4["command"] = APP.VOL3
        APP.VOLUME4.grid(row = 6, column = 7, padx = 1, pady = 1)
#-----------------------------ARTIST-----------------------------------

#----------------------------------------------------------------------

        APP.GD = Button(APP)
        APP.GD["text"] = ("IPHONE")
        APP.GD["width"] = "6"
        APP.GD["fg"]   = "gray70"
        APP.GD["bg"]   = "gray24"
        APP.GD["command"] = APP.IPHONE
        APP.GD.grid(row = 5, column = 6, padx = 1, pady = 1)
        
        APP.G = Button(APP)
        APP.G["text"] = ("GOOGLE")
        APP.G.config(image=photo3,height="20")
        APP.G["width"] = "45"
        APP.G["fg"]   = "gray70"
        APP.G["command"] = APP.CHROME
        APP.G.grid(row = 6, column = 6, padx = 1, pady = 1)
#----------------------------------------------------------------------
        APP.AABBCC = Button(APP) 
        APP.AABBCC["text"] = ("CLS")
        APP.AABBCC["width"] = "6"
        APP.AABBCC["fg"]   = "black"
        APP.AABBCC["bg"]   = "snow"
        APP.AABBCC["command"] = APP.CLS
        APP.AABBCC.grid(row = 4, column = 6, padx = 1, pady = 1)
        
        APP.QUIT = Button(APP)
        APP.QUIT["text"] = ("QUIT")
        APP.QUIT["width"] = "6"
        APP.QUIT['fg']=('#CCCCCC')
        APP.QUIT['bg']=('#CD0000')
        APP.QUIT["command"] = APP.quit
        APP.QUIT.grid(row = 3, column = 6, padx = 1, pady = 1)
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
