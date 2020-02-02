cd /
echo off
mode con: cols=50 lines=30
cls
set "Python=Python27"
cd \%Python%
@color 10
pip install label
echo label
pause
cd \%Python%
@color 01
pip install goto-statement
echo goto
pause
cd \%Python%
@color 02
"C:\%Python%\python.exe" -m pip install  pip --upgrade
echo Update was INSTALLED
pause
cd \%Python%
@color 03 
pip install libarchive-dev
echo libarchive-dev was INSTALLED
pause
cd \%Python%
@color 04
pip install colorama
echo colorama was INSTALLED
pause
cd \%Python%
@color 05
pip install auto-py-to-exe
echo auto-py-to-exe was INSTALLED
@color 06
pip install pyinstall
echo pyinstall was INSTALLED
timeout /t 4 > NUL
@color 74
echo all done...!!!
echo Hopefully it all went ok...
timeout /t 7 > NUL