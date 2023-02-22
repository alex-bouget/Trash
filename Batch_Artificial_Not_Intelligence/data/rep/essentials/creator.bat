set ncode=0
set sayatome=0
set sayhuman=0
set arg1=0
set arg2=0
set arg3=0
set arg4=0
set arg5=0
set arg6=0
set arg7=0
set arg8=0
set arg9=0
set arg10=0
set extra=off
set extrain=0

if not "%1" == "" (
	if "%1" == "rep" (
		set sayhuman=%~2
		set ncode=%random%
	)
	if "%1" == "extra" (
		set ncode=%a%
		set sayatome=%b%
		set sayhuman=%c%
		set arg1=%d%
		set arg2=%e%
		set arg3=%f%
		set arg4=%g%
		set arg5=%h%
		set arg6=%i%
		set arg7=%j%
		set arg8=%k%
		set arg9=%l%
		set arg10=%m%
		set extrain=1
		call :compil
		goto:eof
	)
)
:return
set wait=0
cls
echo -----------------------
echo creation d'une question
echo -----------------------
echo.
echo IL EST IMPOSSIBLE DE CREER PLUS DE 10 ARGUMENTS (ce que va dire At0me non compter)
echo.
echo 1-nommer le nom de code de la question : %ncode%
echo 2-que va dire at0me ? : %sayatome%
echo 3-avec quel phrase at0me va repondre ? : %sayhuman%
echo 4-ajouter des arguments (il faut avoir des bases en batch)
echo 5-aide a la librairies At0me
echo 6-compiler
echo 7-fermer
set /p "wait=}"
if %wait% ==1 goto 1
if %wait% ==2 goto 2
if %wait% ==3 goto 3
if %wait% ==4 goto 4
if %wait% ==5 (
	cls
	call library options
	pause
)
if %wait% ==6 goto 5
if %wait% ==7 goto 6
goto return

:1
cls
set wait=0
echo quel serat le nom de code de votre question (cela peut etre un chiffre comme un mot), interdiction d'utiliser des espace
set /p "ncode=}"
cls
echo %ncode%
echo c'est bien ca ?
set /p "wait=oui/non}"
if %wait% ==oui goto return
goto 1

:2
cls
set wait=0
echo que va dire At0me (faire des fautes d'orthographe n'est pas grave et est meme conseiller pour eviter les accents)
echo.
echo les accents ne marches pas
echo.
set /p "sayatome=}"
cls
echo %sayatome%
echo c'est bien ca ?
set /p "wait=oui/non}"
if %wait% ==oui goto return
goto 2

:3
cls
set wait=0
echo mettez ce que l'utilisateur doit marquer pour activer votre reponse
set /p "sayhuman=}"
cls
echo %sayhuman%
echo c'est bien ca ?
set /p "wait=oui/non}"
if %wait% ==oui goto return
goto 3

:4
cls
set wait=0
echo ajouter des Arguments
echo arguments 1: %arg1%
echo arguments 2: %arg2%
echo arguments 3: %arg3%
echo arguments 4: %arg4%
echo arguments 5: %arg5%
echo arguments 6: %arg6%
echo arguments 7: %arg7%
echo arguments 8: %arg8%
echo arguments 9: %arg9%
echo arguments 10: %arg10%
echo.
echo 1-ajouter un arguments
echo 2-changer un arguments
echo 3-changer les places des arguments
echo 4-retour
set /p "wait=}"
if %wait% ==1 goto 41
if %wait% ==2 goto 42
if %wait% ==3 goto 43
if %wait% ==4 goto return
goto 4

:41
echo une phrase batch 
if %arg1% ==0 (
	set /p "arg1="
	goto 4
) else (
	if %arg2% ==0 (
		set /p "arg2="
		goto 4
	) else ( 
		if %arg3% ==0 (
			set /p "arg3="
			goto 4
		) else (
			if %arg4% ==0 (
				set /p "arg4="
				goto 4
			) else (
				if %arg5% ==0 (
					set /p "arg5="
					goto 4
				) else (
					if %arg6% ==0 (
						set /p "arg6="
						goto 4
					) else (
						if %arg7% ==0 (
							set /p "arg7="
							goto 4
						) else ( 
							if %arg8% ==0 (
								set /p "arg8="
								goto 4
							) else (
								if %arg9% ==0 (
									set /p "arg9="
									goto 4
								) else (
									if %arg10% ==0 (
										set /p "arg10="
										goto 4
									) else (
										echo il n'y a plus d'argument libre
										pause>nul
										goto 4 
									)
								)
							)
						)
					)
				)
			)
		)
	)
)

:42
cls
set wait=0
echo quel argument voulez vous changer ?
echo.
echo arguments 1: %arg1%
echo arguments 2: %arg2%
echo arguments 3: %arg3%
echo arguments 4: %arg4%
echo arguments 5: %arg5%
echo arguments 6: %arg6%
echo arguments 7: %arg7%
echo arguments 8: %arg8%
echo arguments 9: %arg9%
echo arguments 10: %arg10%
echo.
echo 11: retour
set /p "wait=}"
cls
if %wait% ==1 (
	echo argument 1
	set /p "arg1="
)
if %wait% ==2 (
	echo argument 2
	set /p "arg2="
)
if %wait% ==3 (
	echo argument 3
	set /p "arg3="
)
if %wait% ==4 (
	echo argument 4
	set /p "arg4="
)
if %wait% ==5 (
	echo argument 5
	set /p "arg5="
)
if %wait% ==6 (
	echo argument 6
	set /p "arg6="
)
if %wait% ==7 (
	echo argument 7
	set /p "arg7="
)
if %wait% ==8 (
	echo argument 8
	set /p "arg8="
)
if %wait% ==9 (
	echo argument 9
	set /p "arg9="
)
if %wait% ==10 (
	echo argument 10
	set /p "arg10="
)
if %wait% ==11 goto 4
goto 42

:43
set wait=0
cls
echo CECI EST DANS L'ORDRE
echo si vous voulez faire retour ecriver R
echo.
echo %arg1%
echo %arg2%
echo %arg3%
echo %arg4%
echo %arg5%
echo %arg6%
echo %arg7%
echo %arg8%
echo %arg9%
echo %arg10%
echo.
echo lequel veux tu deplacer
set /p "argdep1=}"
if %argdep1% ==R goto 4
cls

cls
echo CECI EST DANS L'ORDRE
echo.
echo.
echo %arg1%
echo %arg2%
echo %arg3%
echo %arg4%
echo %arg5%
echo %arg6%
echo %arg7%
echo %arg8%
echo %arg9%
echo %arg10%
echo.
echo avec quel arguments voulez vous deplacer l'arguments %ardep1%
set /p "argdep2=}"
set argdepw=%argdep1%
set arg%argdep1%=%argdep2%
set arg%argdep2%=%argdepw%
goto 4

:5
cls
set wait=0
echo nom de code : %ncode%
echo.
echo SI %sayhuman% est poser a At0me alors :
if not "%arg1%" =="0" echo %arg1%
if not "%arg2%" =="0" echo %arg2%
if not "%arg3%" =="0" echo %arg3%
if not "%arg4%" =="0" echo %arg4%
if not "%arg5%" =="0" echo %arg5%
if not "%arg6%" =="0" echo %arg6%
if not "%arg7%" =="0" echo %arg7%
if not "%arg8%" =="0" echo %arg8%
if not "%arg9%" =="0" echo %arg9%
if not "%arg10%" =="0" echo %arg10%
echo At0mes dit : %sayatome%
echo.
echo 1-commencer la compilation
echo 2-options de compilations
echo 3-cela n'est pas bon je continue la creation
set /p "wait=}"
if %wait% ==1 goto compil
if %wait% ==2 goto optionscompil
if %wait% ==3 goto return
goto 5

:optionscompil
cls
set wait=0
echo ---------------------
echo option de compilation
echo ---------------------
echo.
echo 1-activer la save extra : %extra%
echo 2-retour
set /p "wait=}"
if %wait% ==1 (
	if %extra% ==off set extra=on
	if %extra% ==on set extra=off
)
if %wait% ==2 goto 5
goto optionscompil

:compil
if not %extrain% ==1 (
	if not "%arg1%" =="0" echo %arg1%>>rep\%ncode%.bat
	if not "%arg2%" =="0" echo %arg2%>>rep\%ncode%.bat
	if not "%arg3%" =="0" echo %arg3%>>rep\%ncode%.bat
	if not "%arg4%" =="0" echo %arg4%>>rep\%ncode%.bat
	if not "%arg5%" =="0" echo %arg5%>>rep\%ncode%.bat
	if not "%arg6%" =="0" echo %arg6%>>rep\%ncode%.bat
	if not "%arg7%" =="0" echo %arg7%>>rep\%ncode%.bat
	if not "%arg8%" =="0" echo %arg8%>>rep\%ncode%.bat
	if not "%arg9%" =="0" echo %arg9%>>rep\%ncode%.bat
	if not "%arg10%" =="0" echo %arg10%>>rep\%ncode%.bat
	echo set text=%sayatome%>>rep\%ncode%.bat
	echo goto:eof>>rep\%ncode%.bat
	echo ::Creer avec At0me creator>>rep\%ncode%.bat
)
if %extrain% ==1 (
	if not "%arg1%" =="0 " echo %arg1%>>rep\%ncode%.bat
	if not "%arg2%" =="0 " echo %arg2%>>rep\%ncode%.bat
	if not "%arg3%" =="0 " echo %arg3%>>rep\%ncode%.bat
	if not "%arg4%" =="0 " echo %arg4%>>rep\%ncode%.bat
	if not "%arg5%" =="0 " echo %arg5%>>rep\%ncode%.bat
	if not "%arg6%" =="0 " echo %arg6%>>rep\%ncode%.bat
	if not "%arg7%" =="0 " echo %arg7%>>rep\%ncode%.bat
	if not "%arg8%" =="0 " echo %arg8%>>rep\%ncode%.bat
	if not "%arg9%" =="0 " echo %arg9%>>rep\%ncode%.bat
	if not "%arg10%" =="0 " echo %arg10%>>rep\%ncode%.bat
	echo set text=%sayatome%>>rep\%ncode%.bat
	echo goto:eof>>rep\%ncode%.bat
	echo ::Creer avec At0me creator>>rep\%ncode%.bat
)
cls
echo if "%%don%%" =="%sayhuman%" set lel=%ncode%>>asset_pl.bat
echo         %sayhuman%>>asset_pl.txt
cls
if %extrain% ==1 goto:eof
if %extra% ==on (
	cd ..
	echo set a=%ncode%>>loader\%ncode%.bat
	echo set b=%sayatome%>>loader\%ncode%.bat
	echo set c=%sayhuman%>>loader\%ncode%.bat
	echo set d=%arg1% >>loader\%ncode%.bat
	echo set e=%arg2% >>loader\%ncode%.bat
	echo set f=%arg3% >>loader\%ncode%.bat
	echo set g=%arg4% >>loader\%ncode%.bat
	echo set h=%arg5% >>loader\%ncode%.bat
	echo set i=%arg6% >>loader\%ncode%.bat
	echo set j=%arg7% >>loader\%ncode%.bat
	echo set k=%arg8% >>loader\%ncode%.bat
	echo set l=%arg9% >>loader\%ncode%.bat
	echo set m=%arg10% >>loader\%ncode%.bat
	cd data
)
echo et c'est fini.
pause
goto return

:6
goto:eof