set text=quel son voulez vous que je joue
call library speech
set song=0
set /p "song=sans le .mp3}"
if %song% ==0 goto:eof
call library music song\%song%.mp3 true
set text=fin du son
goto:eof