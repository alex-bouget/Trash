@echo off
if exist engine.xfiles for /f "delims=" %%i in ('type engine.xfiles') do set "engine=%%i"
start engine\engine.exe %engine%
del engine.xfiles
exit