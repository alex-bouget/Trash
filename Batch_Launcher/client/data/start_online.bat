@echo off 
cls
Call data\launch\V.bat
if not exist cache\DATA.C Call data\cache.bat
if not exist data\launch\launch.bat goto download
Call data\newload.bat
Call data\launch\launch.bat
exit

:download