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

#-----------------------------------------------------------------------
titlezero='title Swisscmd'
os.system(titlezero)
os.system("color 01")
os.system("mode con: cols=55 lines=11")
root.geometry("365x150")
#--------------Swiss-Photo.gif-only-Verry-small------------------------------------------------------
photo0=PhotoImage(file=".\gif\switzerland.gif")
photo1=PhotoImage(file=".\gif\datpiff.gif")
photo2=PhotoImage(file=".\gif\youtube.gif")
photo3=PhotoImage(file=".\gif\google.gif")
photo4=PhotoImage(file=".\gif\pandora.gif")
file0='.\\cecho.exe';
file1='.\\nircmd.exe';
commandcls = 'cls'
#------------------------------------------------------------------------

class  Application(Frame):
    def CLS(APP):
        print(Style.BRIGHT + Fore.BLUE + Back.BLACK + 'CLEAR') 
        sleep(1) 
        os.system(commandcls);
    
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
        os.system(commandcls);
        
    def VOL2(APP):        
        print(Style.BRIGHT + Fore.BLUE + Back.BLACK + 'Ambient') 
        command4 = file1 +' setsysvolume 19200'
        os.system(command4);
        sleep(1)
        os.system(commandcls);
        
    def VOL3(APP):        
        print(Style.BRIGHT + Fore.BLUE + Back.BLACK + 'Street') 
        command5 = file1 +' setsysvolume 42000'
        os.system(command5);
        sleep(1)
        os.system(commandcls);
#-------------------------------------------------------------------------        
    def COLOR(APP): 
       print (Style.BRIGHT + Fore.GREEN + Back.BLACK + "Color")
       webbrowser.open_new('http://www.science.smith.edu/dftwiki/images/3/3d/TkInterColorCharts.png')
    
    def ARTIST(APP):
       print (Style.BRIGHT + Fore.GREEN + Back.BLACK + "ARTIST")
       webbrowser.open_new('https://en.wikipedia.org/wiki/List_of_hip_hop_musicians')
       
    def PANDORA(APP):
       print (Style.BRIGHT + Fore.RED + Back.BLACK + "PANDORA")
       webbrowser.open_new('https://www.pandora.com ')
       
    def FABOLOUS(APP):
       print (Style.BRIGHT + Fore.RED + Back.BLACK + "FABOLOUS")
       webbrowser.open_new('https://www.datpiff.com/mixtapes-search?criteria=Fabolous&sort=relevance')
  
    def NOTORIOUS(APP):
       print (Style.BRIGHT + Fore.BLUE + Back.BLACK + "NOTORIOUS")
       webbrowser.open_new('https://www.datpiff.com/mixtapes-search?criteria=Notorious&sort=relevance')
       
    def PAC(APP):
       print (Style.BRIGHT + Fore.BLUE + Back.BLACK + "PAC")
       webbrowser.open_new('https://www.datpiff.com/mixtapes-search?criteria=2%20pac&sort=relevance')
    
    def BIGL(APP):
       print (Style.BRIGHT + Fore.GREEN + Back.BLACK + "BIGL")
       webbrowser.open_new('https://www.datpiff.com/mixtapes-search?criteria=Big%20L&sort=relevance')
    
    def EASYE(APP):
       print (Style.BRIGHT + Fore.RED + Back.BLACK + "EASYE")
       webbrowser.open_new('https://www.datpiff.com/mixtapes-search?criteria=Easy%20E&sort=relevance')
    
    def TUPAC(APP):
       print (Style.BRIGHT + Fore.RED + Back.BLACK + "Tupac")
       webbrowser.open_new('https://www.datpiff.com/mixtapes-search?criteria=TuPac&sort=relevance')
       
    def EMINEM(APP):
       print (Style.BRIGHT + Fore.RED + Back.BLACK + "Eminem")
       webbrowser.open_new('https://www.datpiff.com/mixtapes-search?criteria=eminem&sort=relevance')
       
    def ALIYAH(APP):
       print (Style.BRIGHT + Fore.RED + Back.BLACK + "ALIYAH")
       webbrowser.open_new('https://www.datpiff.com/mixtapes-search?criteria=Aaliyah&sort=relevance')
       
    def TI(APP):
       print (Style.BRIGHT + Fore.RED + Back.BLACK + "TI")
       webbrowser.open_new('https://www.datpiff.com/mixtapes-search?criteria=TI&sort=relevance')
       
    def GurillaBlack(APP):
       print (Style.BRIGHT + Fore.RED + Back.BLACK + "Gurilla Black")
       webbrowser.open_new('https://www.datpiff.com/mixtapes-search?criteria=Gorilla&sort=relevance')
       
    def TOOSHORT(APP):
       print (Style.BRIGHT + Fore.RED + Back.BLACK + "TOOSHORT")
       webbrowser.open_new('https://www.datpiff.com/mixtapes-search?criteria=TOO%20SHORT&sort=relevance')
       
    def Lilwayne(APP):
       print (Style.BRIGHT + Fore.RED + Back.BLACK + "Lilwayne")
       webbrowser.open_new('https://www.datpiff.com/mixtapes-search?criteria=Lilwayne&sort=relevance')

    def DOG(APP):
       print (Style.BRIGHT + Fore.RED + Back.BLACK + "SNOOP-DOG")
       webbrowser.open_new('https://www.datpiff.com/mixtapes-search?criteria=Snoop%20dog&sort=relevance')

    def AG(APP):
       print (Style.BRIGHT + Fore.RED + Back.BLACK + "AG")
       webbrowser.open_new('https://www.datpiff.com/mixtapes-search?criteria=AG&sort=relevance')

    def THREESIX(APP):
       print (Style.BRIGHT + Fore.RED + Back.BLACK + "THREE6")
       webbrowser.open_new('https://www.datpiff.com/mixtapes-search?criteria=Three%206%20Mafia&sort=relevance')
      
    def UGK(APP):
       print (Style.BRIGHT + Fore.RED + Back.BLACK + "UGK")
       webbrowser.open_new('https://www.datpiff.com/mixtapes-search?criteria=UGK&sort=relevance')

#-----------------------------------------------------------------------------------------
    def PYTHON(APP):
        os.system(commandcls);
        print (Style.BRIGHT + Fore.RED + Back.BLACK + "by:KIA7L")
        print (Style.BRIGHT + Fore.BLUE + Back.BLACK + "Python:Search")
        Pytho=(input('Type Search:'))
        webbrowser.open_new('https://www.google.com/search?source=hp&ei=ki36XOL4EYv3-gTbl5HoDg&q=Python:'+Pytho)

    def CHROME(APP):
        os.system(commandcls);
        print (Style.BRIGHT + Fore.RED + Back.BLACK + "Chrome")
        GoogleSearch = input('Google: ')
        webbrowser.open_new_tab('https://www.google.com/search?q='+ GoogleSearch)

    def YOUTUBE(APP):
        os.system(commandcls);
        print (Style.BRIGHT + Fore.GREEN + Back.BLACK + "YOUTUBE")
        YU=input('YouTube-Search:')
        webbrowser.open_new('https://www.youtube.com/results?search_query='+ YU)

    def DATPIFF(APP):
        os.system(commandcls);
        print (Style.BRIGHT + Fore.BLUE + Back.BLACK + "Rappers:")
        DAT=input('Datpiff:')
        print('')
        webbrowser.open_new('https://www.datpiff.com/mixtapes-search?criteria='+ DAT)
    
    def createWidgets(APP):
#----------------------------------------------------------------------------------------
        commandcecho1 = file0 +' {01} High Im Kia? {\n} '
        commandcecho2 = file0 +' {06} Welcome As I Comfort your D3ZIERS {\n} ' 
        os.system(commandcls);
        os.system(commandcecho1);
        print('')
        os.system(commandcecho2);
        print('')
    
#-----------------------------------------------------------------------------------------
        root.title('Swiss7L')

        #-------------------------SWISS-PHOTO.gif------------------------------

        APP.AABBCCZ=Button(APP)
        APP.AABBCCZ["text"] = ("Swiss")
        APP.AABBCCZ.config(image=photo0,width="47",height="20")
        APP.AABBCCZ["width"] = "47"
        APP.AABBCCZ["fg"]   = "gray70"
        APP.AABBCCZ["command"] = APP.PYTHON
        APP.AABBCCZ.grid(row = 1, column = 6, padx = 1, pady = 1)       
       
        #--------------------------VOLUME--------------------------------------------
        
        APP.VOLUME1 = Button(APP)
        APP.VOLUME1["text"] = ("UP+")
        APP.VOLUME1["width"] = "6"
        APP.VOLUME1["fg"]   = "gray70"
        APP.VOLUME1["bg"]   = "gray24"
        APP.VOLUME1["command"] = APP.UP
        APP.VOLUME1.grid(row = 1, column = 7, padx = 1, pady = 1)
        
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
        
        #---------------------------WEB-LINKS---------------------------------------------
        APP.A=Button(APP)
        APP.A["text"] = ("ARTIST")
        APP.A["width"] = "6"
        APP.A["fg"]   = "gray70"
        APP.A["bg"]   = "gray24"
        APP.A["command"] = APP.ARTIST
        APP.A.grid(row = 1, column = 1, padx = 1, pady = 1)
       
        APP.ARTIST = Button(APP)
        APP.ARTIST["text"] = ("DATPIFF")
        APP.ARTIST.config(image=photo1,width="47",height="20")
        APP.ARTIST["width"] = "46"
        APP.ARTIST["fg"]   = "gray70"
        APP.ARTIST["bg"]   = "gray24"
        APP.ARTIST["command"] = APP.DATPIFF
        APP.ARTIST.grid(row = 1, column = 2, padx = 1, pady = 1)
        
        APP.YOUTUB = Button(APP)
        APP.YOUTUB["text"] = ("YOUTUBE")
        APP.YOUTUB.config(image=photo2,width="47",height="20")
        APP.YOUTUB["width"] = "47"
        APP.YOUTUB["fg"]   = "gray70"
        APP.YOUTUB["command"] = APP.YOUTUBE
        APP.YOUTUB.grid(row = 1, column = 3, padx = 1, pady = 1)
        
        APP.PANDOR = Button(APP)
        APP.PANDOR["text"] = ("PANDORA")
        APP.PANDOR.config(image=photo4,width="47",height="20")
        APP.PANDOR["width"] = "46"
        APP.PANDOR["fg"]   = "white"
        APP.PANDOR["bg"]   = "gray24"
        APP.PANDOR["command"] = APP.PANDORA
        APP.PANDOR.grid(row = 1, column = 4, padx = 1, pady = 1)
        #-----------------------------ARTIST-------------------------------------------
  
        APP.B = Button(APP)
        APP.B["text"] = ("FABOL")
        APP.B["width"] = "6"
        APP.B["fg"]   = "gray85"
        APP.B["bg"]   = ("gray64")
        APP.B["command"] = APP.FABOLOUS
        APP.B.grid(row = 3, column = 1, padx = 1, pady = 1)
        
        APP.C = Button(APP)
        APP.C["text"] = ("NOTOR")
        APP.C["width"] = "6"
        APP.C["fg"]   = "gray85"
        APP.C["bg"]   = ("gray64")
        APP.C["command"] = APP.NOTORIOUS
        APP.C.grid(row = 3, column = 2, padx = 1, pady = 1)

        APP.D = Button(APP)
        APP.D["text"] = ("TUPAC")
        APP.D["width"] = "6"
        APP.D["fg"]   = "gray85"
        APP.D["bg"]   = ("gray64")
        APP.D["command"] = APP.TUPAC
        APP.D.grid(row = 3, column = 3, padx = 1, pady = 1)
        
        APP.GG = Button(APP)
        APP.GG["text"] = ("EMINEM")
        APP.GG["width"] = "6"
        APP.GG["fg"]   = "gray85"
        APP.GG["bg"]   = ("gray64")
        APP.GG["command"] = APP.EMINEM
        APP.GG.grid(row = 4, column = 2, padx = 1, pady = 1)
      
        APP.H = Button(APP)
        APP.H["text"] = ("BIGL")
        APP.H["width"] = "6"
        APP.H["fg"]   = "gray85"
        APP.H["bg"]   = ("gray64")
        APP.H["command"] = APP.BIGL
        APP.H.grid(row = 4, column = 3, padx = 1, pady = 1)
        
        APP.I = Button(APP)
        APP.I["text"] = ("ALIYAH")
        APP.I["width"] = "6"
        APP.I["fg"]   = "gray85"
        APP.I["bg"]   = ("gray64")
        APP.I["command"] = APP.ALIYAH
        APP.I.grid(row = 4, column = 4, padx = 1, pady = 1)
        
        APP.E = Button(APP)
        APP.E["text"] = ("PAC")
        APP.E["width"] = "6"
        APP.E["fg"]   = "gray85"
        APP.E["bg"]   = ("gray64")
        APP.E["command"] = APP.PAC
        APP.E.grid(row = 3, column = 4, padx = 1, pady = 1)
        
        APP.F = Button(APP)
        APP.F["text"] = ("EASYE")
        APP.F["width"] = "6"
        APP.F["fg"]   = "gray85"
        APP.F["bg"]   = ("gray64")
        APP.F["command"] = APP.EASYE
        APP.F.grid(row = 4, column = 1, padx = 1, pady = 1)
        
        APP.J = Button(APP)
        APP.J["text"] = ("TI")
        APP.J["width"] = "6"
        APP.J["fg"]   = "gray85"
        APP.J["bg"]   = ("gray64")
        APP.J["command"] = APP.TI
        APP.J.grid(row = 5, column = 1, padx = 1, pady = 1)
    
        APP.K = Button(APP)
        APP.K["text"] = ("Black")
        APP.K["width"] = "6"
        APP.K["fg"]   = "gray85"
        APP.K["bg"]   = ("gray64")
        APP.K["command"] = APP.GurillaBlack
        APP.K.grid(row = 5, column = 2, padx = 1, pady = 1)   
   
        APP.LL = Button(APP)
        APP.LL["text"] = ("SHORT")
        APP.LL["width"] = "6"
        APP.LL["fg"]   = "gray85"
        APP.LL["bg"]   = ("gray64")
        APP.LL["command"] = APP.TOOSHORT
        APP.LL.grid(row = 5, column = 3, padx = 1, pady = 1)   
   
        APP.MM = Button(APP)
        APP.MM["text"] = ("Wayne")
        APP.MM["width"] = "6"
        APP.MM["fg"]   = "gray85"
        APP.MM["bg"]   = ("gray64")
        APP.MM["command"] = APP.Lilwayne
        APP.MM.grid(row = 5, column = 4, padx = 1, pady = 1) 
        
        APP.FMM = Button(APP)
        APP.FMM["text"] = ("DOG")
        APP.FMM["width"] = "6"
        APP.FMM["fg"]   = "gray85"
        APP.FMM["bg"]   = ("gray64")
        APP.FMM["command"] = APP.DOG
        APP.FMM.grid(row = 6, column = 1, padx = 1, pady = 1) 
        
        APP.AMM = Button(APP)
        APP.AMM["text"] = ("AG")
        APP.AMM["width"] = "6"
        APP.AMM["fg"]   = "gray85"
        APP.AMM["bg"]   = ("gray64")
        APP.AMM["command"] = APP.AG
        APP.AMM.grid(row = 6, column = 2, padx = 1, pady = 1) 
               
        APP.AMM = Button(APP)
        APP.AMM["text"] = ("three6")
        APP.AMM["width"] = "6"
        APP.AMM["fg"]   = "gray85"
        APP.AMM["bg"]   = ("gray64")
        APP.AMM["command"] = APP.THREESIX
        APP.AMM.grid(row = 6, column = 3, padx = 1, pady = 1) 

        APP.AMMK = Button(APP)
        APP.AMMK["text"] = ("UGK")
        APP.AMMK["width"] = "6"
        APP.AMMK["fg"]   = "gray85"
        APP.AMMK["bg"]   = ("gray64")
        APP.AMMK["command"] = APP.UGK
        APP.AMMK.grid(row = 6, column = 4, padx = 1, pady = 1) 
#----------------------------------------------------------------------

        APP.G = Button(APP)
        APP.G["text"] = ("GOOGLE")
        APP.G.config(image=photo3,width="45",height="20")
        APP.G["width"] = "47"
        APP.G["fg"]   = "gray70"
        APP.G["command"] = APP.CHROME
        APP.G.grid(row = 6, column = 6, padx = 9, pady = 1)
#----------------------------------------------------------------------

        APP.AABBCC = Button(APP) 
        APP.AABBCC["text"] = ("CLS")
        APP.AABBCC["width"] = "6"
        APP.AABBCC["fg"]   = "black"
        APP.AABBCC["bg"]   = "snow"
        APP.AABBCC["command"] = APP.CLS
        APP.AABBCC.grid(row = 4, column = 6, padx = 1, pady = 1)

        APP.BB = Button(APP)
        APP.BB["text"] = ("COLOR")
        APP.BB["width"] = "6"
        APP.BB["fg"]   = "ivory"
        APP.BB["bg"]   = "gray85"
        APP.BB["command"] = APP.COLOR
        APP.BB.grid(row = 5, column = 6, padx = 9, pady = 1)
        
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
