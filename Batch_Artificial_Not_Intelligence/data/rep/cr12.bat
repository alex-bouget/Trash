set songID=0
:r
set /a songId=%songID%+1
set song=cr%songID%
if not exist song\%song%.mp3 goto:eof
call library music song\%song%.mp3 true
set text=fin des son
goto r