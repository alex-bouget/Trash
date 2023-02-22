set text=quel jeu voulais vous jouer ?
call library speech
dir game
set /p "wait=}"
if exist game/%wait% (
	call game/%wait%/game.bat
)
set text=arret