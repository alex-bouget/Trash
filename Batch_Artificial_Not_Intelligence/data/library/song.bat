@echo off
title song
call load.bat
del load.bat
library\cmdmp3 "%song%" >nul
exit