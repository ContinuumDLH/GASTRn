set PYUIC=C:\ProgramData\Anaconda3\python.exe -m PyQt5.uic.pyuic
set PATH=C:\ProgramData\Anaconda3\Library\bin;%PATH%
set TGT=QtPJH
set SONA=sonA
REM %PY%\pyuic5.bat -x %TGT%.ui -o %TGT%.py
%PYUIC% -x %TGT%.ui -o %TGT%.py
%PYUIC% -x %SONA%.ui -o %SONA%.py
pause
