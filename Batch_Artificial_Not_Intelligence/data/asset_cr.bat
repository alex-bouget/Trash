REM Essentials At0me :
if "%don%" =="settings" set lel=essentials\settings
if "%don%" =="creator" set lel=essentials\creator
Rem packet At0me :
if "%don%" =="ouvre un jeu" set lel=cr1
if "%don%" =="ouvre notepad" set lel=cr2
if "%don%" =="aime tu le cafe" set lel=cr3
if "%don%" =="je n aime pas les robot" set lel=cr4
if "%don%" =="qu est qui est jaune et qui attends" set lel=cr5
if "%don%" =="j aime les frites" set lel=cr6
if "%don%" =="apple c de la merde" set lel=cr7
if "%don%" =="ouvre cmd" set lel=cr8
if "%don%" =="pions noirs" set lel=cr9
if "%don%" =="met un son createur aleatoire" set lel=cr10
if "%don%" =="joue un son" set lel=cr11
if "%don%" =="joue tout les son createur" set lel=cr12
if "%don%" =="help" set lel=cr13
if %sdq% == 1 goto:eof
if %sdq% == 0 (
	if "%lel%" =="0" set lel=cr14
)
if "%don%" ==" " set lel=cr15
if "%don%" =="0" set lel=cr16
