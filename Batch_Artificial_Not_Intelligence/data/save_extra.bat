@echo off
set don=0
set text=0
set lel=0
set wait=0
set sdq=0
echo lequel voulez vous entrer (sans le .bat) ?
echo.
cd loader
for %%A in ("*.bat") do echo %%~A
cd ..
echo.
set /p "wait=}"
if not exist loader\%wait%.bat goto no
call loader\%wait%.bat
cd data
call rep\essentials\creator.bat extra
echo le packet a ete installer
pause
exit

:no
echo le packet n'existe pas
pause
exit