@echo off
if not exist start.bat exit
cls
md cache
:Start
if [%E2%]==[] set E2=0
if [%E1%]==[] set E1=0
if [%E0%]==[] set E0=0
:E0
if %E0%==9 goto E1
if %E0%==8 set E0=9
if %E0%==7 set E0=8
if %E0%==6 set E0=7
if %E0%==5 set E0=6
if %E0%==4 set E0=5
if %E0%==3 set E0=4
if %E0%==2 set E0=3
if %E0%==1 set E0=2
if %E0%==0 set E0=1
goto DONE
:E1
set E0=0
if %E1%==9 goto E2
if %E1%==8 set E1=9
if %E1%==7 set E1=8
if %E1%==6 set E1=7
if %E1%==5 set E1=6
if %E1%==4 set E1=5
if %E1%==3 set E1=4
if %E1%==2 set E1=3
if %E1%==1 set E1=2
if %E1%==0 set E1=1
goto DONE
:E2
set E1=0
if %E2%==9 set E2=0
if %E2%==8 set E2=9
if %E2%==7 set E2=8
if %E2%==6 set E2=7
if %E2%==5 set E2=6
if %E2%==4 set E2=5
if %E2%==3 set E2=4
if %E2%==2 set E2=3
if %E2%==1 set E2=2
if %E2%==0 set E2=1
goto E0
:DONE
echo %E2%%E1%%E0%=*cache*>>cache\%E2%%E1%%E0%.cache
echo load: %E2%%E1%%E0%.cache if *cache*=*%E2%%E1%%E0%-1*>>cache\%E2%%E1%%E0%.Cload
if %E2% ==1 goto OK
goto Start
:OK
echo DELETED>>cache/31B.cache
echo DELETED>>cache/32B.cache
echo DELETED>>cache/33B.cache
echo DELETED>>cache/34B.cache
echo set/set>>cache\DATA.C