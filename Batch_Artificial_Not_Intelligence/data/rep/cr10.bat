set /a wait=%random% %% 8 + 1
set song=cr%wait%
call library music song\%song%.mp3 true
goto:eof