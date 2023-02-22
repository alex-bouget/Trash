set text=sette question n'a pas de reponse voulais vous craiei une reponse ?
call library speech
echo 1-oui
echo 2-non
set /p "ml=}"
if /i %ml% == 1 call rep\essentials\creator.bat rep "%don%" 
set text=trai bien