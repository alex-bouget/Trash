title launcher packet data
for /f "delims=" %%i in ('type cache\31B.cache') do set "L1=%%i"
for /f "delims=" %%y in ('type cache\32B.cache') do set "L2=%%y"
for /f "delims=" %%a in ('type cache\33B.cache') do set "L3=%%a"
for /f "delims=" %%g in ('type cache\34B.cache') do set "L4=%%g"
if exist data.xfilestimes CALL :launcher
CALL :ShowGui_ "data\launch\Agraf_packet.agl" #compte
if %conn% ==1 goto conn
if %create% ==1 goto create
exit
REM création d'un compte
:create
CALL :ShowGui_ "data\launch\Agraf_packet.agl" #comptecre
if not %creterminer% ==1 exit
echo open files.000webhost.com>> temp.dat
echo %L1%%L4%>> temp.dat
echo %L2%%L3%>> temp.dat
echo cd save>> temp.dat
echo get %naig%.xfilestimes>> temp.dat
echo bye>> temp.dat
exe\ftp.exe -s:temp.dat
del temp.dat
REM envoie le compte au serveur
if exist %naig%.xfilestimes goto nop
echo --------------- >> data.xfilestimes
echo %name% >> data.xfilestimes
echo --------------- >> data.xfilestimes
echo %mail% >> data.xfilestimes
echo --------------- >> data.xfilestimes
echo %naig% >> data.xfilestimes
echo --------------- >> data.xfilestimes
echo %pass% >> data.xfilestimes
echo --------------- >> %naig%.xfilestimes
echo %name% >> %naig%.xfilestimes
echo --------------- >> %naig%.xfilestimes
echo %mail% >> %naig%.xfilestimes
echo --------------- >> %naig%.xfilestimes
echo %naig% >> %naig%.xfilestimes
echo --------------- >> %naig%.xfilestimes
echo %pass% >> %naig%.xfilestimes
echo open files.000webhost.com>> temp.dat
echo %L1%%L4%>> temp.dat
echo %L2%%L3%>> temp.dat
echo cd save>> temp.dat
echo put %naig%.xfilestimes>> temp.dat
echo bye>> temp.dat
exe\ftp.exe -s:temp.dat
del temp.dat
cls
del %naig%.xfilestimes
exit
:nop
cls
echo le nom in game a deja etait utilise veuillez reessayer
del %naig%.xfilestimes
exit
REM stop la création du compte



REM connexion du compte
:conn
CALL :ShowGui_ "data\launch\Agraf_packet.agl" #comptecon
if not %connexion% ==1 exit
REM télechargement du fichier sur le serveur
echo open files.000webhost.com>> temp.dat
echo %L1%%L4%>> temp.dat
echo %L2%%L3%>> temp.dat
echo cd save>> temp.dat
echo get %naig%.xfilestimes>> temp.dat
echo bye>> temp.dat
exe\ftp.exe -s:temp.dat
del temp.dat
rename %naig%.xfilestimes test.xfilestimes
REM tester code/adresse mail
for /f "delims=" %%a in ('more/e +2 ^< test.xfilestimes') do if not defined ligne  set "mail1=%%a"
REM mdp
if not %mdp% ==%mail1% goto no
for /f "delims=" %%a in ('more/e +3 ^< test.xfilestimes') do if not defined ligne set "ligne=%%a"
REM mail
if not %mail% ==%ligne% goto no
rename test.xfilestimes data.xfilestimes
start start.bat
:no
del test.xfilestimes
exit
REM stop connexion du compte



:launcher
REM Ouvre le launcher
set play=0
set options=0
set quit=0
CALL :ShowGui_ "data\launch\Agraf_packet.agl" #launcher
if %play% ==1 goto play
if %options% ==1 goto options
if %quit% ==1 exit
exit
:play
REM Ouvre le menu de jeu
REM Remmetre le menu a 0
set ret=0
set des=0
set maj=0
set jouer=0
set scratch=0
set advgame=0
REM Remmetre le gestionnaire a 0
set jouer=0
set maj=0
set des=0
set ret=0
CALL :ShowGui_ "data\launch\Agraf_packet.agl" #play
if %scratch% ==1 goto scratch
if %advgame% ==1 goto advgame
if %ret% ==1 goto launcher
goto launcher
:options
REM Ouvre les options
CALL :ShowGui_ "data\launch\Agraf_packet.agl" #options
if %supcompte% ==1 goto supcompte
if %ret% ==1 goto launcher
if %decco% ==1 del data.xfilestimes
exit
:supcompte
REM Supprimer le compte sur le serveur
for /f "delims= " %%a in ('more/e +5 ^<data.xfilestimes ') do if not defined ligne set "ligne=%%a"
echo open files.000webhost.com>> temp.dat
echo serv001ftpsql>> temp.dat
echo azertyuiop12345>> temp.dat
echo cd save>> temp.dat
echo delete %ligne%.xfilestimes>> temp.dat
echo bye>> temp.dat
exe\ftp.exe -s:temp.dat
del temp.dat
del data.xfilestimes
exit


REM OPEN SCRATCH
:scratch
if not exist ProgramFiles\scratch_launcher\launch.bat goto majscratch 
CALL :ShowGui_ "data\launch\Agraf_packet.agl" #gestionnaire
if %jouer% ==1 goto scratchgo
if %maj% ==1 goto majscratch
if %des% ==1 goto desscratch 
if %ret% ==1 goto play
goto play
:scratchgo
start ProgramFiles\Scratch_launcher\launch.bat
exit
:majscratch
exe\wget.exe http://mescouillessurtonfront.esy.es/launcher/ProgramFiles/scratchlauncher/scratch.rar
exe\7z.exe x scratch.rar
del scratch.rar
goto play
:desscratch
rd ProgramFiles\scratchlauncher /s /q
goto play




:ShowGui_
FOR /F "tokens=1,* delims=:" %%A IN ('exe\AGRAF "%~1" %2') DO SET %%A=%%B