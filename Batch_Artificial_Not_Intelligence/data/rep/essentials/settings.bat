:return
cls
set wait=0
echo --------------
echo At0me Settings
echo -------------- 
echo.
echo 1-Aide
echo 2-Demande creation de reponse
echo 3-Regle de At0me
echo 4-CASSE
echo 5-At0me packet creator
echo 6-retour a At0me
set /p "wait=}"
if %wait% ==1 goto 1
if %wait% ==2 goto 2
if %wait% ==3 goto 3
if %wait% ==4 goto 4
if %wait% ==5 goto 5
if %wait% ==6 goto 6
goto return

:1
set wait=0
cls
echo --------------
echo At0me Settings
echo -------------- 
echo.
echo 1-Ajout de packet a At0me
echo 2-je n'entends pas At0me
echo 3-retour
set /p "wait=}"
if %wait% ==1 goto 11
if %wait% ==2 goto 12
if %wait% ==3 goto return
goto 1

:11
set wait=0
cls
echo --------------
echo At0me Settings
echo -------------- 
echo.
echo At0me est interchangeable est l'on peut ajouter un a plusieurs packet
echo tant qu'il n'ont pas le meme nom de code
echo si ils ont le meme nom de code vous pouvez le changez en regardant sur notre site internet
pause
goto 1

:12
goto 1

:2
set wait=0
cls
echo --------------
echo At0me Settings
echo -------------- 
echo.
echo voulez activer le systeme de demande de question
echo.
echo 1-oui
echo 2-non
echo 3-kezako ?
echo 4-fermer
echo.
set /p "wait=}"
if %wait% == 1 echo set sdq=0 >> settings.bat
if %wait% == 2 echo set sdq=1 >> settings.bat
if %wait% == 3 goto 23
goto return

:23
set wait=0
cls
echo --------------
echo At0me Settings
echo -------------- 
echo.
echo le systeme de demande de question est systeme servant a demander a l'utilisateur si il veut creer une reponse pour une question poser dont la reponse est inexistante
pause
goto 2

:3
cls
echo --------------
echo At0me Settings
echo -------------- 
echo.
echo regle de At0me :
echo 1-Les idees racistes donner par At0me et creer par vous restent sur votre ordinateur et n'a rien a faire sur notre site internet
echo 2-amuser vous
echo 3-Si vous avez recuperez un fichier At0me qui a detruit votre ordinateur nous ne sommes en aucun cas les fautifs
pause
goto return

:4
cls
echo --------------
echo At0me Settings
echo -------------- 
echo.
echo cette endroit est casse
pause
goto return

:5
call rep\essentials\creator.bat
goto return

:6
set text=options de Atome fermer
goto:eof