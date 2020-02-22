cd /
echo off
mode con: cols=50 lines=30
cls
set "Python=Python27"
set "PY=C:\%Python%\Scripts\pip.exe"
cd C:\%Python%
@color 01
%PY% install goto-statement
echo goto
cd C:\%Python%
@color 02
%PY% install  pip --upgrade
echo Update was INSTALLED
cd C:\%Python%
@color 03 
%PY% install libarchive-dev
echo libarchive-dev was INSTALLED
cd C:\%Python%
@color 04
%PY% install colorama
echo colorama was INSTALLED
cd C:\%Python%
@color 05
%PY% install auto-py-to-exe
echo auto-py-to-exe was INSTALLED
@color 06
%PY% install pyinstall
echo pyinstall was INSTALLED
timeout /t 4 > NUL
@color 74
echo all done...!!!
echo Hopefully it all went ok...
timeout /t 7 > NUL