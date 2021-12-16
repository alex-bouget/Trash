@echo off
title launcher packet data
if not exist ProgramFiles\Scratch_launcher\engine\engine.bat goto majengine
:launcher
set Scratch_engine=0
set Scratch_engine=0
set install_game=0
set play=0
CALL :ShowGui_ "ProgramFiles\Scratch_launcher\Agraf_packet.agl" #L1
if %Scratch_engine% ==1 goto engine
if %install_game% ==1 goto install_game
if %play% ==1 goto play
exit

:engine
set majengine=0
set ret=0
CALL :ShowGui_ "ProgramFiles\Scratch_launcher\Agraf_packet.agl" #compte
if %majengine% ==1 goto testengine
if %ret% ==1 goto launcher
:test engine
:majengine
exit

:install_game
goto launcher

:play
set "apple=1"
if %apple% ==1 (
set "game=game\appleclicker\01\data.scratch"
call :playengine
)
if %dodge% ==1 (
set "game=game\dodgeball\01\data.scratch"
call :playengine
)
goto launcher

:playengine
cd ProgramFiles\Scratch_launcher
echo %game%>> engine.xfiles
start engine\engine.bat
exit

:ShowGui_
FOR /F "tokens=1,* delims=:" %%A IN ('exe\AGRAF "%~1" %2') DO SET %%A=%%B