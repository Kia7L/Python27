cd /
mode con: cols=77 lines=45
echo off
color 10
cls







echo. Place 'FOLDER' ON 
echo. "%Userprofile%\Documents\Rainmeter\Skins\DarkDragonRainmeter\@Resources\python\" 
echo. Place .py in that folder PLEASE...
cd %Userprofile%\Documents\Rainmeter\Skins\DarkDragonRainmeter\@Resources\python\
set /p ICON=icon TO_USE:
set /p PY=Type_NAME.py:
pyinstaller -F -i "%Userprofile%\Documents\Rainmeter\Skins\DarkDragonRainmeter\@Resources\python\%ICON%.ico" "%Userprofile%\Documents\Rainmeter\Skins\DarkDragonRainmeter\@Resources\python\%PY%.py
timeout /t 1
echo all done...Finish......!!!
echo Hopefully it all went ok...
timeout /t 6

exit