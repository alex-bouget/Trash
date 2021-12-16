@echo off
for /f "delims=" %%i in ('type data\start.xfiles') do set "start=%%i"
start data\start_%start%.bat