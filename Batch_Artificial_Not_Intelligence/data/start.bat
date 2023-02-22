@echo off
cd data
if not exist Aie_player.bat (
	set me=Aie_player
	goto error
)
if not exist return.bat (
	set me=Aie_player
	goto error
)
if not exist asset_cr.bat (
	set me=asset_cr
	goto error
)
if not exist asset_pl.bat (
	set me=asset_pl
	goto error
)
if not exist library.bat (
	set me=library
	goto error
)
if not exist library (
	set me=library
	goto error
)
call Aie_player.bat

:error
echo error 1 : %me% not found
exit