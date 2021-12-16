exe\wget.exe http://mescouillessurtonfront.esy.es/launcher/majtest/launcher/new.rar
cls
if exist new.rar call :new
goto:eof
exit
:install
rd data\launch /s /q
wget.exe http://mescouillessurtonfront.esy.es/launcher/launcher/launch.rar
7z.exe x launch.rar
del launch.rar
start start.bat
exit
:new
for /f "delims=" %%i in ('type new.rar') do set "new=%%i"
CALL :ShowGui_ "data\Agraf_packet.agl" #load
if %install% ==1 goto install
if %cont% ==1 del new.rar
goto:eof
:ShowGui_
FOR /F "tokens=1,* delims=:" %%A IN ('exe\AGRAF "%~1" %2') DO SET %%A=%%B